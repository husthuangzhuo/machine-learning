# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:13:52 2018

@author: DELL
"""
from collections import Counter
from KNN import *
from os import listdir
def img2vector(filename):
    file = open(filename)
    X = []
    numoflines = file.readlines()
    for i in numoflines:
        i = i.strip('\n')
        for j in i:
            X.append(int(j))
#    X = np.array(X)
#    X = X.reshape((1,-1))
    return X

def imgset2XY(filepath):
    trainingset = listdir(filepath) ##将路径下的文件名依次写入一个list中
    numofdata = len(trainingset)
    Y = np.zeros((numofdata, 1))
    X = []
    for i in range(numofdata):
        filename = trainingset[i]
        Y[i,0] = int(filename[0])
        X += img2vector(filepath + '\\' + filename)
    X = np.array(X)
    X = X.reshape((numofdata,-1))
    return X,Y

filepath = 'digits\\trainingDigits'
X_train,Y_train = imgset2XY(filepath)
testpath = 'digits\\testDigits'
X_test,Y_test = imgset2XY(testpath)
print(X_train.shape)
print(X_test.shape)

error = 0
for i in range(X_test.shape[0]):
    x_test = X_test[i, :]
    y_test = Y_test[i,:]

    x_test_classifer = classify(x_test, X_train, Y_train, k=3)
    print('the classifier came back with:' + str(x_test_classifer) + ', the real number is: ' + str(y_test))
    if x_test_classifer != y_test:
        error += 1

print('the total error rate is:' + str(error/X_test.shape[0]))


    
    