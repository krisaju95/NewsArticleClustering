import pickle
import numpy as np
import pandas as pd
import os


newsPaperName = "NewsPaper A"
path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame5 = pickle.load( open(os.path.join(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Cosine Similarity', 'dataFrame5.p')), "rb"))
numberOfDocuments = len(dataFrame5.index)
numberOfClusters = 5
    

# Create a dataframe containing cosine similarity values for each document
def computeStatistics():
    unclassified = 0
    clusterScores = pd.DataFrame(np.zeros(numberOfClusters))
    clusterID = 0
    for row in range(numberOfDocuments):
        clusterID = int(dataFrame5.ix[row , "clusterID"])
        if clusterID == -1.0:
            unclassified = unclassified + 1
        else:
            clusterScores.ix[clusterID , 0] = clusterScores.ix[clusterID , 0] + 1
        
    for i in range(numberOfClusters):
        clusterScores.ix[i , 0] = clusterScores.ix[i , 0] / (numberOfDocuments - unclassified) * 100

    print clusterScores
    print unclassified,  " unclassified documents."
    clusterScores.to_csv(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Cosine Similarity','clusterScores.csv'))
    
    
computeStatistics()
#print len(dataFrame3.columns)