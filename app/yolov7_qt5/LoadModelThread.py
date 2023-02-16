from PyQt5.QtCore import QThread, pyqtSignal

from models.experimental import attempt_load
from utils.general import set_logging
from utils.torch_utils import TracedModel


class LoadModelThread(QThread):
    callback = pyqtSignal(object)
    def __init__(self, device, weights, parent=None):
        super().__init__(parent)
        self.device = device
        self.weights = weights

    def run(self):
        # 載入模型, 參照 yolo7 detect.py
        half = self.device.type != 'cpu'  # 將精準度降為一半, 僅支援 CUDA
        set_logging()
        model = attempt_load(self.weights, map_location=self.device)  # 載入 FP32模型
        stride = int(model.stride.max())  # 捲積時, 每次要步進的值
        model = TracedModel(model, self.device, 1920)
        if half:
            model.half()  # 降低模型精準度, 加快偵測速度
        self.callback.emit((model, stride))
