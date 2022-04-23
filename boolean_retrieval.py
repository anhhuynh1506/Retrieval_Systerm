# Bước 1:  đọc tất cả các file văn bản để lấy danh sách
import os
import re
import numpy as np
path = r"C:/Users/Admin/Desktop/Boolean Retrieval/data/"
files = os.listdir(path)
dictionary = set()
list_str=[]
for file in files:
	f= open(path+file,"r",encoding="utf8")
	content_file = f.read()
	content_file=(re.sub("\,|\.|\-|\'|\"|\_|\+|\?|\!|\@|\#|\$|\%|\;|\[|\]|\/|\:|\)|\(","",content_file))
	content_file=content_file.lower()
	content_file = set(content_file.split())
	list_str.append(content_file) 
	dictionary.update(content_file)
# print(dictionary)
# Bước 2: Xây dựng ma trận term document
init_matric_term = np.zeros((len(dictionary),len(list_str)))
index =0
for string in list_str:
	init_matric_term[:,index] = np.array(([int(word in string) for word in dictionary]))
	index+=1
# Bước 3: Phân tích query
query = 'Goal'
query=re.sub("\,|\.|\-|\'|\"|\_|\+|\?|\!|\@|\#|\$|\%|\;|\[|\]|\/|\:|\)|\(","",query)
query=query.split()
terms = []
operand_logic = []
for i in range(len(query)):
	if i%2==1:
		operand_logic.append(query[i].lower())
	else:
		terms.append(query[i].lower())	
print(terms)
# tokens = re.findall('"(\w+)"',query)
dictionary = list(dictionary)
arr = []
for token in terms:
	if token in dictionary:
		ind = dictionary.index(token)
		vector = init_matric_term[ind]
		arr.append(vector)
	else:
		vector = np.zeros(len(list_str))
		arr.append(vector)
print(arr)
# Bước 4: Tìm tất cả các file văn bản thỏa mãn query
def xor_(a,b):
	if a!=b:
		return 1
	else:
		return 0
def and_(a,b):
	if a==b and a==1:
		return 1
	else:
		return 0
def or_(a,b):
	if a==1 or b==1:
		return 1
	else:
		return 0
def not_(a,b):
	if a==1 and b==0:
		return 1
	else:
		return 0
arr =list(arr)

temp = sum(arr)
list_query = []
print("Danh sach các file văn bản thỏa mãn query: ")
for j in range(len(operand_logic)):
	arr1=[]
	for i in range(len(temp)):
		if len(arr)>1:
			if operand_logic[j]=='and':
				if and_(int(arr[0][i]) ,int(arr[1][i]))==1 :
					arr1.append(1)
				else:
					arr1.append(0)
				
			elif operand_logic[j]=='or':
				if or_(int(arr[0][i]) ,int(arr[1][i]))==1 :
					arr1.append(1)
				else:
					arr1.append(0)
			elif operand_logic[j] =='xor':
				if xor_(int(arr[0][i]) ,int(arr[1][i]))==1 :
					arr1.append(1)
				else:
					arr1.append(0)
			elif operand_logic[j] =='not':
				if xor_(int(arr[0][i]) ,int(arr[1][i]))==1 :
					arr1.append(1)
				else:
					arr1.append(0)
	if len(arr)>1:
		arr.remove(arr[0])
		arr.remove(arr[0])
		arr.append(arr1)
arr=np.array(arr)
for i in range(len(arr[0])):
	if int(arr[0][i])==1:
		print(files[i])