# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
total=len(df)
p_a=len(df[df["fico"]>700])/total
p_b=len(df[df["purpose"]=="debt_consolidation"])/total
df1=df[df["purpose"]=="debt_consolidation"]
p_a_b=len(df1[df1["fico"]>700])/len(df1)
result=(p_a_b==p_a)
print(result)

prob_lp=len(df[df["paid.back.loan"]=="Yes"])/total
prob_cs=len(df[df["credit.policy"]=="Yes"])/total
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print("{0:.3f}".format (bayes))

df["purpose"].value_counts().plot.bar()
df1=df[df['paid.back.loan']=="No"]
df1['purpose'].value_counts().plot.bar()

inst_median=df["installment"].median()
inst_mean=df["installment"].mean()
df["installment"].hist()
df["log.annual.inc"].hist()



