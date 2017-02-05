import pickle
import numpy as np
import pandas as pd
import os
import math


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
D = set()
A = []
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
cosineSimilarityMatrix = pickle.load( open(os.path.join(path, 'KMeansClustering','dataFrame4.p'), "rb" ))
wordSetSize = len(dataFrame3.columns)
numberOfDocuments = len(dataFrame3.index)
m = 1
k = 4
centroids = pickle.load( open(os.path.join(path, 'KMeansClustering','initialCentroids.p'), "rb" ))
centroidCosineSimilarity = pd.DataFrame(np.zeros(numberOfDocuments).reshape(numberOfDocuments,1))
dataFrame5 = pd.DataFrame(np.zeros(numberOfDocuments).reshape(numberOfDocuments,1))
clusters = []
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


#def initializeDataFrame5():
#    for row


def findMostSimilarCentroids():
    mostSimilarValue = 0
    mostSimilarCentroid = 0
    for row in dataFrame5.index:
        mostSimilarValue = 0
        mostSimilarCentroid = 0
        for column in centroidCosineSimilarity.columns:
            if centroidCosineSimilarity.ix[row , column] > mostSimilarValue:
                mostSimilarValue = centroidCosineSimilarity.ix[row , column]
                mostSimilarCentroid = column

        dataFrame5.ix[row , "ClusterID"] = mostSimilarCentroid
        dataFrame5.ix[row , "maxSimilarityValue"] = mostSimilarValue
    
def initializeSetD():
    for column in cosineSimilarityMatrix.columns:
        D.add(column)                           

def initializeClusters():
    global clusters
    clusters = []
    for i in range(k):
        clusters.append([])


def initializeCentroids():
    for row in centroids.index:
        for word in dataFrame3.columns:
            centroids.ix[row , word] = 0
                                                                        
                                                                                                                                                                                                        
def calculateNewCentroids():
    initializeCentroids()
    clusterID = 0
    clusterSizes = [0 , 0 , 0 , 0]
    for row in dataFrame5.index:
        clusterID = dataFrame5.ix[row , "ClusterID"]
        clusterSizes[int(clusterID)] = clusterSizes[int(clusterID)] + 1
        for word in centroids.columns:            
            centroids.ix[int(clusterID) , word] = centroids.ix[int(clusterID) , word] + dataFrame3.ix[row , word]
            
    for row in centroids.index:
        for word in centroids.columns:
            centroids.ix[row , word] = centroids.ix[row , word] / clusterSizes[row]
        
        
                                                                                                                                                                                                                                           
def calculateCosineSimilarity():
    # Initialise Cosine Similarity Data Frame with zeroes
    for row in range(numberOfDocuments):
        for column in range(k):
            centroidCosineSimilarity.ix[row , column] = 0
    
    # print dataFrame3                
    for row in range(numberOfDocuments):
        document1 = dataFrame3.loc[row , :]
        for column in range(k):
            document2 = centroids.loc[column , :]
            centroidCosineSimilarity.ix[row , column] = cosineSimilarity(document1 , document2)


def generateClusters():
    clusterID = 0
    initializeClusters()
    for row in dataFrame5.index:
        clusterID = int(dataFrame5.ix[row , "ClusterID"])
        clusters[clusterID].append(row)
        

def findClosestCluster(row):
    maxSimilarityValue = 0
    clusterID = 0
    for centroid in centroidCosineSimilarity.columns:
        if centroidCosineSimilarity.ix[row , centroid] > maxSimilarityValue:
            maxSimilarityValue = centroidCosineSimilarity.ix[row , centroid]
            clusterID = centroid
            
    return clusterID , maxSimilarityValue
                     
def updateCentroidData():
    clusterID = 0
    newSimilarityValue = 0
    for row in dataFrame5.index:
        clusterID = int(dataFrame5.ix[row , "ClusterID"])
        if centroidCosineSimilarity.ix[row , clusterID] < dataFrame5.ix[row , "maxSimilarityValue"]:
            clusterID , newSimilarityValue = findClosestCluster(row)
            dataFrame5.ix[row , "maxSimilarityValue"] = newSimilarityValue
            dataFrame5.ix[row , "ClusterID"] = clusterID
            
        

def skMeansClustering():
    global previousClusters
    calculateCosineSimilarity()
    findMostSimilarCentroids()
    generateClusters()
    #print dataFrame5
    for i in range(10):
        calculateNewCentroids()
        calculateCosineSimilarity()
        updateCentroidData()
        generateClusters()
        #print dataFrame5
        if convergenceCase():
            break
        else:
            print "Not converged"
            #print centroidCosineSimilarity
            previousClusters = list(clusters)
    
    print "Converged in ", i , " iteration(s)"   


skMeansClustering()
print clusters