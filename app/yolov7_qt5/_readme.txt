steps:
1. 更新 pip
    File -> Settings -> Project -> Python Interpreter -> pip

2. 安裝套件
    請勿使用 requirements.txt
    pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
    pip install pyqt5 opencv-python
    yolo所需
        pip install tqdm pandas pyyaml matplotlib requests seaborn scipy

3. 以QtDesigner 設計視窗布局
    參閱: http://mahaljsp.asuscomm.com/index.php/2023/01/10/yolov7%e8%88%87pyqt5/
    將.ui 放置於 專案內 ui目錄底下

4. 編譯.ui檔
    File -> Settings -> Tools -> External Tools -> add
        name: pyUic_yolo7
        program: E:\GitHub\python-lccclass\20221202_machine_learning\22_qt5_yolo7\venv\Scripts\pyuic5.exe
        arg: $FileName$ -o $FileNameWithoutExtension$.py
        working dir: $ProjectFileDir$\ui
    於左側專案檢視視窗內.ui檔按右鍵 -> External Tools -> pyUic_yolo7

5. 下載 yolov7 主程式與權重
    https://github.com/wongkinyiu/yolov7 -> code/download zip
    https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt

6. 撰寫程式碼
    MainWindow.py
    LoadModelThread.py
    PictureThread.py

7. 修改 yolov7 所提供的程式碼
    utils/dataset.py 164
        path = self.files[self.count]
        path = self.files[self.count].replace('\\', '/')

    utils/dataset.py 186
        img0 = cv2.imread(path)  # BGR
        img0 = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

8. 於 MainWindow.py 32, 33
    設定偵測權重與初始圖片的路徑

9. 執行 MainWindow.py 進行偵測


