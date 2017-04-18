import glob
import os
from nltk.corpus import stopwords
import string
import nltk, re, pprint
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from itertools import groupby
import sys
import string
from nltk.tokenize import TweetTokenizer
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import pickle


tknzr = TweetTokenizer()
lmtzr = WordNetLemmatizer()

punct = list(string.punctuation)

#Stanford NER initialization
stanford_classifier = 'F:\stanford-ner-2016-10-31\classifiers\english.all.3class.distsim.crf.ser.gz'
stanford_ner_path = 'F:\stanford-ner-2016-10-31\stanford-ner.jar'

st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')


path = ""
words = set()
wordSet = set()

path = "C:\Users\hp\Desktop\FINAL YEAR PROJECT\S8"
count = 1
sw = set()
sw = stopwords.words('english')

def has_all_lowercase_letter(word):
    for letter in word:
        if letter.isupper():
            return 0
            break
    return 1

def meaningful_word(word):
    if has_all_lowercase_letter(word) and len(word)<4:
        return 0
    return 1
     

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag in ('NNS','NN'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return 0

def onlyalpha(s):
    return not(any(i.isdigit() for i in s))

def strip_nonascii(tokenized):
    # print tokenized
     a= []
     ff=open(os.path.join(path, 'temp1.txt'),'a')
     for word in tokenized:
        for i in range(0, len(word)):
            try:
                word[i].encode("ascii")
            except UnicodeDecodeError:
                if i==0:
                    word=word.replace(word[i]," ")
                elif ((i-1)>=0) and ((i+1)< len(word)):
                    if word[i-1].isalpha() and word[i+1].isalpha():
                        word=word.replace(word[i],"'")
                    else:
                        word=word.replace(word[i]," ")
                else:
                    word=word.replace(word[i]," ") 
      
        a = word.split()
        for w in a:
            ff.write(w + ' ')
            #print w
     ff.close()

# Creates a text file containing all the words in the python Word set
def createWordSet():
    print "Generating WordSet containing unique words"
    
    if os.path.exists(os.path.join(path, 'Word Set','wordSet.txt')):
            os.remove(os.path.join(path, 'Word Set','wordSet.txt'))
    
    fileID = 1         
    for filename in glob.glob(os.path.join(path , 'News Articles' , '*.txt')):
        f=open(filename, 'r')
        print 'Preprocessing file ', fileID
        fileID = fileID + 1
        #op=open(os.path.join(path, 'temp.txt'),'w')
        for line in f:
            try:
                tokenized = word_tokenize(line)
                strip_nonascii(tokenized)
            except UnicodeDecodeError:
                line=line.strip().decode("ascii","ignore").encode("ascii")
                tokenized = word_tokenize(line)
                strip_nonascii(tokenized)
                
                
        ascii_f=open(os.path.join(path, 'temp1.txt'),'r')
        
 
#lemmatization code starts here..
        lem_f=open(os.path.join(path, 'temp3.txt'),'w')
        for sent in ascii_f:
            tokens = tknzr.tokenize(sent) 
            #print tokens               
            tagged = nltk.pos_tag(tokens)
            #print tagged
            for x,y in tagged:
                tag = get_wordnet_pos(y)
                if tag != 0:
                    lem_f.write(lmtzr.lemmatize(x,tag)+ ' ')
                else:
                    lem_f.write(x + ' ')               
        lem_f.close()

#lemmatization code ends here....        
                        
        ip=open(os.path.join(path, 'temp3.txt'),'r')
        op=open(os.path.join(path, 'temp2.txt'),'w')
        #sys.stdout = ff
        for sent in ip:
           # tokenized_text = word_tokenize(sent)
            tokenized_text = tknzr.tokenize(sent)
            pos = -1
            for token in tokenized_text:
                pos = pos + 1
                length = len(token)
                if ((length-1) >= 0):
                    if token[length-1]=='s' and token[length-2]=="'":
                        tokenized_text[pos] = token[:length-2]
            classified_text = st.tag(tokenized_text)
            for tag,word in groupby(classified_text, lambda x:x[1]):
                a = []
                if tag != "O":
                    op.write(" ".join(w for w, t in word))
                    op.write('\n')
                else:
                    op.write(("\n".join(w for w, t in word)).lower())
                    op.write('\n')
        op.close()
        ip.close()
        f=open(filename, 'w')
        fp = open(os.path.join(path, 'temp2.txt'),'r')
        for line in fp:
            line = line.rstrip('\n')
            
            if (line not in sw) and (onlyalpha(line)) and (line not in punct) and (meaningful_word(line)):
                f.write(line)
                f.write('\n')
                wordSet.add(line)
        f.close()
        fp.close()
        fpo = open(os.path.join(path, 'temp1.txt'),'w')
        fpo.close()
        fp1 = open(os.path.join(path, 'temp2.txt'),'w')
        fp1.close() 

    #print "WordSet has been Generated"    
    
createWordSet()
pickle.dump(wordSet , open(os.path.join(path, 'Word Set','wordSet.p'), 'wb'))