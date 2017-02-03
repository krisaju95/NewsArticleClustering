import glob
import os
from nltk.corpus import stopwords
import string

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
words = set()
wordSet = set()

# Creates a Python Set containing all the words found in the documents in path including stop words
def createWordSet():
    for filename in glob.glob(os.path.join(path, 'News Articles','*.txt')):
        f=open(filename, 'r')
        for line in f:
                for word in line.split():
                    # Pre-processing
                    word = word.strip(string.punctuation)
                    word = word.lower()
                    if word.isalpha():
                        words.add(word)
                        #print word

                    

# Removes a small set of stop words from the initial word set using nltk's stop word corpus
def removeInitialStopWords():
    stop = set(stopwords.words('english'))
    wordSet=words.copy()
    for element in words:
        if element.lower() in stop:
            wordSet.discard(element)
    return wordSet

# Creates a text file containing all the words in the python Word set
def generateWordSetFile():
    wordSetFile = open(os.path.join(path, 'Word Set','wordSet.txt'), 'w')
    for word in wordSet:
        wordSetFile.write(word)
        wordSetFile.write('\n')

createWordSet()
wordSet=removeInitialStopWords()
generateWordSetFile()
#print wordSet