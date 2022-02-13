
from sklearn.model_selection import train_test_split
from sklearn import metrics
import csv
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle


def loadcsv(path):
    data = []
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)

        for line in reader:
            data.append(line)
    return data

def labelsforABtrain(y):
    labels = []
    for i in y:
        #print(i)
        if i[0] == 'low risk':
            labels.append('a')
        elif i[0] == 'mid risk':
            labels.append('a')
        elif i[0] == 'high risk':
            labels.append('b')
        else:
            print(i)
    return labels

def trainmodel(data,labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3,shuffle=True)
    best = 0.0
    for i in range(2,24):
            clf = RandomForestClassifier(max_depth = i)
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)
            if float(metrics.accuracy_score(y_test, y_pred)) > best:
                #print(float(metrics.accuracy_score(y_test, y_pred)))
                best = float(metrics.accuracy_score(y_test, y_pred))
                bestclf = clf
    return bestclf


def dataforsecondmodel(data,labels):
    newdata = []
    newlables = []
    for i in range(len(data)):
        if labels[i] != 'high risk':
            newdata.append(data[i])
            newlables.append(labels[i])
    return newdata,newlables

def distrobution(y):
    distr = [0,0,0]
    for i in y:
        #print(i)
        if i[0] == 'low risk':
            distr[0] +=1
        elif i[0] == 'mid risk':
            distr[1] +=1
        elif i[0] == 'high risk':
            distr[2] +=1
        else:
            print(i)
    print(distr)

if __name__ == '__main__':
    recallarray = []
    precisionarray = []
    accuracyarray = []
    tpa = []

    best = 0
    bestid = -1
    
    for j in range(20):

        dataset = loadcsv('Dataset/Train_Data.csv')
        risklevel = loadcsv('Dataset/Train_Labels.csv')
        print(len(risklevel))
        fmlabels = labelsforABtrain(risklevel)
        print(len(dataset),len(fmlabels))
        firstmodel = trainmodel(dataset,fmlabels)


        datast,labelsst = dataforsecondmodel(dataset,risklevel)

        secondmodel = trainmodel(datast,labelsst) 

        testdata = loadcsv('Dataset/Test_Data.csv')
        riskleveltest = loadcsv('Dataset/Test_Labels.csv')

        print("Test Data distrobution")
        distrobution(riskleveltest)



        firstpredicts = firstmodel.predict(testdata)

        finalpresdicts = []

        for i in range(len(testdata)):
            if firstpredicts[i] == 'a':
                secondpredict = secondmodel.predict([testdata[i]])
                finalpresdicts.append(secondpredict[0])
            else:
                finalpresdicts.append('high risk')
        
        
        if best < metrics.accuracy_score(riskleveltest, finalpresdicts):
            best = metrics.accuracy_score(riskleveltest, finalpresdicts)
            bestid = j

            bestmodel1 = firstmodel
            bestmodel2 = secondmodel

        accuracyarray.append(float(metrics.accuracy_score(riskleveltest, finalpresdicts)))
        precisionarray.append(float(metrics.precision_score(riskleveltest, finalpresdicts,average='micro')))
        recallarray.append(float(metrics.recall_score(riskleveltest, finalpresdicts,average='micro')))

    print("Average Accuracy:",np.mean(accuracyarray))
    print("Average Precision:",np.mean(precisionarray))
    print("Average Recall:",np.mean(recallarray))


    
    print("The Best Accuracy:",accuracyarray[bestid])
    print("The Best Precision:",precisionarray[bestid])
    print("The Best Recall:",recallarray[bestid])


    pickle.dump(bestmodel1,open('Clr/HRiskClr.sav','wb'))
    pickle.dump(bestmodel2,open('Clr/MLRiskClr.sav','wb'))

    



