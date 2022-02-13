# Maternal Health Classification
## 1.About
This repo contains a Python Classification algorithm. The data was retrieved from a kaggle dataset about Health issues during pregnancy.
Source : https://www.kaggle.com/csafrit2/maternal-health-risk-data

## 2.Requiremnts
'''
pip istall -r requirements.txt
'''
## 3.Train
The dataset is containd in the folder Dataset and has been separated to Train data , Test data and some data that can be used later for examples.

'''
python Train.py
'''

The saved Model will be saved on Clf folder. The pre trained classifiers are been provided in that folder.

## 4.Classification 
'''
python ClassificationReport.py
'''

  ||            precision  |  recall | f1-score |  support|
  |-|----------------------|---------|----------|---------|
  | high risk     |  0.92  |    0.91  |    0.91   |     53|
   | low risk      | 0.90   |   0.83  |    0.86   |     87|
   | mid risk       |0.71    |  0.81  |    0.76   |     58|

|    accuracy        |                |   0.84    |   198|
 |  macro avg      | 0.85     | 0.85  |    0.84   |    198|
|weighted avg       |0.85      |0.84  |    0.85   |    198|

# 5.Examples 
5 examples is provited in the Testsubject folder
|Name|Age|SystolicBP|DiastolicDP|BS|BodyTemp|HeartRate|RiskLevel|
|----|---|----------|-----------|--|--------|---------|---------|
|Lidia|	48|	120|	80|	11|	98|	88| High Risk|
|Georgia|	20|	110|	60|	7|	100|	70|Mid Risk|
|Nikoleta|	17|	110|	75|	13|	101|	76|High Risk|
|Eirini|	23|	100|	85|	7.5|	98	66|Low Risk|
|Agkeliki|	19|	120|	90|	6.8|	98|	60|Mid Risk|


