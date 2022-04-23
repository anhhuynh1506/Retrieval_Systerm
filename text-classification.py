# -*- coding: utf-8 -*-
"""Assignment_7_Retrival.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dwhro6UO3rANi4cI2j90zxxLH-md6LWQ

#Download Data
"""

!sudo wget -O /usr/sbin/gdrivedl 'https://f.mjh.nz/gdrivedl'
!sudo chmod +x /usr/sbin/gdrivedl

!gdrivedl "https://drive.google.com/file/d/1nzjCrSSlBAsWa9GXEI218zfsmuLEj9F0/view?usp=sharing"

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/
!tar -zxvf "/content/20_newsgroups.tar.gz"

"""#Data processing"""

import os

f_path = "/content/20_newsgroups"
folder_label = os.listdir(f_path)
print(folder_label)
print(len(folder_label))

#Lưu tên của từng document trong mỗi folder
Documents = []
Path_name_list = []
Y_label = []
for f in folder_label:
  file_path = os.path.join(f_path, f)
  list_file = os.listdir(file_path) 
  for file_name in list_file:
    path = os.path.join(file_path, file_name)
    new_path = path + '.txt'
    os.rename(path, new_path)
    Path_name_list.append(new_path)
    Y_label.append(f)

  Documents.append([files for files in list_file])

#Documents = [[list_file of class_1], [list_file of class_2], ... [list_file of class_20]]
#Path_name_list lưu đường dẫn của mỗi file để tiện cho việc chi tập train và tập test
#Y_label lưu nhãn của từng file

Nof = 0
for i in range(len(Documents)):
  Nof += len((Documents[i]))

print("Kiểm tra số lượng file trong dataset: ", Nof)
print("Kiem tra so lượng đường dẫn: ", len(Path_name_list))
print("kiểm tra số lượng label: ", len(Y_label))
print("File_name: ", Documents[0][0])
print("Label: ", Y_label[0])
print("Link: ", Path_name_list[0])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Path_name_list, Y_label, test_size=0.25, random_state=0)

print(len(X_train))
print(len(y_train))

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at',
 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 
 'can', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during',
 'each', 'few', 'for', 'from', 'further', 
 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's",
 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's",
 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself',
 "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself',
 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours' 'ourselves', 'out', 'over', 'own',
 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 
 'than', 'that',"that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", 
 "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 
 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where',
 "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's",'will', 'with', "won't", 'would', "wouldn't", 
 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 
 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'hundred', 'thousand', '1st', '2nd', '3rd',
 '4th', '5th', '6th', '7th', '8th', '9th', '10th']

import string 
def Preprocess_data(words):

  #Sử dụng hàm maketrans() để xóa đi ký tự tab
  tab = str.maketrans('', '', '\t')
  words = [word.translate(tab) for word in words]

  #Xóa đi các ký tự đặc biệt, hàm string.punctuation trả về kết quả là 1 dãy các ký tự đặc biệt !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
  punctuations = (string.punctuation).replace("'", "")
  punc = str.maketrans('', '', punctuations)
  filtered_words = [word.translate(punc) for word in words]

  #Sau khi đã loại bỏ các ký tự đặc biệt, câu lệnh dưới loại bỏ những phần tử là khoảng trắng
  words = [str for str in filtered_words if str]

  #Chỉnh sửa một số từ có dấu " ' " ở đầu hoặc cuối từ đó, nếu dấu " ' " ở giữa từ thì giữ nguyên để đảm bảo tính toàn vẹn của từ
  edit_words = []
  for w in words:
      if (w[0] and w[len(w)-1] == "'"):
          w = w[1:len(w)-1]
      elif(w[0] == "'"):
          w = w[1:len(w)]
      else:
          w = w
      edit_words.append(w)
  
  words = edit_words.copy()

  #Xóa những từ là số 
  words = [word for word in words if not word.isdigit()]

  #Xóa những từ chỉ có 1 ký tự
  words = [word for word in words if not len(word) == 1]

  #Chuyển tất cả từ về chữ thường
  words = [word.lower() for word in words]

  return words

#Xóa những từ là đại từ nhân xừng, từ hỏi, động từ đặc biệt, giới từ,...
def Remove_SpecialWord(words):

  words = [word for word in words if word not in stopwords]
  
  return words

