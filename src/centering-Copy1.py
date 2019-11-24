#!/usr/bin/env python
# coding: utf-8

# In[106]:


import nltk
import string
from nltk import pos_tag
import spacy
import numpy as np
from nltk import grammar, parse
from collections import Counter 


# In[82]:


nlp = spacy.load("en")


# In[117]:


filename = '../data/test1.txt'
f = open(filename, "r")
contents = f.read()
print(contents)

print("\n")
utterances = []
split_utterances = []
sentences = contents.strip().split('.')
for sentence in sentences:
    if sentence != '':
        utterances.append(sentence.strip())

print(utterances)


# In[118]:


## pos tags
pos_tags_utterances = []

for utterance in utterances:
    print(utterance)
    pos_tags_utterances.append(pos_tag(utterance.split(' ')))
    
print(pos_tags_utterances)


# In[119]:


processed_utterance = nlp(utterances[0])
init_topic = ''
print()
for chunk in processed_utterance.noun_chunks:
    if chunk.root.dep_ == "nsubj":
        init_topic = chunk.text
    print(chunk.text,",",chunk.root.text, ",",chunk.root.dep_,",",chunk.root.head.text)


# In[120]:


total_utterances = len(utterances)

Cb = [None] * total_utterances

Cf = []
for i in range(total_utterances):
    Cf.append([])

Cb[0] = "undefined"
for i in range(total_utterances):
    
    for token in pos_tags_utterances[i]:
        if "NN" in token[1]:
            Cf[i].append((token[0].lower(), token[1]))
        if i!=0:
            if "PRP" == token[1]:
                if token[0].lower() == "he" or token[0].lower() == "she":
                    for pos in Cf[i-1]:
                        if pos[1] == "NNP":
                            if (pos[0].lower(), "NNP") not in Cf[i]:
                                Cf[i].append((pos[0].lower(), "NNP"))
                                break
                elif token[0].lower() == "it":
                    for pos in Cf[i-1]:
                        if pos[1] == "NN":
                            if (pos[0].lower(), "NN") not in Cf[i]:
                                Cf[i].append((pos[0].lower(), "NN"))
                                break

    if i != 0:
        Cb[i] = Cf[i][0]

        
print("Centers")        
print(Cb)


# In[121]:


topics_utterances = []
focus_utterances = []
topics_utterances.append(init_topic)
for tuple_val in Cb:
    if tuple_val != "undefined":
        if tuple_val[1] == "NNP":
            topics_utterances.append(tuple_val[0].capitalize())
        else:
            topics_utterances.append(tuple_val[0])

print(topics_utterances)


# In[125]:


topic_dict = {}
for topic in topics_utterances:
    if topic not in topic_dict.keys():
        topic_dict[topic] = 1
    else:
        topic_dict[topic] += 1
        
k  = Counter(topic_dict)
top_topics_num = len(topic_dict)/2
top_topics_list = k.most_common(2)


print("Topics present in the discourse are:\n")
for topic in top_topics_list:
    print(topic[0])


# In[ ]:




