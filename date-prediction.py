# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:13:52 2018

@author: DELL
"""

import KNN
import Createplot
import numpy as np

X,Y = KNN.filetodata('datingTestSet2.txt')
X_norm = KNN.Norm_X(X)
error_rate = KNN.ClassTest(X_norm,Y)
print('the test error rate is ' + str(error_rate))

x_test = np.zeros((1,3))
x_test[0,0] = float(input('每年获得的飞行常客数：'))
x_test[0,1] = float(input('玩视频游戏所消耗的时间百分比：'))
x_test[0,2] = float(input('每周消耗的冰淇淋公升数：'))
x_test_norm = KNN.Norm_x_test(x_test,X)
y = KNN.classify(x_test_norm, X_norm, Y, k=3)
print('你属于类别：' + str(y))

Createplot.plot_scatter(X,Y)

    
    