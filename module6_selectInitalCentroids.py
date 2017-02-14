import pickle
import numpy as np
import pandas as pd
import os


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
D = set()
A = [[0, 61, 70, 87, 100, 115, 128, 151, 162, 168],
    [1, 2, 20, 42, 96, 129, 130, 173, 174, 197],
    [46, 48, 53, 64, 93, 95, 105, 124, 159, 171],
    [57, 60, 73, 83, 89, 117, 120, 146, 150, 175],
    [31, 34, 39, 80, 98, 116, 131, 140, 191, 195]]
#A = []
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
dataFrame3 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame3.p'), "rb" ))
cosineSimilarityMatrix = pickle.load( open(os.path.join(path, 'KMeansClustering','dataFrame4.p'), "rb" ))
wordSetSize = len(dataFrame3.columns)
numberOfDocuments = len(dataFrame3.index)
m = 1
k = 5
centroids = pd.DataFrame(np.zeros(k).reshape(k,1))

# Find a pair of points having maximum cosine similarity
def findMostSimilarPoints():
    global D
    mostSimilarValue = 0
    mostSimilarPoints = []
    for document in D:
        for column in cosineSimilarityMatrix.columns:
            if document != column:
                if cosineSimilarityMatrix.ix[document , column] > mostSimilarValue:
                    mostSimilarValue = cosineSimilarityMatrix.ix[document , column]
                    mostSimilarPoints = [column, document]
    
    return mostSimilarPoints
    

# Find a single point in D which is closest to the set of points in Am
def findNextClosestPoints(A):
    mostSimilarValue = 0
    mostSimilarPoint = 0
    for document in A:
        for column in cosineSimilarityMatrix.columns:
            if column in D:
                if cosineSimilarityMatrix.ix[document , column] >= mostSimilarValue:
                    mostSimilarValue = cosineSimilarityMatrix.ix[document , column]
                    mostSimilarPoint = column
                    
    return mostSimilarPoint
    
# Initialize set D with all documents   
def initializeSetD():
    for column in cosineSimilarityMatrix.columns:
        D.add(column)

# Initialize set A with k empty lists, each empty list within A represents the initial state of a cluster
def initalizeSetAm():
    for i in range(k):
        A.append([])        
# Given a list of points P, append the set of points to Am
def addToSetA(i, P):
    for point in P:
        A[i].append(point)                        

# Initialize a dataframe containing the centroid vectors with zero values
def initializeCentroids():
    for row in centroids.index:
        for word in dataFrame3.columns:
            centroids.ix[row , word] = 0
    del centroids[0]
                                                                        
# Find the average vector for each cluster Am and assign that as a centroid for that cluster                                                                                                                                                                                                        
def computeCentroidsForEachSetA():
    sizeOfAm = 0
    for m in range(k):
        sizeOfAm = len(A[m])
        for point in A[m]:
            for word in centroids.columns:
                centroids.ix[m , word] = centroids.ix[m , word] + dataFrame3.ix[point, word]
        for word in centroids.columns:
            centroids.ix[m , word] = centroids.ix[m , word] / sizeOfAm
                                                                                                                                                                                                                                           
# Main function for selecting inital centroids for the K Means Clustering algorithm
def selectInitialCentroids():
    firstPoints = []
    nextClosestPoint = 0
    pointListForm = []
    pointSetForm = set()
    global m
    initalizeSetAm()
    initializeSetD()
    initializeCentroids()
    m = 0
    
    print "Computing Inital Centroids"
    for m in range(k):
        
        print "Generating Cluster ", m + 1 , " of " , k
        
        firstPoints = findMostSimilarPoints()
        addToSetA(m , firstPoints)
        D.difference_update(set(firstPoints))
        while len(A[m]) < (0.75 * numberOfDocuments / k):
            nextClosestPoint = findNextClosestPoints(A[m])
            pointListForm.append(nextClosestPoint)
            addToSetA(m , pointListForm)
            pointSetForm.add(nextClosestPoint)
            D.difference_update(pointSetForm)
            pointListForm = []
            pointSetForm = set()
            #print nextClosestPoint
            #print D
    
         
#selectInitialCentroids()
#initalizeSetAm()
#initializeSetD()
initializeCentroids()
computeCentroidsForEachSetA()
centroids.to_pickle(os.path.join(path, 'KMeansClustering','initialCentroids.p'))
