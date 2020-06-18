import numpy as np
import pandas as pd
import nltk
import random
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,sent_tokenize
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
lemmatizer = WordNetLemmatizer()
#do not touch

f = open('testing.txt','r',encoding='utf-8')
text = f.read()
sent_tokens = nltk.sent_tokenize(text)
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

def get_lemmatization(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

GREETINGS = ["hi","hello","how are you"]
GREETING_RESPONSES = ["hi","hello","how are you"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETINGS:
            return random.choice(GREETING_RESPONSES)


def get_response(user_response):

    
    user_response =user_response.lower()

    chatbot_response =''

    sent_tokens.append(user_response)
    #tfidf
    TfidfVec = TfidfVectorizer(tokenizer=get_lemmatization) #could've done this with gensim word2vec
    tfidf = TfidfVec.fit_transform(sent_tokens)

    #get similarity
    vals = cosine_similarity(tfidf[-1],tfidf)#last index, compares to all of them
    

    #get index most similar text/sentence
    idx = vals.argsort()[0][-2]#double array, msot similar is at very end but since we append
    #we choose second last
    #Returns the indices that would sort an array.

    x = vals.flatten()#gets only 1d array
    x.sort()

    score = x[-2]
  
    #if score is 0 has nothing similar
    if score == 0:
        chatbot_response += "I don't understand"
    else:
        chatbot_response += sent_tokens[idx]

    sent_tokens.remove(user_response)

  

    return chatbot_response

