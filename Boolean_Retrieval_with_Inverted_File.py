
import os
import re
import numpy as np
path = r"/content/data/"
files = os.listdir(path)
dictionary = set()
list_str=[]
for file in files:
  f= open(path+file,"r",encoding="utf8")
  content_file = f.read()
  content_file=re.sub("\,|\.|\-|\'|\"|\_|\+|\?|\!|\@|\#|\$|\%|\;|\[|\]|\/|\:|\)|\(","",content_file)
  content_file=content_file.lower()
  content_file = content_file.split()
  list_str.append(content_file) 
  dictionary.update(content_file)

query = "Fernandes and Greenwood"
query=re.sub("\,|\.|\-|\'|\"|\_|\+|\?|\!|\@|\#|\$|\%|\;|\[|\]|\/|\:|\)|\(","",query)
query=query.split()
terms = []
operand_logic = []
for i in range(len(query)):
	if i%2==1:
		operand_logic.append(query[i].lower())
	else:
		terms.append(query[i])
inverted_index = {}
for i in range (len(list_str)):
    for word in list_str[i]:
        if inverted_index.get(word, None) is None:
            inverted_index[word] = {files[i]}
        else:
            inverted_index[word].add(files[i])
posting=[]
for token in terms:
    if token in dictionary:
        posting.append(list(inverted_index.get(token)))
    else:
        posting.append("0")
def or_(a,b):
    for i in a:
        if i not in b:
            b.append(i)
    return b
def xor_(a,b):
    c=[]
    for i in a:
        if i not in b:
            c.append(i)
    for j in b:
        if j not in a:
            c.append(j)
    return c
print(posting)
for j in range(len(operand_logic)):
        if len(posting)>1:
            if operand_logic[j]=='and':
                posting.append(list(set(posting[0]) & set(posting[1])))
            elif operand_logic[j]=='or':
                posting.append(list(or_(posting[0],posting[1])))
            elif operand_logic[j]=='xor':
                posting.append(list(xor_(posting[0],posting[1])))   
        # print(posting)
            posting.remove(posting[0])
            posting.remove(posting[0])

print("Danh sach các file văn bản thỏa mãn query: ") 
if "0" in posting[0]:
    posting[0] = ''
print(posting[0])
