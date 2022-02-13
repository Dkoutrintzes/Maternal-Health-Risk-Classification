import os
import csv
import numpy as np
import random
from sklearn.model_selection import train_test_split

file = 'Maternal Health Risk Data Set.csv'

data = []
risklevel = []


first = True
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if first:
            first = False
            continue
        risklevel.append([line[-1]])
        data.append(line[:-1])


X_train, X_test, y_train, y_test = train_test_split(data, risklevel, test_size=0.2,shuffle=True)

print("Number of Train Data: "+ str(len(X_train)))



with open('Dataset/Train_Data.csv','w',newline='') as newfile1:
    writer = csv.writer(newfile1)
    for line in X_train:
        writer.writerow(line)


with open('Dataset/Train_Labels.csv','w',newline='') as newfile3:
    writer = csv.writer(newfile3)
    for line in y_train:
        writer.writerow(line)

ids = []
while len(ids) < 5:
    i = random.randint(0,len(X_test))
    if i not in ids:
        ids.append(i)
ids.sort()
#print(ids)

Testdata = []
Testlabels = []

showdata = []
showlabel = []

for i in range(len(X_test)):
    if i in ids:
        showdata.append(X_test[i])
        showlabel.append(y_test[i])
    else:
        Testdata.append(X_test[i])
        Testlabels.append(y_test[i])


print("Number of Test Data: "+ str(len(Testdata)))



with open('Dataset/Test_Data.csv','w',newline='') as newfile2:
    writer = csv.writer(newfile2)
    for line in Testdata:
        writer.writerow(line)

with open('Dataset/Test_Labels.csv','w',newline='') as newfile4:
    writer = csv.writer(newfile4)
    for line in Testlabels:
        writer.writerow(line)



with open('Dataset/Show_Data.csv','w',newline='') as newfile2:
    writer = csv.writer(newfile2)
    for line in showdata:
        writer.writerow(line)

with open('Dataset/Show_Labels.csv','w',newline='') as newfile4:
    writer = csv.writer(newfile4)
    for line in showlabel:
        writer.writerow(line)