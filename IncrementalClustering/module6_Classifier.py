import pickle
import numpy as np
import pandas as pd
import math
import os


newsPaperName = "NewsPaper A"
path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame2 = pickle.load( open(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Feature Set','dataFrame3.p'), "rb" ))
wordSetSize = len(dataFrame2.columns)
numberOfDocuments = len(dataFrame2.index)
oldDataFrame3 = pickle.load(open(os.path.join(path, 'Feature Set', 'dataFrame3.p'), "rb" ))
numberOfDocumentsOldDataFrame3 = len(oldDataFrame3.index)
originalClusters = pickle.load(open(os.path.join(path, 'KMeansClustering','dataFrame5.p'), "rb"))
dataFrame4 = pickle.load(open(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Cosine Similarity', 'dataFrame4.p'), "rb"))
dataFrame5 = pd.DataFrame(np.zeros(numberOfDocuments).reshape(numberOfDocuments,1))
numberOfClusters = 5
minSimilarityThreshold = 0.01


# Compute cosine similarity given two documents
def findMostSimilarCluster(documentID):
    clusterID = 0
    #doc = document.as_matrix()
    similarityValues = np.zeros(numberOfClusters)
    clusterSizes = np.zeros(numberOfClusters)
    
    for i in range(numberOfDocumentsOldDataFrame3):
        clusterID = int(originalClusters.ix[i , "ClusterID"])
        similarityValue = dataFrame4.ix[documentID , i]
        similarityValues[clusterID] = similarityValues[clusterID] + similarityValue
        clusterSizes[clusterID] = clusterSizes[clusterID] + 1
    
    similarityValues = np.divide(similarityValues , clusterSizes)
    
    clusterID = np.argmax(similarityValues)
    if np.max(similarityValues) < minSimilarityThreshold:
        clusterID = -1
    
    return clusterID
    

# Create a dataframe containing cosine similarity values for each document
def classifyDocuments():
    print "Classifying Documents"
      
    for row in range(numberOfDocuments):
        
        #document = dataFrame4.loc[row , :]
        mostSimilarCluster = findMostSimilarCluster(row)
        dataFrame5.ix[row , "clusterID"] = int(mostSimilarCluster)
    
    print "Documents classified"
    print "Saving data in DataFrame5 as a pickle package and as a CSV"
    del dataFrame5[0]                                
    dataFrame5.to_pickle(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Cosine Similarity','dataFrame5.p'))
    dataFrame5.to_csv(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Cosine Similarity', 'dataFrame5.csv'))
    
    print "DataFrame5 has been saved"
    
classifyDocuments()
#print len(dataFrame3.columns)