import glob
import os
from nltk.corpus import stopwords
import string
import nltk, re, pprint
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

path = ""
words = set()
wordSet = set()

path = "C:/Users/hp/Desktop/FINAL YEAR PROJECT/S8/"
count = 0
sw = set()
sw = stopwords.words('english')


# Checks if a given word comprises only of alphabets
def isOnlyStr(str):
    for char in str:
        if not char.isalpha():
            return False
            break
    return True
    

# Converts all words to lower-case and filters out words that contain numbers and symbols                                                
def preprocess(sent , filename):
        f = open(os.path.join(path, 'Word Set','wordSet.txt'), 'a')
        f1 = open(filename, 'w')
	sent = sent.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sent)
	filtered_words = [w for w in tokens if not w in sw]
	for w in filtered_words:
	    if isOnlyStr(w):
	       f.write(w + '\n')
	       f1.write(w + '\n')
	f.close()


# Creates a text file containing all the words in the python Word set
def createWordSet():
    print "Generating WordSet containing unique words"
    
    if os.path.exists(os.path.join(path, 'Word Set','wordSet.txt')):
            os.remove(os.path.join(path, 'Word Set','wordSet.txt'))
            
    for filename in glob.glob(os.path.join(path , 'News Articles' , '*.txt')):
        f=open(filename, 'r')
        op=open(os.path.join(path, 'temp.txt'),'w')
        for line in f:            
            line=line.strip().decode("ascii","ignore").encode("ascii")
            if line=="":
                continue
            op.write(line + ' ')
        op.close()        
            
        fo = open(os.path.join(path, 'temp.txt'), "r")
        for sent in fo:
            preprocess(sent, filename)
        fo.close()
    
    print "WordSet has been Generated"    
    
#createWordSet()