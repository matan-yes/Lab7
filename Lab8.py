import pandas as pd
import  numpy as np
import  matplotlib as plt


#load file
df = pd.read_csv("C:\\train_Loan.csv")

#df['Random_Factor'] = np.random.randn(len(df))

#Add new column named  Normalized_Income with value sqrt('ApplicantIncome')*1.5
newCol = np.sqrt(df['ApplicantIncome'])*0.5
df = df.assign(Normalized_Income=newCol)
print(df)


#create dummy variable for attribute education for value 'Graduate' get value '1' for 'Not Graduate' get value '0'
df_Gender = pd.get_dummies(df['Education'])
df = df.join(df_Gender)

print(df)