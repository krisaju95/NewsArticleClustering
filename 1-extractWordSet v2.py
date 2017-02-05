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

def isOnlyStr(str):
    for char in str:
        if not char.isalpha():
            return False
            break
    return True
    
                        
def preprocess(sent , filename):
        f = open(os.path.join(path, 'Word Set','wordSet.txt'), 'a')
        f1 = open(filename, 'w')
	sent = sent.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sent)
	filtered_words = [w for w in tokens if not w in sw]
	for w in filtered_words:
	    if len(w) >= 3 and isOnlyStr(w):
	       f.write(w + '\n')
	       f1.write(w + '\n')
	f.close()


# Creates a text file containing all the words in the python Word set
def createWordSet():
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

createWordSet()