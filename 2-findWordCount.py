import numpy as np
import glob
import os
import pandas as pd
import string

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
wordSetSize = 0
numberOfDocuments = 0


# Calculates the number of words in the word set
def findSetSize():
    wordSetFile = open(os.path.join(path, 'Word Set','wordSet.txt'), 'r')
    for line in wordSetFile:
        for word in line.split():
            words.add(word)
            #print word
    
    setSize=len(words)
    return setSize


# Finds the number of documents present in path
def findNumberOfDocuments():
    numberOfDocuments = 0
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        numberOfDocuments = numberOfDocuments + 1
    return numberOfDocuments

# Calculates the count of each word from word set found in each document in path
def findWordCounts():
    dataFrame1=pd.DataFrame(np.zeros(numberOfDocuments).reshape(numberOfDocuments,1))
    fileID = 0

    # Initialise all values as zero
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        for word in words:
            dataFrame1.ix[fileID,word]=0
        fileID = fileID + 1
    
    fileID = 0
    
    # Calculate term frequency for all words in each document
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        f=open(filename, 'r')
        for line in f:
            for word in line.split():
                word = word.strip(string.punctuation)
                word = word.lower()
                if word.isalpha():
                    if word in words:
                        dataFrame1.ix[fileID,word] = dataFrame1.ix[fileID,word] + 1
        fileID = fileID + 1
    
    # Delete default column from DataFrame initialisation
    del dataFrame1[0]
          
    #print dataFrame1
    
    # Pickle dataFrame for exporting
    dataFrame1.to_pickle(os.path.join(path, 'Word Count','dataFrame1.p'))
    #print dataFrame1 #.ix[1,"richard"]
                        
wordSetSize=findSetSize()
numberOfDocuments=findNumberOfDocuments()
findWordCounts()
#print words
