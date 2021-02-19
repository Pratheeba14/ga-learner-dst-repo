# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
data_sample=data.sample(n=sample_size,random_state=0)
sample_mean=data_sample["installment"].mean()
margin_of_error=z_critical*(data["installment"].std()/math.sqrt(sample_size))
confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)
true_mean=data["installment"].mean()
print(true_mean)
print(confidence_interval)

sample_size=np.array([20,50,100])
fig,ax=plt.subplots(1,3)
for i in range(len(sample_size)):
    me_an=[]
    for j in range(1000):
        sample_mean_inst=data["installment"].sample(sample_size[i]).mean()
        me_an.append(sample_mean_inst)
    mean_series=pd.Series(me_an)
    ax[i].hist(mean_series,bins=1000)
plt.show()

data["int.rate"]=data["int.rate"].str.replace("%","").astype(float)
z_statistic_1,p_value_1=ztest(data[data["purpose"]=="small_business"]["int.rate"],value=data["int.rate"].mean(),alternative="larger")
if p_value_1<0.05:
    print("Reject")
else:
    print("Accept")

z_statistic_2,p_value_2=ztest(data[data["paid.back.loan"]=="No"]["installment"],data[data["paid.back.loan"]=="Yes"]["installment"])

purp=pd.crosstab(data["purpose"],data["paid.back.loan"])
chi2,p_value,dof,ex=chi2_contingency(purp)

if chi2>critical_value:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")






