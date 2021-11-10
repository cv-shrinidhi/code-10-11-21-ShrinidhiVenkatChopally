import json
import pandas as pd
import functools
f = open('PatientData.json')
bmiIndex = []
count = [0]*6
print(count)
bmiCategory = []
healthRisk = []
patientData = pd.read_json(f)
for row in patientData.itertuples():
    bmi = (int(row[3])*100*100)/(int(row[2])*int(row[2]))
    bmiIndex.append(format(bmi,'.1f'))
    if(bmi<=18.4):
        count[0] += 1
        bmiCategory.append('Underweight')
        healthRisk.append('Malnutrition risk')
    elif(bmi>=18.5 and bmi<=24.9):
        count[1] += 1
        bmiCategory.append('Normal weight')
        healthRisk.append('Low risk')
    elif(bmi>=25 and bmi<=29.9):
        count[2] += 1
        bmiCategory.append('Overweight')
        healthRisk.append('Enhanced risk')
    elif(bmi>=30 and bmi<=34.9):
        count[3] += 1
        bmiCategory.append('Moderately obese')
        healthRisk.append('Medium risk')
    elif(bmi>=35 and bmi<=39.9):
        count[4] += 1
        bmiCategory.append('Severely obese')
        healthRisk.append('High risk')
    elif(bmi>=40):
        count[5] += 1
        bmiCategory.append('Very severely obese')
        healthRisk.append('Very high risk')
patientData = patientData.assign(**{'BMI': pd.Series(bmiIndex)})
patientData = patientData.assign(**{'BMI Category': pd.Series(bmiCategory)})
patientData = patientData.assign(**{'Health Risk': pd.Series(healthRisk)})
# below is the solution of question 1
print('below is the updated patient data with BMI index, BMI category and health risk added')
print(patientData)
# below is the solution of question 2
print('below is the count of number of overweight people')
print(count[2])
print('the number of patients with other BMI category are also calculated')


