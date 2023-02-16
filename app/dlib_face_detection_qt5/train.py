import os
import cv2
import dlib
import numpy as np
import mysql.connector as mysql
from Gfile.G import G
from sdk.IvanCv import IvanCv as cv

# 使用 gpu偵測人臉時, 圖片大小若超過 1200萬像素(4000*3000)
# 連 RTX-3080Ti 12G都會 out of memory
# 載入模型切換到 gpu會花一些時間
# detector_face = dlib.get_frontal_face_detector()
detector_face_gpu = dlib.cnn_face_detection_model_v1('model/mmod_human_face_detector.dat')
detector_shape = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')
detector_recognition = dlib.face_recognition_model_v1('model/dlib_face_recognition_resnet_model_v1.dat')


def get_descriptor(img):
    # if not gpu, remove [0].rect
    try:
        return np.asarray(
            detector_recognition.compute_face_descriptor(img, detector_shape(img, detector_face_gpu(img, 0)[0].rect))
        )
    except Exception as e:
        print(e)
        return None


path_db = 'E:\\project\\data\\img\\face_detect\\db'
# database table 人臉資料, id, name, descriptor (BLOB), fileName
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database
)
cur = conn.cursor()
files = os.listdir(path_db)
for file in files:
    file = file.lower()
    img = cv2.imdecode(np.fromfile(os.path.join(path_db, file), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    h, w, _ = img.shape
    r = w / h
    if w > 2000:  # 依顯卡記憶體大小做調整
        w = 2000
        h = int(w / r)
        img = cv.resize(img, w, h)
    fileName, _ = os.path.splitext(os.path.basename(os.path.join(path_db, file)))
    name = file.split('_')[0]
    img = img[:, :, ::-1].copy()  # 轉成RGB
    descriptor = get_descriptor(img)
    if descriptor is not None:
        dump = descriptor.dumps()  # 轉成 BLOB
        cmd = 'insert into 人臉資料 (name, descriptor, fileName) values (%s, %s, %s)'
        cur.execute(cmd, (name, dump, fileName))
        print(f'正在寫入 {file} ...')
        conn.commit()
print(f'寫入完畢, 共 {len(files)} 組資料')
cur.close()
conn.close()
