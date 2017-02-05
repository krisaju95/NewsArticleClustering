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
wordSetSize = len(dataFrame3.columns)
numberOfDocuments = len(dataFrame3.index)
m = 1
k = 4
centroids = pd.DataFrame(np.zeros(k).reshape(k,1))

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
    

def findNextClosestPoints(A):
    mostSimilarValue = 0
    mostSimilarPoint = 0
    for document in A:
        for column in cosineSimilarityMatrix.columns:
            if column in D:
                if cosineSimilarityMatrix.ix[document , column] > mostSimilarValue:
                    mostSimilarValue = cosineSimilarityMatrix.ix[document , column]
                    mostSimilarPoint = column
                    
    return mostSimilarPoint
    
    
def initializeSetD():
    for column in cosineSimilarityMatrix.columns:
        D.add(column)

def initalizeSetAm():
    for i in range(k):
        A.append([])        

def addToSetA(i, P):
    for point in P:
        A[i].append(point)                        


def initializeCentroids():
    for row in centroids.index:
        for word in dataFrame3.columns:
            centroids.ix[row , word] = 0
    del centroids[0]
                                                                        
                                                                                                                                                                                                        
def computeCentroidsForEachSetA():
    sizeOfAm = 0
    for m in range(k):
        sizeOfAm = len(A[m])
        for point in A[m]:
            for word in centroids.columns:
                centroids.ix[m , word] = centroids.ix[m , word] + dataFrame3.ix[point, word]
        for word in centroids.columns:
            centroids.ix[m , word] = centroids.ix[m , word] / sizeOfAm
                                                                                                                                                                                                                                           

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
    for m in range(k):
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
    
         
selectInitialCentroids()
computeCentroidsForEachSetA()
centroids.to_pickle(os.path.join(path, 'KMeansClustering','initialCentroids.p'))