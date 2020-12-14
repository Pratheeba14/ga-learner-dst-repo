# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var=bank_data.select_dtypes(include="object")
print(categorical_var)
numerical_var=bank_data.select_dtypes(include="number")
print(numerical_var)
categorical_var.shape
numerical_var.shape
banks = bank_data.drop('Loan_ID', axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks.fillna(banks.mode().iloc[0],inplace=True)
print(banks.isnull().sum())
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(round(avg_loan_amount['LoanAmount'][1],2))
loan_approved_se=(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')
loan_approved_nse=(banks['Self_Employed']=="No") &(banks['Loan_Status']=="Y")
banks['Loan_Status'].count()
percentage_se=((banks[loan_approved_se]['Loan_Status'].count()/banks['Loan_Status'].count())*100)
percentage_nse=((banks[loan_approved_nse]['Loan_Status'].count()/banks['Loan_Status'].count())*100)
loan_term=banks["Loan_Amount_Term"].apply(lambda x:x/12)
big_loan_term = len(loan_term[loan_term >= 25])
loan_groupby=banks.groupby("Loan_Status")
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.agg(np.mean)
print(mean_values.iloc[1,0], 2)


