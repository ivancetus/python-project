import os
import random
imgs_path = 'training_data/fruits/images'
train = open('training_data/fruits/train.txt', 'w')
val = open('training_data/fruits/val.txt', 'w')
fruits = os.listdir(imgs_path)
for fruit in fruits:
    files = os.listdir(os.path.join(imgs_path, fruit))
    ls = [f'./images/{fruit}/{file}' for file in files]
    random.shuffle(ls)
    total = len(ls)
    for i, f in enumerate(ls):
        if i < total * 0.9:
            train.write(f'{f}\n')
        else:
            val.write(f'{f}\n')
train.close()
val.close()
