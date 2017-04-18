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
    dotProduct = 0
    v1 = value1.as_matrix()
    v2 = value2.as_matrix()
    document1 = np.square(v1)
    document2 = np.square(v2)

    dotProduct = np.dot(v1 , v2)
    
    d1 = math.sqrt( document1.sum() )
    d2 = math.sqrt( document2.sum() )
    
    if d1 * d2 == 0:
        return 0
                
    cosineSimilarityValue = dotProduct/(d1*d2)
    return cosineSimilarityValue
    

# Create a dataframe containing cosine similarity values for each document
def calculateCosineSimilarity():
    dataFrame4 = pd.DataFrame(np.zeros(shape = (numberOfDocuments , numberOfDocuments)).reshape(numberOfDocuments,numberOfDocuments))
    similarityValue = 0

    print "Generating Cosine Similarity Matrix"
      
    for row in range(numberOfDocuments):
        
        document1 = dataFrame3.loc[row , :]
        print "Calculating Cosine Similarity Values for Document " , row + 1 , " of " , numberOfDocuments
        
        for column in range(numberOfDocuments):
            if column < row:
                document2 = dataFrame3.loc[column , :]
                similarityValue = cosineSimilarity(document1 , document2)
                if similarityValue <= 0.0:
                    similarityValue = 0.0
                dataFrame4.ix[row , column] = similarityValue
                dataFrame4.ix[column , row] = dataFrame4.ix[row , column]
            elif column == row:
                dataFrame4.ix[row , column] = 1.0
            elif column > row:
                break
    
    print "Cosine Similarity Matrix generated"
    
    print "Saving data in DataFrame4 as a pickle package and as a CSV"
                                    
    dataFrame4.to_pickle(os.path.join(path, 'KMeansClustering','dataFrame4.p'))
    dataFrame4.to_csv(os.path.join(path, 'KMeansClustering','dataFrame4.csv'))
    
    print "DataFrame4 has been saved"
    
calculateCosineSimilarity()