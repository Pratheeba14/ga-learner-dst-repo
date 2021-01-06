# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(path)
loan_status=data["Loan_Status"].value_counts()
loan_status.plot(kind="bar")
property_and_loan=data.groupby(["Property_Area","Loan_Status"]).size().unstack()
property_and_loan.plot(kind="bar",stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack()
education_and_loan.plot(kind="bar",stacked=True)
plt.xlabel("Education")
plt.ylabel("Loan_Status")
plt.xticks(rotation=45)
graduate=data[data["Education"]=="Graduate"]
not_graduate=data[data["Education"]=="Not Graduate"]
graduate["LoanAmount"].plot(kind="density",label="Graduate")
not_graduate["LoanAmount"].plot(kind="density",label="Not Graduate")
fig ,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(10,10))
ax_1.scatter(x=data["ApplicantIncome"],y=data["LoanAmount"])
ax_1.set(title="Applicant Income")
ax_2.scatter(x=data["CoapplicantIncome"],y=data["LoanAmount"])
ax_2.set(title="CoapplicantIncome")
data["TotalIncome"]=data["CoapplicantIncome"]+data["ApplicantIncome"]
plt.scatter(x=data["TotalIncome"],y=data["LoanAmount"])
ax_3.set(title="Total Income")
plt.show()


