from unittest import TestLoader
from numpy import *
import operator

def classify0(input_x,datasets,labels,k):
    singledis = datasets - input_x
    singledis2 = singledis ** 2
    sqdistances = singledis2.sum(axis = 1)
    distances = sqdistances**0.5
    index_up_sorted_list = distances.argsort()
    classcount = {}
    for i in range(k):
        label = labels[index_up_sorted_list[i]]
        classcount[label] = classcount.get(label,0)+1
    sortedClassCount = sorted(classcount.items(),reverse=True,key=operator.itemgetter(1))
    return sortedClassCount[0][0]


def creatDataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def file2matrix(filepath,split_item=' ',need_strip = False):
    fr = open(filepath,mode="r")
    arrayLines = fr.readlines()
    sample_number = len(arrayLines)
    if(need_strip):
        feature_number = len(arrayLines[0].strip().split(split_item)) - 1
    else:
        feature_number = len(arrayLines[0].split(split_item)) - 1
    return_featureMatrix = zeros((sample_number,feature_number))
    return_labels = zeros(sample_number)
    index = 0
    for line in arrayLines:
        if(need_strip):
            line = line.strip()
        lineArray = line.split(split_item)
        return_featureMatrix[index,:] = lineArray[0:feature_number]
        return_labels[index] = lineArray[-1]
        index+=1
    fr.close()
    return return_featureMatrix,return_labels

def autoNorm(dataset):
    min = dataset.min(0) # 从列中选最小值
    max = dataset.max(0)
    ranges = max-min
    normDataset = (dataset-min)/ranges
    sample_number = dataset.shape[0]
    return normDataset, ranges, sample_number
    # minVals = dataset.min(0)
    # maxVals = dataset.max(0)
    # ranges = maxVals -minVals
    # normDataSet = zeros(shape(dataset))
    # m = dataset.shape[0]
    # normDataSet = dataset - tile(minVals,(m,1))
    # normDataSet = normDataSet/tile(ranges,(m,1))
    # return normDataSet,ranges,minVals

def split_dataset(dataset,hoRatio):
    total_sample_number = dataset.shape[0]
    train_data = dataset[:int(total_sample_number*(1-hoRatio)),:]
    test_data = dataset[int(total_sample_number*(1-hoRatio)):,:]
    return train_data,test_data

def split_labels(labels,hoRatio):
    total_sample_number = labels.shape[0]
    train_labels = labels[:int(total_sample_number*(1-hoRatio))]
    test_labels = labels[int(total_sample_number*(1-hoRatio)):]
    return train_labels,test_labels

def split_data(dataset,labels,hoRatio):
    train_data, test_data = split_dataset(dataset,hoRatio)
    train_labels, test_labels = split_labels(labels,hoRatio)
    return train_data, test_data, train_labels, test_labels

def kNNTest(dataset,labels,hoRatio = 0.1,k=5):
    total_sample_number = labels.shape[0]
    train_data, test_data, train_labels, test_labels=split_data(dataset,labels,hoRatio)
    test_sample_namber = test_labels.shape[0]
    right_count = 0
    for i in range(test_sample_namber):
        classify_result = classify0(test_data[i],train_data,train_labels,k)
        if classify_result == test_labels[i]:
            right_count += 1
    return right_count/test_sample_namber



