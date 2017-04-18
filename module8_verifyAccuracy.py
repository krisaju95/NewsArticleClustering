import pickle
import numpy as np
import pandas as pd
import os


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
classifiedDocuments = pd.read_csv(os.path.join(path, 'KMeansClustering','classifiedDocuments.csv'))
outputClassification = pickle.load( open(os.path.join(path, 'KMeansClustering','dataFrame5.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
numberOfDocuments = len(dataFrame3.index)

del classifiedDocuments["Unnamed: 0"]
centroids = pickle.load( open(os.path.join(path, 'KMeansClustering','initialCentroids.p'), "rb" ))
k = len(centroids.index)
df=pd.DataFrame(np.zeros(k).reshape(k,1))



def calculateAccuracy():
    for row in df.index:
        for i in range(k + 1):
            df.ix[row , i] = 0
            df.ix[row + 1, i] = 0    

    for row in outputClassification.index:
        actualClass = 0
        actualClass = classifiedDocuments.ix[row , "actualClass"]
        clusterID = outputClassification.ix[row , "ClusterID"] + 1
        df.ix[int(clusterID) , actualClass] = df.ix[int(clusterID) , actualClass] + 1

    accuracy = 0
    for i in range (1, k + 1):
        accuracy = accuracy + df.ix[i, i]

    accuracy = float(accuracy / numberOfDocuments) * 100 

    print "Confusion Matrix"
    print "----------------"
    print df
    print "\nAccuracy = " , accuracy , "%"
    

def precision(row):
    truePositive = df.ix[row , row]
    falsePositive = 0
    precision = 0
    if truePositive == 0:
        return 0
    for column in df.columns:
        if row != column:
            falsePositive = falsePositive + df.ix[row , column]
    precision = truePositive / (truePositive + falsePositive)
    
    return precision
    
def recall(column):
    truePositive = df.ix[column , column]
    falseNegative = 0
    recall = 0
    if truePositive == 0:
        return 0
    for row in df.index:
        if row != column:
            falseNegative = falseNegative + df.ix[row , column]
    
    recall = truePositive / (truePositive + falseNegative)
    
    return recall 
    

def fMeasure(recall , precision):
    if (recall + precision) == 0:
        return 0
    fMeasure = (2 * recall * precision) / (recall + precision)
    return fMeasure
    
  
def macroAveragedFMeasure():
    macroAveragedFMeasure = 0
    for i in range(k):
        macroAveragedFMeasure = macroAveragedFMeasure + fMeasure(recall(i + 1) , precision(i + 1))
        
    macroAveragedFMeasure = macroAveragedFMeasure / k
    
    print "Macro-Averaged F Score = ", macroAveragedFMeasure
            
calculateAccuracy()
macroAveragedFMeasure()