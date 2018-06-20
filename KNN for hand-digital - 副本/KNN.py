# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:20:25 2018

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

### 读取文件并赋值给X，Y
def filetodata(filename):
    file = open(filename) #打开文件
    unstructure_data = file.readlines() #读取文件所有行作为一个list，每行作为list中一个元素
    num_of_data = len(unstructure_data)
    Y = np.zeros((num_of_data,1))
    m = unstructure_data[0]
    m = m.strip('\n') #去掉换行符
    m = m.split() #将字符串转换成list
    num_of_feature = len(m) - 1
    X = np.zeros((num_of_data, num_of_feature))
    index = 0
    for i in unstructure_data:
        i = i.strip('\n') #去掉换行符
        i = i.split() #将字符串转换成list
        for j in range(num_of_feature):
            X[index,j] = i[j]
        Y[index,0] = i[-1]
        index += 1
    return X,Y

###  归一化特征值    
def Norm_X(X):
    X_max = np.amax(X, axis = 0) #Maxima along the first axis 取列中最大的值
    X_min = np.amin(X, axis = 0) #Minima along the first axis
    X_norm = (X-X_min)/(X_max-X_min)
    return X_norm

###  归一化测试样本特征值    
def Norm_x_test(x_test,X):
    X_max = np.amax(X, axis = 0) #Maxima along the first axis 取列中最大的值
    X_min = np.amin(X, axis = 0) #Minima along the first axis
    x_test_norm = (x_test-X_min)/(X_max-X_min)
    return x_test_norm
        

def classify(x_test, X, Y, k=3):
    distance = np.sum((x_test-X)**2, axis = 1) #将行中的数相加
    d_sort = sorted(distance)
    line_k = d_sort[k-1]
    idx = [] # 最近邻的k个坐标
    cls = []
    for i in range(len(distance)):
        if distance[i]<=line_k:
            idx.append(i)
            cls.append(Y[i,0])
    cls_count = Counter(cls)
    top_three = cls_count.most_common(3)
    return top_three[0][0]
    # classCount = {}
    # Y_near = Y[idx,0]
    # idx_class1 = np.where(Y_near==1)
    # idx_class1 = idx_class1[0]
    # numofclass1 = len(idx_class1)
    # classCount['class1'] = numofclass1
    # idx_class2 = np.where(Y_near==2)
    # idx_class2 = idx_class2[0]
    # numofclass2 = len(idx_class2)
    # classCount['class2'] = numofclass2
    # idx_class3 = np.where(Y_near==3)
    # idx_class3 = idx_class3[0]
    # numofclass3 = len(idx_class3)
    # classCount['class3'] = numofclass3
    # if classCount['class3']>=classCount['class2'] and classCount['class3']>=classCount['class1']:
    #     return 3
    # elif classCount['class2']>=classCount['class3'] and classCount['class2']>=classCount['class1']:
    #     return 2
    # else:
    #     return 1
    

def ClassTest(X,Y):
    ratio = 0.1
    numofsample = X.shape[0]
    permutation = np.random.permutation(X.shape[0])
    shuffled_X = X[permutation,:]
    shuffled_Y = Y[permutation]
    numoftrain = (1-ratio)*numofsample
    numoftest = ratio*numofsample
#    X_trian = shuffled_X[0:numoftrain,:]
#    Y_trian = shuffled_Y[:numoftrain,0]
#    X_test = shuffled_X[numoftrain:,:]
#    Y_test = shuffled_Y[numoftrain:,0]    
    error = 0
    for i in range(int(numoftest)):
        x_test = X[i,:]
        y = classify(x_test, X, Y)
        if y!=Y[i]:
            error += 1
            print('classifier canme back with:'+ str(y) + ', but real class is'+ str(Y[i]) ) 
    return error/numoftest
    
    

    




