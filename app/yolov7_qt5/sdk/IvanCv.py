# version: 2023-0100
# authorized: Ivan Teng 2023-01-12 release
import platform
# pip install opencv-python Pillow matplotlib
from enum import IntEnum

import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw


class Direction(IntEnum):
    # 類別變數
    HORIZONTAL = 1
    VERTICAL = 0
    BOTH = -1


class IvanCv:
    @staticmethod
    def read(file):
        img = Image.open(file)
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

    @staticmethod
    def resize(src, width=None, height=None, scale=1):
        h, w, _ = src.shape
        if width is None or height is None:
            width = int(w * scale)
            height = int(h * scale)
        dst = cv2.resize(src, (width, height), interpolation=cv2.INTER_LINEAR)
        return dst

    @staticmethod
    # 指定左上右下的點, 去除未選取的部分
    def crop(src, x1, y1, x2, y2):
        dst = src[y1:y2, x1:x2].copy()
        return dst

    @staticmethod
    def shift(src, x=0, y=0):
        # [1, 0, x]: 水平平移
        # [0, 1, y]: 垂直平移
        m = np.float32([[1, 0, x], [0, 1, y]])
        h, w, _ = src.shape
        # 仿射
        dst = cv2.warpAffine(src, m, (w, h))
        return dst

    # 高度抽象化
    @staticmethod
    def rotation(src, x=None, y=None, angle=0, scale=1):
        h, w, _ = src.shape
        if x is None or y is None:
            x = (w-1)/2
            y = (h-1)/2
        m = cv2.getRotationMatrix2D((x, y), angle, scale)
        dst = cv2.warpAffine(src, m, (w, h))
        return dst

    @staticmethod
    def flip(src, direction=Direction.HORIZONTAL):
        # direction
        #  1: 水平鏡射
        #  0: 垂直鏡射
        # -1: 水平垂直鏡射
        return cv2.flip(src, direction)

    @staticmethod
    def perspective(src, pts1, pts2, w=None, h=None):
        if w is None or h is None:
            h, w, _ = src.shape
        m = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(src, m, (w, h))
        return dst

    @staticmethod
    def write(src, file):
        dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        dst = Image.fromarray(dst)
        dst.save(file)

    @staticmethod
    def blank(w=100, h=100, color=(255, 255, 255)):
        dst = np.zeros([h, w, 3], dtype=np.uint8)
        dst[:] = color
        return dst

    @staticmethod
    def line(src, p1=(0, 0), p2=(0, 0), color=(0, 0, 0), line_width=1):
        cv2.line(src, p1, p2, color, line_width)
        return src

    @staticmethod
    def rectangle(src, p1=(0, 0), p2=(0, 0), color=(0, 0, 0), line_width=1):
        cv2.rectangle(src, p1, p2, color, line_width)
        return src

    @staticmethod
    def circle(src, center=(0, 0), radius=1, color=(0, 0, 0), line_width=1):
        cv2.circle(src, center, radius, color, line_width)
        return src

    @staticmethod
    def ellipse(src, center=(0, 0), axes=(0, 0),
                angle=0, startAngle=0, endAngle=360,
                color=(0, 255, 0), line_width=1):
        cv2.ellipse(src, center, axes, angle, startAngle, endAngle, color, line_width)
        return src

    @staticmethod
    def polylines(src, points, isClose=True, color=(0, 0, 0), line_width=1):
        cv2.polylines(src, [points], isClose, color, line_width)
        return src

    @staticmethod
    def fillPoly(src, points, color=(0, 0, 0)):
        cv2.fillPoly(src, [points], color)
        return src

    @staticmethod
    def text(src, position, txt, size=24, color=(0, 255, 0)):
        pil = Image.fromarray(src)
        if platform.system() == 'Linux':
            font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqz-zenhei.ttc', size)
        else:
            font = ImageFont.truetype('simsun.ttc', size)
        ImageDraw.Draw(pil).text(position, txt, font=font, fill=color)
        return np.asarray(pil)
