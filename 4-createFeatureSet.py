import pickle
import os


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
wordSetSize = len(dataFrame2.columns)
numberOfDocuments = len(dataFrame2.index)
TfIdf_Threshold = 0.01


def generateFeatureSet():
    dataFrame3=dataFrame2.copy()
    
    for row in dataFrame3.index:
        for word in dataFrame3.columns:
             if dataFrame3.ix[row,word] < TfIdf_Threshold:
             #    dataFrame3.ix[row,word] = 1
             #else:
                 dataFrame3.ix[row,word] = 0.0  
    
    notFeatures = []             
    for column in dataFrame3.columns:
        flag = 0
        for row in dataFrame3.index:
            if dataFrame3.ix[row , column] != 0.0:
                flag = 1
                break;
        if flag == 0:
            notFeatures.append(column)
                 
    for word in notFeatures:
        del dataFrame3[word]
                                                                                 
    dataFrame3.to_pickle(os.path.join(path, 'Feature Set','dataFrame3.p'))
    
    
    print dataFrame3
    
    
    
generateFeatureSet()