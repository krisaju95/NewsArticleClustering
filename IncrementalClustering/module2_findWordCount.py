import numpy as np
import glob
import os
import pandas as pd
import string
import pickle

newsPaperName = "NewsPaper A"
path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = pickle.load(open(os.path.join(path, 'Word Set','wordSet.p'), 'rb'))
wordSetSize = 0
numberOfDocuments = 0
wordCount = {}

# Calculates the number of words in the word set
def findSetSize():
    setSize=len(words)
    return setSize

# Resets word counts to 0 in the dictionary
def initializeWordCountDictionary():
    for word in words:
        wordCount[word] = 0

# Finds the number of documents present in path
def findNumberOfDocuments():
    numberOfDocuments = 0
    for filename in glob.glob(os.path.join(path , 'Crawled Articles' , newsPaperName , '*.txt')):
        numberOfDocuments = numberOfDocuments + 1
    return numberOfDocuments

# Calculates the count of each word from word set found in each document in path
def findWordCounts():
    dataFrame1=pd.DataFrame(np.zeros(shape = (numberOfDocuments , wordSetSize)).reshape(numberOfDocuments , wordSetSize))
    fileID = 0
    dataFrame1.columns = list(words)

    print "Document Term Frequency DataFrame Initialised"
    #fileID = 0
    
    print "Calculating Term Frequency for each document"
    
    # Calculate term frequency for all words in each document
    for filename in glob.glob(os.path.join(path , 'Crawled Articles' , newsPaperName ,'*.txt')):
        print "Processing Document ",fileID + 1," of ",numberOfDocuments, " from ", newsPaperName
        f=open(filename, 'r')
        for line in f:
            #for word in line.split():
                line = line.rstrip('\n')
                if line in words:
                    dataFrame1.ix[fileID,line] = dataFrame1.ix[fileID,line] + 1
        fileID = fileID + 1
    
    print "Document Term Frequencies calculation completed"
    
    # Delete default column from DataFrame initialisation
    #del dataFrame1[0]
          
    #print dataFrame1
    
    print "Saving data in dataFrame1 as pickle package and CSV"
    
    # Pickle dataFrame for exporting
    dataFrame1.to_pickle(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Word Count','dataFrame1.p'))
    
    # Save dataframe as CSV for user
    dataFrame1.to_csv(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Word Count','dataFrame1.csv'))
    
    print "Dataframe1 has been saved"
                        
                                                                
wordSetSize=findSetSize()
numberOfDocuments=findNumberOfDocuments()
findWordCounts()
#print words
#print len(words)