import pickle
import numpy as np
import pandas as pd
import os


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
D = set()
A = []
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
cosineSimilarityMatrix = pickle.load( open(os.path.join(path, 'KMeansClustering','dataFrame4.p'), "rb" ))
classifiedDocuments = pd.read_csv(os.path.join(path, 'KMeansClustering','classifiedDocuments.csv'))
wordSetSize = len(dataFrame3.columns)
numberOfDocuments = len(dataFrame3.index)
m = 1
k = 5
sampleSize = 3
centroids = pd.DataFrame(np.zeros(shape = (k , wordSetSize)).reshape(k , wordSetSize))

# Initialize set A with k empty lists, each empty list within A represents the initial state of a cluster
def initalizeSetAm():
    for i in range(k):
        A.append([])   
             
# Given a list of points P, append the set of points to Am
def addToSetA(i, P):
    A[i].append(P)                        

# Initialize a dataframe containing the centroid vectors with zero values
def initializeCentroids():
    global centroids
    centroids.columns = dataFrame3.columns

                                                                                                                                            
def findBestSamples():
    clusterID = 0
    for row in classifiedDocuments.index:
        clusterID = classifiedDocuments.ix[row , "actualClass"]
        addToSetA(int(clusterID - 1), row)
    
    dataFrame3Matrix = dataFrame3.as_matrix()
    minFeaturePoint = 0
    minFeatureWeight = wordSetSize        
    for i in range(k):
        while len(A[i]) > sampleSize:
            minFeaturePoint = 0
            minFeatureWeight = wordSetSize 
            for point in A[i]:
                
                if np.sum(dataFrame3Matrix[point , :]) < minFeatureWeight:
                    minFeatureWeight = np.sum(dataFrame3Matrix[point , :])
                    minFeaturePoint = point
            A[i].remove(minFeaturePoint)
                                                                                                                                            
# Find the average vector for each cluster Am and assign that as a centroid for that cluster                                                                                                                                                                                                        
def computeCentroidsForEachSetA():
    global centroids
    sizeOfAm = 0
    dataFrame3Matrix = dataFrame3.as_matrix()
    centroidsMatrix = centroids.as_matrix()
    for m in range(k):
        sizeOfAm = len(A[m])
        for point in A[m]:
            centroidsMatrix[m] = np.add(centroidsMatrix[m] , dataFrame3Matrix[point])
        centroidsMatrix[m] = np.divide(centroidsMatrix[m] , float(sizeOfAm))
    centroids = pd.DataFrame(centroidsMatrix)
    initializeCentroids()
                                                                                                                                                                                                                                        

initalizeSetAm()
findBestSamples()
initializeCentroids()
computeCentroidsForEachSetA()
centroids.to_pickle(os.path.join(path, 'KMeansClustering','initialCentroids.p'))
centroids.to_csv(os.path.join(path, 'KMeansClustering','initialCentroids.csv'))