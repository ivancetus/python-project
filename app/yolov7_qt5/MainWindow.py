# 讀取的檔案有中文則出錯, 解決辦法, 修改 utils/datasets.py 186 行

import random
import sys
import time

import cv2
import numpy as np
import torch
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidgetItem, QFileDialog

from LoadModelThread import LoadModelThread
from PictureThread import PictureThread
from ui.ui_mainwindow import Ui_MainWindow
from utils.datasets import LoadImages
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.torch_utils import select_device
from sdk.IvanCv import IvanCv as cv


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(1920, 1080)
        self.btnPath.clicked.connect(self.btnPathClick)
        self.device = select_device('0')  # 選取 GPU, 若出現錯誤, 確認 torch, 與 torchvision 版本, 以及 cuda版本
        self.lblStatus.setText('載入模型中...')

        self.weights = 'weights/yolov7.pt'
        self.defaultPath = 'E:/project/data/img/yolo7testimg'

        self.loadModelThread = LoadModelThread(self.device, self.weights)
        self.loadModelThread.callback.connect(self.loadModelThreadCallback)
        self.loadModelThread.start()

    def loadModelThreadCallback(self, info):
        self.model = info[0]
        self.stride = info[1]
        self.lblStatus.setText('')
        self.lblPath.setText(self.defaultPath)
        self.path = self.lblPath.text()
        self.picThread = PictureThread(self.path)
        self.picThread.callback.connect(self.showPicture)
        self.picThread.start()

    def showPicture(self, picture):
        btn = QPushButton()
        btn.setIcon(QIcon(picture))
        btn.setIconSize(QSize(400, 300))
        btn.tag = picture.tag.replace('\\', '/')
        btn.clicked.connect(self.btnPictureClick)
        item = QListWidgetItem()
        item.setSizeHint(QSize(400, 300))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, btn)

    def btnPictureClick(self):
        btn = self.sender()
        # self.detect請參照官網的程式碼
        img = self.detect(btn.tag, self.model, self.stride, self.device)
        img = img[:, :, ::-1].copy()

        # 圖片縮放
        h, w, _ = img.shape
        r = w / h
        lbl_w = self.lblShow.width()
        lbl_h = self.lblShow.height()
        lbl_r = lbl_w / lbl_h

        # 原圖若比例過大, 則縮小, 反之放大, 使得以放入標籤lblShow中
        if r > lbl_r:
            img = cv.resize(img, lbl_w, int(lbl_w / r))
        else:
            img = cv.resize(img, int(lbl_h * r), lbl_h)

        # 將 cv2格式轉成 QImage, 再轉成 QPixmap才可放入 QLabel中, 寬 高 RGB, 8bit顏色值
        pix = QPixmap(QImage(
            img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)
        )
        self.lblShow.setPixmap(pix)

    def btnPathClick(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path != '':
            self.path = self.path.replace('\\', '/')
            self.picThread.runFlag = False
            self.picThread = None
            self.lblPath.setText(self.path)
            self.listWidget.clear()
            self.picThread = PictureThread(self.path)
            self.picThread.callback.connect(self.showPicture)
            self.picThread.start()

    def closeEvent(self, event):
        self.picThread.runFlag = False

    def detect(self, file, model, stride, device):
        imgsz = check_img_size(1920, s=stride)  # 偵測影像大小
        dataset = LoadImages(file, img_size=imgsz, stride=stride)  # 載入圖片
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]
        # colors = [[0, 0, 255] for _ in names]  # 自訂標籤顏色
        # torch的使用方式, 需有四維, 第一維紀錄分數
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))
        t0 = time.time()
        for path, img, im0s, vid_cap in dataset:
            # 處理圖片
            img = torch.from_numpy(img).to(device)  # 將圖片由 cv2格式轉成 torch格式
            img = img.half()  # 降低一半的精準度
            img = img/255.0  # 歸一化, 0~255 => 0~1之間, 就不受大小旋轉影響
            if img.ndimension() == 3:
                img = img.unsqueeze(0)  # 在最前面擴充一個維度, 紀錄偵測分數

            # 開始偵測圖片
            # t2-t1是偵測圖片的時間, 約在 0.5秒左右, 目標是 0.033秒, 才能以正常的速度偵測影片
            # yolact可以再縮短, 或透過硬體升級, 演算法改進優化等
            t1 = time.time()
            with torch.no_grad():
                pred = model(img, augment=False)[0]
            t2 = time.time()
            # 刪除多餘的方框, 避免偵測結果出現多個偵測方框
            pred = non_max_suppression(
                pred,
                0.25,  # opt.conf_thres
                0.45,  # opt.iou_thres
                classes=None,  # opt.classes
                agnostic=False  # agnostic_nms
            )
            t3 = time.time()
            # 為每個偵測到的物件畫上方框, 並加上註解
            for i, dst in enumerate(pred):
                s = ''
                if len(dst):  # 有偵測到物件時, 才標示方框
                    # 標示座標
                    dst[:, :4] = scale_coords(img.shape[2:], dst[:, :4], im0s.shape).round()
                    # 列印結果
                    for c in dst[:, -1].unique():
                        n = (dst[:, -1] == c).sum()  # 偵測每一個物件的種類
                        # 增加名稱
                        s += f'{n}{names[int(c)]}{"s"*(n>1)},'
                    for *xyxy, conf, cls in reversed(dst):
                        # 信心度 非 精準度
                        label = f'{names[int(cls)]}{conf:.2f}'  # conf 信心度, 分數
                        # 修改顯示字大小 utils/plot_one_box -> tl / 3, 3改小就變大
                        plot_one_box(xyxy, im0s, label=label, color=colors[int(cls)], line_thickness=1)
                print(
                    f'{s}Done. ({(1E3 * (t2-t1)):.1f}ms) Inference, ({(1E3 * (t3-t2)):.1f}ms) NMS'
                )
        print(f'Done. ({time.time()-t0:.3f}s)')
        return im0s


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
