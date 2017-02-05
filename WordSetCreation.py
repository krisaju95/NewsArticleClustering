import glob
import os
from nltk.corpus import stopwords
import string
import nltk, re, pprint
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


path = "C:\Users\Akshay-PC\Desktop\Articles"
count = 0
sw = set()
sw = stopwords.words('english')

def isOnlyStr(str):
    for char in str:
        if not char.isalpha():
            return False
            break
    return True

# Creates a Python Set containing all the words found in the documents in path excluding stop words
        
def preprocess(sent):
        f = open("C:\Users\Akshay-PC\Desktop\\Wordset.txt", "a")
	sent = sent.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sent)
	filtered_words = [w for w in tokens if not w in sw]
	for w in filtered_words:
	    if len(w) >= 3 and isOnlyStr(w):
	       f.write(w + '\n')
	f.close()
	
def createWordSet():
    for filename in glob.glob(os.path.join(path, '*.txt')):
        f=open(filename, 'r')
        op=open("C:\Users\Akshay-PC\Desktop\\temp.txt",'w')
        for line in f:            
            line=line.strip().decode("ascii","ignore").encode("ascii")
            if line=="":
                continue
            op.write(line + ' ')
        op.close()

        fo = open("C:\Users\Akshay-PC\Desktop\\temp.txt", "r")
        for sent in fo:
            preprocess(sent)
        fo.close()
        

createWordSet()
