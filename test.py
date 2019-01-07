from joblib import dump, load
from PIL import Image
import os
import numpy as np

clf = load('svm-clf.joblib')


def process():
    k = 0
    im = Image.open("captcha.jpg")

    box = (60, 11, 68, 21)
    cropped = im.crop(box)
    cropped.save(os.path.join("test", str(k) + ".png"))
    k += 1
    box = (69, 11, 77, 21)
    cropped = im.crop(box)
    cropped.save(os.path.join("test", str(k) + ".png"))
    k += 1
    box = (78, 11, 86, 21)
    cropped = im.crop(box)
    cropped.save(os.path.join("test", str(k) + ".png"))
    k += 1
    box = (87, 11, 95, 21)
    cropped = im.crop(box)
    cropped.save(os.path.join("test", str(k) + ".png"))
    k += 1
    box = (96, 11, 104, 21)
    cropped = im.crop(box)
    cropped.save(os.path.join("test", str(k) + ".png"))
    k += 1

    X = []
    for image in list(sorted(os.listdir("test"), key=len)):
        img = Image.open(os.path.join("test", image)).convert("L")
        bw = np.array(img) // 128
        X.append(clf.predict(bw.ravel().reshape(1, -1)))

    X = [int(x) for x in X]
    return ''.join(str(e) for e in X)
