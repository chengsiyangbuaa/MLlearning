import os


def getFile(fileName):
    cwd = os.getcwd()
    file_dict = {
        'datingTestSet2.txt': cwd + "\\MLiA_SourceCode\\machinelearninginaction\\Ch02\\datingTestSet2.txt",
        'flowers.txt': cwd + "\\MLiA_SourceCode\\flowers.txt"
    }
    return file_dict[fileName]