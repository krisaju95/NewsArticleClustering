import pickle
import numpy as np
import pandas as pd
import math
import os

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
wordSetSize = len(dataFrame2.columns)
numberOfDocuments = len(dataFrame2.index)

# Compute cosine similarity given two documents
def cosineSimilarity(value1 , value2):
    d1 = 0
    d2 = 0
    dot = 0
    for row in value1.index:
        d1 = d1 + (value1.ix[row, 0])**2
    for row in value2.index:
        d2 = d2 + (value2.ix[row, 0])**2
        
    for row in value1.index:
        dot = dot + ( value1.ix[row, 0] * value2.ix[row, 0] )
    
    d1 = math.sqrt( d1 )
    d2 = math.sqrt( d2 )
    
    if d1 * d2 == 0:
        return 0
                
    cosineSimilarityValue = dot/(d1*d2)
    return cosineSimilarityValue
    

# Create a dataframe containing cosine similarity values for each document
def calculateCosineSimilarity():
    dataFrame4 = pd.DataFrame(np.zeros(numberOfDocuments).reshape(numberOfDocuments,1))
    
    print "Initialising DataFrame4"
    # Initialise Cosine Similarity Data Frame with zeroes
    for row in range(numberOfDocuments):
        for column in range(numberOfDocuments):
            dataFrame4.ix[row , column] = 0
    
    print "Generating Cosine Similarity Matrix"
      
    for row in range(numberOfDocuments):
        
        document1 = dataFrame3.loc[row , :]
        print "Calculating Cosine Similarity Values for Document " , row + 1 , " of " , numberOfDocuments
        
        for column in range(numberOfDocuments):
            
            document2 = dataFrame3.loc[column , :]
            dataFrame4.ix[row , column] = cosineSimilarity(document1 , document2)
    
    print "Cosine Similarity Matrix generated"
    print "Saving data in DataFrame4 as a pickle package and as a CSV"
                                    
    dataFrame4.to_pickle(os.path.join(path, 'KMeansClustering','dataFrame4.p'))
    dataFrame4.to_csv(os.path.join(path, 'KMeansClustering','dataFrame4.csv'))
    
    print "DataFrame4 has been saved"
    
calculateCosineSimilarity()
