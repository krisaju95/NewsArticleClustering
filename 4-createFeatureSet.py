import pickle
import os


path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
dataFrame2 = pickle.load( open(os.path.join(path, 'Feature Set','dataFrame2.p'), "rb" ))
wordSetSize = len(dataFrame2.columns)
numberOfDocuments = len(dataFrame2.index)
TfIdf_Threshold = 0.0035


# Creates a dataframe containing features in each document as document vectors (each row is a vector)
def generateFeatureSet():
    dataFrame3=dataFrame2.copy()
    
    print "Generating documents vectors"
    print "TF-IDF threshold value set at ",TfIdf_Threshold
    
    for row in dataFrame3.index:
        for word in dataFrame3.columns:
             if dataFrame3.ix[row,word] < TfIdf_Threshold:
             #    dataFrame3.ix[row,word] = 1
             #else:
                 dataFrame3.ix[row,word] = 0.0  
    
    print "Document Vectors generated"
    print "Performing Dimensionality Reduction at threshold value"
    
    notFeatures = []             
    for column in dataFrame3.columns:
        flag = 0
        for row in dataFrame3.index:
            if dataFrame3.ix[row , column] != 0.0:
                flag = 1
                break;
        if flag == 0:
            notFeatures.append(column)
                 
    for word in notFeatures:
        del dataFrame3[word]
    
    print "Document Vectors saved in DataFrame3"
    print "Saving data in DataFrame3 as a pickle package and as a CSV"
                                                                        
    dataFrame3.to_pickle(os.path.join(path, 'Feature Set','dataFrame3.p'))
    dataFrame3.to_csv(os.path.join(path, 'Feature Set','dataFrame3.csv'))
    
    print "DataFrame3 has been saved"    
    
    
generateFeatureSet()