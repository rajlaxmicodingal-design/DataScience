import pandas as pd
import numpy as np
import nltk
import re
import random

nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from termcolor import colored

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load data
df = pd.read_csv("D:/Codingal/Data Science/M23/Lesson 6Text Summarizer/tennis.csv")

# Random article selection
i = random.randint(0, len(df))
print("Selected article text:")
print(df['article_text'][i])
print("\n" + "="*80 + "\n")

# Tokenize into sentences
sentences = []
for s in df['article_text']:
    sentences.append(sent_tokenize(s))
sentences = [y for x in sentences for y in x]

# Load GloVe embeddings
word_embeddings = {}
f = open('glove.6B.300d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

# Clean sentences
clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
clean_sentences = [s.lower() for s in clean_sentences]

# Remove stopwords
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

# Create sentence vectors
sentence_vectors = []
for i in clean_sentences:
    if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((300,))) for w in i.split()])/(len(i.split())+0.001)
    else:
        v = np.zeros((300,))
    sentence_vectors.append(v)

# Create similarity matrix
sim_mat = np.zeros([len(sentences), len(sentences)])
for i in range(len(sentences)):
    for j in range(len(sentences)):
        if i != j:
            sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,300), 
                                            sentence_vectors[j].reshape(1,300))[0,0]

# Apply PageRank algorithm
nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

# Rank sentences
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

# Display results
print(colored("ARTICLE:".center(80), 'yellow'))
print('\n')
print(colored(df['article_text'][i], 'blue'))
print('\n')
print(colored("SUMMARY:".center(80), 'green'))
print('\n')
print(colored(ranked_sentences[0][1], 'cyan'))  # Display top-ranked sentence as summary