#Tách từ 
def Tokenization(sentences):

  token = sentences[0:len(sentences)-1].strip().split(" ")
  token = Preprocess_data(token)
  token = Remove_SpecialWord(token)

  return token

#xóa những hàng là hàng trống 
def remove_line(lines):
  for i in range(len(lines)):
    if(lines[i] == "\n"):
      s = i + 1
      break
  next_lines = lines[s:]
  return next_lines

def word_tokenize(doc_path):
  #đọc file doc
  print(doc_path)
  try:
    with open(doc_path, 'r') as f:
      text_lines = f.readlines()

      #xóa hàng trống trong doc
      text_lines = remove_line(text_lines)

      #lưu trữ các từ trong doc
      word_holder = []

      #duyệt qua toàn bộ doc và tách từ từng hàng trong doc
      for l in text_lines:
        word_holder.append(Tokenization(l))
      
      return word_holder
  except:
      return None

def flatten(holder):
  new_holder = []
  for doc in holder:
    for w in doc:
      new_holder.append(w)
  return new_holder

print(len(X_train))

vocabulary = []
for doc in X_train:
  w_token = word_tokenize(doc)
  print(w_token)
  if w_token != None:
    vocabulary.append(flatten(w_token))
  else:
    vocabulary.append(w_token)

vocabulary_test = []
for doc in X_test:
  w_token = word_tokenize(doc)
  if w_token != None:
    vocabulary_test.append(flatten(w_token))
  else:
    vocabulary_test.append(w_token)

for i in range(len(vocabulary)-1):
  if vocabulary[i] == None:
    vocabulary.pop(i)
    y_train.pop(i)
    i -= 1

i = 0
for i in range(len(vocabulary_test)-1):
  if vocabulary_test[i] == None:
    vocabulary_test.pop(i)
    y_test.pop(i)
    i -= 1

import numpy as np
np_vocabulary = np.asarray(flatten(vocabulary))

words, counts = np.unique(np_vocabulary, return_counts=True)
len(words)

import numpy as np
np_vocabulary_test = np.asarray(flatten(vocabulary_test))

freq, wrds = (list(i) for i in zip(*(sorted(zip(counts, words), reverse=True))))

n = 2000
features = wrds[0:n]

dictionary = {}
doc_num = 1
for doc_words in vocabulary:
    #print(doc_words)
    np_doc_words = np.asarray(doc_words)
    w, c = np.unique(np_doc_words, return_counts=True)
    dictionary[doc_num] = {}
    for i in range(len(w)):
        dictionary[doc_num][w[i]] = c[i]
    doc_num = doc_num + 1

dictionary_test = {}
doc_num = 1
for doc_words in vocabulary_test:
    #print(doc_words)
    np_doc_words = np.asarray(doc_words)
    w, c = np.unique(np_doc_words, return_counts=True)
    dictionary_test[doc_num] = {}
    for i in range(len(w)):
        dictionary_test[doc_num][w[i]] = c[i]
    doc_num = doc_num + 1

X_train = []
for k in dictionary.keys():
    row = []
    for f in features:
        if(f in dictionary[k].keys()):
            #if word f is present in the dictionary of the document as a key, its value is copied
            #this gives us no. of occurences
            row.append(dictionary[k][f]) 
        else:
            #if not present, the no. of occurences is zero
            row.append(0)
    X_train.append(row)

X_test = []
for k in dictionary_test.keys():
    row = []
    for f in features:
        if(f in dictionary_test[k].keys()):
            #if word f is present in the dictionary of the document as a key, its value is copied
            #this gives us no. of occurences
            row.append(dictionary_test[k][f]) 
        else:
            #if not present, the no. of occurences is zero
            row.append(0)
    X_test.append(row)

X_train = np.asarray(X_train)
y_train = np.asarray(y_train)

X_test = np.asarray(X_test)
Y_test = np.asarray(y_test)

len(X_train)

len(y_train)

len(X_test)

len(y_test)

"""#Naive Bayes"""

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X_train, y_train)

Y_predict = clf.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(accuracy_score(y_test, Y_predict))
print(classification_report(Y_test, Y_predict))

"""#KNN"""

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=21)
neigh.fit(X_train, y_train)

Y_pred = neigh.predict(X_test)

print(accuracy_score(y_test, Y_pred))
print(classification_report(y_test, Y_pred))