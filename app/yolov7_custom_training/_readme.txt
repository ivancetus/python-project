steps:
0. 安裝套件, 先升級 pip
    pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
    pip install numpy==1.23.5
    pip install opencv-python tqdm requests matplotlib scipy pandas seaborn ipython psutil thop tensorboard PyYAML protobuf==4.21.2 setuptools==59.5.0

1. 下載 yolov7 主程式
    https://github.com/wongkinyiu/yolov7 -> code/download zip

2. 安裝 標示圖片的程式 labelimg
    於系統下開啟 命令提示字元 pip install labelimg

3. 準備訓練資料, 以水果為例, 資料來源: mahaljsp 吳明學老師
    於專案下新建目錄 training_data
        新建目錄 fruits
            於底下新建兩個目錄
                images 存放圖片, 將欲訓練的圖片放置於此
                labels 存放標籤
                    若於 images 有分類目錄, 在 labels底下也需新建同數目的分類目錄, 例如
                    images
                        guava
                        lemon
                        pitaya
                        wax
                    labels
                        guava
                        lemon
                        pitaya
                        wax

4. 於系統下開啟 命令提示字元 輸入 labelimg
    change save format -> YOLO
    open dir 開啟專案下 training_data/fruits/images/ -> 分類目錄
    save dir 選擇專案下 training_data/fruits/labels/ -> 分類目錄
        每完成一個分類, 除了開啟新的分類目錄, 儲存的目錄也須一起更改

    開始標示方塊, 快捷鍵 W
    於要標示的物件左上方按下滑鼠左鍵, 拖移至右下方放開, 輸入分類目錄名稱(若目錄為guava 就輸入 guava)
    完成一張圖的標示後按下save, 快捷鍵 ctrl+s, 接著進行下一張圖的標示

5. 將圖片分成兩組, 一組用來訓練, 一組用來驗證
    撰寫程式碼 split_train_val.py
    訓練 90% -> train.txt
    驗證 10% -> val.txt

6. 設定 cfg
    複製 cfg/training/yolov7.yaml
    改名 fruits.yaml 並更改
        nc: 80
        nc: 4

7. 設定 data
    複製 data/coco.yaml
    改名 fruits.yaml
         修改以下
            train: ./training_data/fruits/train.txt
            val: ./training_data/fruits/val.txt
            test: ./training_data/fruits/test.txt

            nc: 4

            names: ['guava', 'lemon', 'pitaya', 'wax']

8. 開始訓練
    每次重新訓練前, 得刪除 fruits底下的 train.cache
    系統下開啟 命令提示字元 進入專案目錄
    cd E:\GitHub\python-project\app\yolov7_custom_training
    venv\Scripts\python train.py --workers 0 --device 0 --batch-size 8 --data data\fruits.yaml --img 640 640  --cfg cfg\training\fruits.yaml --name yolov7 --hyp data\hyp.scratch.p5.yaml --weights '' --epoch 3000

9. 訓練的權重
    runs\train\yolov7xxxx\weights -> best.pt

10.偵測圖片
    venv\Scripts\python detect.py --weights ./runs/train/yolov72/weights/best.pt --conf 0.1 --source ./training_data/fruits/images/pitaya/00017.jpg
    venv\Scripts\python detect.py --weights ./runs/train/yolov72/weights/best.pt --conf 0.1 --source E:\project\data\img\jpg\guava1.jpg