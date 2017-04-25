import pickle
import math
import os
import pandas as pd
import numpy as np

newsPaperName = "NewsPaper A"
path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = pickle.load(open(os.path.join(path, 'Word Set','wordSet.p'), 'rb'))
dataFrame1 = pickle.load( open(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Word Count','dataFrame1.p'), "rb" ))
wordSetSize = len(dataFrame1.columns)
numberOfDocuments = len(dataFrame1.index)
oldDataFrame2 = pickle.load(open(os.path.join(path, 'Feature Set', 'dataFrame2.p'), "rb" ))
originalNumberOfDocuments = len(oldDataFrame2.index)


# Calculates Tf-Idf score for each word using data from the data frame
def calculateTfIdf():
    dataFrame2=dataFrame1.copy()
    dataFrame2Matrix = dataFrame2.as_matrix()
    oldDataFrame2Matrix = oldDataFrame2.as_matrix()
    print "Normalising Term Frequencies"
    # Normalises Term Frequency , Calculates total number of terms in each document and Divides term frequency by document term count (normalising)
    for row in dataFrame2.index:
        fileWordCount = dataFrame2Matrix[row].sum()
        dataFrame2Matrix[row] = np.divide(dataFrame2Matrix[row] , float(fileWordCount))
    dataFrame2 = pd.DataFrame(dataFrame2Matrix)
    
    print "Normalisation completed"
    
    print "Calculating IDF and corresponding TF-IDF values"
    
    # Calculates document frequency for each word and multiply with TF component
    for word in range(len(dataFrame2.columns)):
        wordDocumentCount = 0
        idfValue = 0
        wordDocumentCount = np.count_nonzero(oldDataFrame2Matrix[:,word])
        if wordDocumentCount != 0:
            idfValue = math.log(originalNumberOfDocuments / (wordDocumentCount + 1))
        dataFrame2Matrix[:,word] = np.multiply(dataFrame2Matrix[:,word] , idfValue)

    dataFrame2 = pd.DataFrame(dataFrame2Matrix)
    dataFrame2.columns = list(words)
    
    print "TF-IDF Calculation completed"
    
    print "Saving data in dataFrame2 as pickle package and CSV"
    
    dataFrame2.to_pickle(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Feature Set','dataFrame2.p'))
    dataFrame2.to_csv(os.path.join(path , 'Crawled Articles' , newsPaperName , 'Feature Set','dataFrame2.csv'))
    
    print "Dataframe2 has been saved"

calculateTfIdf()
