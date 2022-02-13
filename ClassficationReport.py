from sklearn.metrics import classification_report
import pickle
import sys
import csv
def loadcsv(path):
    data = []
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)

        for line in reader:
            data.append(line)
    return data

if __name__ == '__main__':
    hrmodel = pickle.load(open('Clr/HRiskClr.sav','rb')) 
    mlrmodel = pickle.load(open('Clr/MLRiskClr.sav','rb')) 

    testdata = loadcsv('Dataset/Test_Data.csv')
    riskleveltest = loadcsv('Dataset/Test_Labels.csv')


    firstpredicts = hrmodel.predict(testdata)

    finalpresdicts = []

    for i in range(len(testdata)):
        if firstpredicts[i] == 'a':
            secondpredict = mlrmodel.predict([testdata[i]])
            finalpresdicts.append(secondpredict[0])
        else:
            finalpresdicts.append('high risk')

    print(classification_report(riskleveltest,finalpresdicts))
    