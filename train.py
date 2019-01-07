import os
from collections import Counter
from joblib import dump
from sklearn import metrics
from sklearn.svm import SVC
from PIL import Image
import numpy as np
import pandas as pd

X = []
for image in list(sorted(os.listdir("tmp"), key=len)):
    print(image)
    img = Image.open(os.path.join("tmp", image)).convert("L")
    bw = np.array(img) // 128
    X.append(bw.ravel().tolist())
    new_img = Image.new("1", (8, 10), "white")
    new_img.putdata(bw.ravel().tolist())
    new_img.save(os.path.join("bw", image))


X = np.array(X)
print(X[1])
print(X[3])
y = pd.read_csv('data.csv')
y = y.iloc[:, 1]
y = np.array(y).reshape(-1, 1)
clf = SVC(gamma=0.001, C=100.)  # 0.546
clf.fit(X, y.ravel())


print(metrics.confusion_matrix(y, clf.predict(X)))
print(metrics.accuracy_score(y, clf.predict(X)))
dump(clf, "svm-clf.joblib")