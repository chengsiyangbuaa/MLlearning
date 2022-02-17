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


