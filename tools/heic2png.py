# pip install Pillow, pillow-heif
# ref: https://stackoverflow.com/questions/63866180/how-to-convert-from-heic-to-jpg-in-python-on-windows
import os

from PIL import Image
import pillow_heif
path = 'E:\\project\\data\\img\\heic'
png_path = 'E:\\project\\data\\img\\png'
ls = []
tree = os.walk(path)
for root, subdirs, files in tree:
    for file in files:
        if file.lower().endswith('.heic'):
            ls.append(os.path.join(root, file))
if not os.path.exists(png_path):
    os.mkdir(png_path)
for l in ls:
    heif_file = pillow_heif.read_heif(l)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    p = os.path.join(png_path, l.replace('.heic', '.png'))
    image.save(p, format("png"))
