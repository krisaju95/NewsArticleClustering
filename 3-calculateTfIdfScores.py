import pickle
import math
import os

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame1 = pickle.load( open(os.path.join(path, 'Word Count','dataFrame1.p'), "rb" ))
wordSetSize = len(dataFrame1.columns)
numberOfDocuments = len(dataFrame1.index)


# Calculates Tf-Idf score for each word using data from the data frame
def calculateTfIdf():
    dataFrame2=dataFrame1.copy()
    
    # Normalises Term Frequency
    for row in dataFrame2.index:
        fileWordCount = 0
        
        # Calculates total number of terms in each document
        for word in dataFrame2.columns:
            fileWordCount = fileWordCount + dataFrame2.ix[row,word]
            
        # Divides term frequency by document term count (normalising)
        for word in dataFrame2.columns:
            if dataFrame2.ix[row,word] != 0:
                dataFrame2.ix[row,word] = dataFrame2.ix[row,word] / fileWordCount
    
    # Calculates document frequency for each word and multiply with TF component
    for word in dataFrame2.columns:
        wordDocumentCount = 0
        for row in dataFrame2.index:
            if dataFrame2.ix[row,word] != 0:
                wordDocumentCount = wordDocumentCount +1
        if wordDocumentCount != 0:
            dataFrame2.ix[row,word] = dataFrame2.ix[row,word] * math.log(numberOfDocuments / wordDocumentCount)

        else:
            dataFrame2.ix[row,word] = 0.0    
    '''
    # Completes  Tf-Idf calculation by dividing with total document count  
    for word in dataFrame2.columns:
        for row in dataFrame2.index:
            dataFrame2.ix[row,word] = dataFrame2.ix[row,word] / numberOfDocuments
    '''
    
    dataFrame2.to_pickle(os.path.join(path, 'Feature Set','dataFrame2.p'))
    #print dataFrame2

calculateTfIdf()