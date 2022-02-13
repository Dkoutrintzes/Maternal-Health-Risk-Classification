import pickle
import os
import sys
import csv
if __name__ == '__main__':
    #print(sys.argv)
    try:
        file = sys.argv[1]
        if os.path.isfile(file):
            pass
        else:
            print('File Doesnt Exist.\nPlease Try Again')
            sys.exit()
    except:
        print('File Doesnt Exist.\nPlease Try Again')
        sys.exit()
    

    hrmodel = pickle.load(open('Clr/HRiskClr.sav','rb')) 
    mlrmodel = pickle.load(open('Clr/MLRiskClr.sav','rb')) 
    data = []
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)

        for line in reader:
            data.append(line)
    print(data)

    apred = hrmodel.predict(data)

    print(apred)
    if apred[0] == 'b':
        Result = 'High Risk'
    else:
        Result = mlrmodel.predict(data)[0]


    print('The patient has been diagnosed with '+Result+' level for mental issues.')

