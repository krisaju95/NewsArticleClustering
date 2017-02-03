import pickle
import numpy as np
import pandas as pd
import math
import os

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
k=4
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
dataFrame4 = pickle.load( open(os.path.join(path, 'KMeansClustering','dataFrame4.p'), "rb" ))
wordSetSize = len(dataFrame3.columns)
numberOfDocuments = len(dataFrame3.index)
centroids = pd.DataFrame(np.zeros(k).reshape(k,1))
cluster1 = set([41])
cluster2 = set([42])
cluster3 = set([43])
cluster4 = set([44])
clusters = [cluster1, cluster2, cluster3, cluster4]
previousClusters = []

def convergenceCase():
    i =0
    if previousClusters == []:
        return False
    for cluster in clusters:
        if cluster != previousClusters[i]:
            return False
        else:
            i = i + 1
    return True
    
    
def initializeCentroids():
    for row in centroids.index:
        for word in dataFrame3.columns:
            centroids.ix[row , word] = dataFrame3.ix[row , word]
    del centroids[0]

def vectorForm(index, df):
    pointVector = []
    for column in df.columns:
        pointVector.append(df.ix[index , column])
        
    return pointVector 


def cosineSimilarity(value1 , value2):
    d1 = 0
    d2 = 0
    dot = 0
    for i in range(len(value1)):
        d1 = d1 + (value1[i])**2
    for i in range(len(value2)):
        d2 = d2 + (value2[i])**2
        
    for i in range(len(value1)):
        dot = dot + ( value1[i] * value2[i])
    
    d1 = math.sqrt( d1 )
    d2 = math.sqrt( d2 )
    
    if d1 * d2 == 0:
        return 0
                
    cosineSimilarityValue = dot/(d1*d2)
    return cosineSimilarityValue
    

def calculateNewCentroids():
    average = []
    
    for i in range(wordSetSize):
        average.append(0)
    clusterID = 0
    for cluster in clusters:
        for i in range(wordSetSize):
            average[i]=0
        for point in cluster:
            v = vectorForm(point, dataFrame3)
            for i in range(len(v)):
                average[i] = average[i] + v[i]
        for i in range(len(average)):
            centroids.ix[clusterID , i] = average[i] / k
            #centroids.ix[clusterID , i]
        clusterID = clusterID + 1


def kMeansClustering():
    initializeCentroids()
    mostSimilarCentroid = 0
    iterationCount = 1
    global previousClusters
    for i in range(10):
        #print previousClusters 
        calculateNewCentroids()
        #print centroids
        cluster1.clear()
        cluster2.clear()
        cluster3.clear()
        cluster4.clear()
        for point in dataFrame4.index:
            pointVector = vectorForm(point , dataFrame3)
            maxSimilarity = 0
            for centroid in centroids.index:
                centroidVector = vectorForm(centroid , centroids)
                if cosineSimilarity(centroidVector , pointVector) > maxSimilarity:
                    maxSimilarity = cosineSimilarity(centroidVector , pointVector)
                    mostSimilarCentroid = centroid
            if mostSimilarCentroid == 0:
                cluster1.add(point)
            elif mostSimilarCentroid == 1:
                cluster2.add(point)
            elif mostSimilarCentroid == 2:
                cluster3.add(point)
            elif mostSimilarCentroid == 3:
                cluster4.add(point)
        
        clusters = [cluster1, cluster2, cluster3, cluster4]        
        if convergenceCase():
            print "converged"
            break
        else:
            print "not converged"
            previousClusters = list(clusters)
            iterationCount = iterationCount + 1
    #print iterationCount

kMeansClustering()
print clusters