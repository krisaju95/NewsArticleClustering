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
    print "Initializing DataFrame conataining Term Frequency for each document"
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        for word in words:
            dataFrame1.ix[fileID,word]=0
        fileID = fileID + 1
    
    print "Document Term Frequency DataFrame Initialised"
    fileID = 0
    
    print "Calculating Term Frequency for each document"
    
    # Calculate term frequency for all words in each document
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        print "Processing Document ",fileID + 1," of ",numberOfDocuments
        f=open(filename, 'r')
        for line in f:
            for word in line.split():
                word = word.strip(string.punctuation)
                word = word.lower()
                if word in words:
                        dataFrame1.ix[fileID,word] = dataFrame1.ix[fileID,word] + 1
        fileID = fileID + 1
    
    print "Document Term Frequencies calculation completed"
    
    # Delete default column from DataFrame initialisation
    del dataFrame1[0]
          
    #print dataFrame1
    
    print "Saving data in dataFrame1 as pickle package and CSV"
    
    # Pickle dataFrame for exporting
    dataFrame1.to_pickle(os.path.join(path, 'Word Count','dataFrame1.p'))
    
    # Save dataframe as CSV for user
    dataFrame1.to_csv(os.path.join(path, 'Word Count','dataFrame1.csv'))
    
    print "Dataframe1 has been saved"
                        
                                                                
wordSetSize=findSetSize()
numberOfDocuments=findNumberOfDocuments()
findWordCounts()
#print words
print len(words)
