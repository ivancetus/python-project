import pickle

import dlib
import mysql.connector as mysql
from Gfile.G import G
from PyQt5.QtCore import QThread, pyqtSignal


class LoadModelThread(QThread):
    callback = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        self.detector_face_gpu = dlib.cnn_face_detection_model_v1('model/mmod_human_face_detector.dat')
        self.detector_shape = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')
        self.detector_recognition = dlib.face_recognition_model_v1('model/dlib_face_recognition_resnet_model_v1.dat')
        conn = mysql.connect(
            host=G.host,
            user=G.user,
            password=G.password,
            database=G.database
        )
        cur = conn.cursor()
        cmd = 'select * from 人臉資料'
        cur.execute(cmd)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        descriptors = []
        candidates = []
        for row in rows:
            name = row[1]
            descriptor = pickle.loads(row[2])  # 從BLOB轉回 np.array
            candidates.append(name)
            descriptors.append(descriptor)
        # emit tuple
        self.callback.emit((
            self.detector_face_gpu,
            self.detector_shape,
            self.detector_recognition,
            descriptors,
            candidates
        ))
