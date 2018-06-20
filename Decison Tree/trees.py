from math import log
import operator
import numpy as np



#计算数据集的香农熵
def cal_ShannonEnt(data):
    numofdata = len(data)
    LabelCounts = {}
    for i in data:
        label = i[-1]
        if label not in LabelCounts.keys():
            LabelCounts[label] = 1
        else:
            LabelCounts[label] += 1
    ShannonEnt = 0
    sum = 0
    for key, value in LabelCounts.items():
        sum += value

    for value in LabelCounts.values():
        prob = value/sum
        ShannonEnt -= prob*log(prob,2)
    return ShannonEnt

def createDataset():
    dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    return dataset

# test the function of cal_ShannonEnt
dataset = createDataset()
print('test the function of cal_ShannonEnt:',cal_ShannonEnt(dataset))

def majority(classList):
    classvote = {}
    for vote in classList:
        if vote not in classvote:
            classvote[vote] = 1
        else:
            classvote[vote] += 1
    sortedclass = sorted(classvote.items(),key=lambda item:item[1])
    return sortedclass[-1][0]

##检查majority函数正确性
dataset = createDataset()
classList = [example[-1] for example in dataset]
print('test the function of majority:',majority(classList))

##按照给定特征划分数据集
def splitDataset(dataset,axis,value):
    retdataset= []
    for feavector in dataset:
        if feavector[axis] == value:
            reducedfeaVec = feavector[:axis]
            reducedfeaVec.extend(feavector[axis+1:])
            retdataset.append(reducedfeaVec)
    return retdataset

## 检查splitDataset函数正确与否
dataset = createDataset()
print('test the function of splitDataset:',splitDataset(dataset,0,1))

## 根据分类后的香农熵来选择最好的特征分类
def choosefeature2split(dataset):
    numoffeature = len(dataset[0]) -1 ##最后一列一般是label
    baseEntropy = cal_ShannonEnt(dataset)
    bestfeature = -1
    bestInfoGain = 0
    for axis in range(numoffeature):
        feaList = [example[axis] for example in dataset]
        uniquevalue = set(feaList) ##将特征的值组合成集合，去掉重复的值！！
        newEntropy = 0
        for value in uniquevalue:
            subdataset = splitDataset(dataset,axis,value)
            shannonEnt = cal_ShannonEnt(subdataset) ##计算每种划分方式的信息熵
            prob = len(subdataset)/len(dataset)
            newEntropy += prob*shannonEnt
        InfoGain = baseEntropy - newEntropy
        if InfoGain >= bestInfoGain:
            bestfeature = axis
            bestInfoGain = InfoGain
    return bestfeature

## 检测choosefeature2split函数的正确性
dataset = createDataset()
print('test the function of choosefeature2split:',choosefeature2split(dataset))

##创建树的函数代码
def createTree(dataset,Labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset) == 1 :
        return majority(dataset)
    bestfeat = choosefeature2split(dataset)
    bestfeatLabel = Labels[bestfeat]
    myTree = {bestfeatLabel:{}}
    del(Labels[bestfeat])
    featValue = [example[bestfeat] for example in dataset]
    uniquefeatValue = set(featValue)
    for value in uniquefeatValue:
        subLabels = Labels[:]
        subdataset = splitDataset(dataset, bestfeat, value)
        myTree[bestfeatLabel][value] = createTree(subdataset,subLabels)
    return myTree

##检测createTree的正确性
dataset = createDataset()
Labels = ['no surfacing','flippers']
tree = createTree(dataset,Labels)
print('test the function of createTree:',tree)











