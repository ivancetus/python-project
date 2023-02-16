ref: http://mahaljsp.asuscomm.com/index.php/2019/06/14/python_face_match/
models:
    人臉外型68個特徵訓練模型
        shape_predictor_68_face_landmarks.dat.bz2
        http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

    ResNet人臉辨識訓練模型，ResNet用於影像辨識深度學習，非常簡潔的網路框架
        dlib_face_recognition_resnet_model_v1.dat.bz2
        http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2

    人臉訓練資料 (用於 cnn_face_detection_model_v1)
        mmod_human_face_detector.dat.bz2
        http://dlib.net/files/mmod_human_face_detector.dat.bz2

使用 Dlib 需先安裝 CMake, Visual Studio 2019 (C++桌面開發):
    CMake: https://cmake.org/download/

使用 dlib.cnn_face_detection_model_v1 卷積神經網路人臉偵測器, 需要安裝 CUDA 以啟動 GPU做偵測, 否則速度非常慢:
    CUDA 11.8: https://developer.nvidia.com/cuda-toolkit-archive
    若需要 cudnn, 參照官網
        https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html

安裝套件:
    pip install pyqt5 opencv-python Pillow dlib mysql-connector-python

驗證 Dlib 是否可啟用 CUDA:
    import dlib
    print(dlib.DLIB_USE_CUDA)
    >>>>True
    print(dlib.cuda.get_num_devices())
    >>>>1

訓練:
    train.py 設定 要訓練的人臉資料位置, 一張照片中只能有一張臉
    訓練完的結果存到資料庫中

偵測:
    執行 MainWindow.py 開啟視窗, 進行測試
    偵測出的名字會顯示在圖片左上角
    同時也會顯示檔案名稱(對應人名)以供比對

Gfile/G.py 為連接至資料庫的帳號密碼
