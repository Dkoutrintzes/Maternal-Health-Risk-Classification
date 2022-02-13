import pickle
import sys
if __name__ == '__main__':
    #print(sys.argv)
    try:
        datas = len(sys.argv)
        
        if datas == 7:
            pass
        else:
            print('Stats are not enough.\nPlease Try Again')
            sys.exit()
    except:
        print('Stats are not enough.\nPlease Try Again')
        sys.exit()
    

    hrmodel = pickle.load(open('Clr/HRiskClr.sav','rb')) 
    mlrmodel = pickle.load(open('Clr/MLRiskClr.sav','rb')) 
    data = [sys.argv[1:]]
    print(data)

    apred = hrmodel.predict(data)

    print(apred)
    if apred[0] == 'b':
        Result = 'High Risk'
    else:
        Result = mlrmodel.predict(data)[0]


    print('The patient has been diagnosed with '+Result+' level for mental issues.')

