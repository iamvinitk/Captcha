import os

from PIL import Image
from collections import Counter

import pandas as pd
import numpy as np


def name_image():
    dataset = []
    y_train = pd.read_csv('result.csv', header=None)
    y_train = np.array(y_train)
    print(y_train)
    for y in y_train:
        dataset.extend(list(str(y[0])))

    print(dataset)
    print(Counter(dataset))
    df = pd.DataFrame(dataset, columns=["result"])
    df.to_csv("data.csv")


def save_image():
    k = 0
    for image in list(sorted(os.listdir("dataset"), key=len))[:1]:
        print(image)
        im = Image.open(os.path.join("dataset", image))

        box = (60, 11, 68, 21)
        cropped = im.crop(box)
        cropped.save(os.path.join("tmp", str(k) + ".png"))
        k += 1
        box = (69, 11, 77, 21)
        cropped = im.crop(box)
        cropped.save(os.path.join("tmp", str(k) + ".png"))
        k += 1
        box = (78, 11, 86, 21)
        cropped = im.crop(box)
        cropped.save(os.path.join("tmp", str(k) + ".png"))
        k += 1
        box = (87, 11, 95, 21)
        cropped = im.crop(box)
        cropped.save(os.path.join("tmp", str(k) + ".png"))
        k += 1
        box = (96, 11, 104, 21)
        cropped = im.crop(box)
        print(cropped)
        cropped.save(os.path.join("tmp", str(k) + ".png"))
        k += 1


def b_n_w():
    img = Image.open("tmp\\0.png").convert("L")
    print(img.size)
    print(np.array(img))
    bw = np.array(img) // 128
    print(bw.flatten())


# name_image()
save_image()
