import pickle
import os
import pandas as pd
import numpy as np


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = pickle.load(open(os.path.join(path, 'Word Set','wordSet.p'), 'rb'))
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
wordSetSize = len(dataFrame2.columns)
numberOfDocuments = len(dataFrame2.index)
TfIdf_Threshold = 0.006
dataFrame3=dataFrame2.copy()

# Creates a dataframe containing features in each document as document vectors (each row is a vector)
def generateFeatureSet():
    global dataFrame3
    
    print "Generating documents vectors"
    print "TF-IDF threshold value set at ",TfIdf_Threshold
    dataFrame3Matrix = dataFrame3.as_matrix()
    numberOfWords = len(dataFrame3.columns) 
    
    
    for row in range(numberOfDocuments):
        for word in range(numberOfWords):
            if dataFrame3Matrix[row , word] < TfIdf_Threshold:
                dataFrame3Matrix[row , word] = 0.0
                
    dataFrame3 = pd.DataFrame(dataFrame3Matrix)

    print "Document Vectors generated"
    print "Performing Dimensionality Reduction at threshold value"
    
    
    dataFrame3.columns = list(words)
    
    i = 0
    for word in dataFrame3.columns:
        if dataFrame3Matrix[: , i].sum() == 0:
            del dataFrame3[word]
        i = i + 1

    print "Document Vectors saved in DataFrame3"
    print "Saving data in DataFrame3 as a pickle package and as a CSV"
                                                                        
    dataFrame3.to_pickle(os.path.join(path, 'Feature Set','dataFrame3.p'))
    dataFrame3.to_csv(os.path.join(path, 'Feature Set','dataFrame3.csv'))
    
    print "DataFrame3 has been saved"    
    
    
generateFeatureSet()