# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:18:57 2018

@author: DELL
"""

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def plot_scatter(X,Y):    
    ## with label
    f1 = plt.figure(1)
    plt.scatter(X[:,0], X[:,1], 15.0*Y, 15.0*Y)
    plt.xlabel(u'玩游戏视频所消耗的时间百分比')
    plt.ylabel(u'每周消费冰淇淋的公升数')
    plt.legend(loc = 'upper right')
    plt.show()


    f2 = plt.figure(2, figsize=(8, 5), dpi=80)
    # 将三类数据分别取出来
    # x轴代表飞行的里程数
    # y轴代表玩视频游戏的百分比
    type1_x = []
    type1_y = []
    type2_x = []
    type2_y = []
    type3_x = []
    type3_y = []
    labels = Y
    matrix = X
    for i in range(len(labels)):
        if labels[i] == 1:  # 不喜欢
            type1_x.append(matrix[i][0])
            type1_y.append(matrix[i][1])
    
        if labels[i] == 2:  # 魅力一般
            type2_x.append(matrix[i][0])
            type2_y.append(matrix[i][1])
    
        if labels[i] == 3:  # 极具魅力        
            type3_x.append(matrix[i][0])
            type3_y.append(matrix[i][1])
    
    type1 = plt.scatter(type1_x, type1_y, s=20, c='red')
    type2 = plt.scatter(type2_x, type2_y, s=40, c='green')
    type3 = plt.scatter(type3_x, type3_y, s=50, c='blue')
    plt.xlabel(u'每年获取的飞行里程数')
    plt.ylabel(u'玩游戏视频所消耗的时间百分比')
    plt.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc='upper left')
    plt.show()
