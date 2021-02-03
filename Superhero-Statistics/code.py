# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data["Gender"].replace("-","Agender",inplace=True)
plt.bar(data["Gender"].unique(),data["Gender"].value_counts())
plt.pie(data["Alignment"].value_counts(),labels=["Good","Bad","Neutral"],autopct="%1f.2f")
newdata=data[["Combat","Intelligence","Strength"]]
ci_cov=(newdata[["Combat","Intelligence"]].cov()).iloc[0,1]
cs_cov=(newdata[["Combat","Strength"]].cov()).iloc[0,1]
cstd=newdata["Combat"].std()
istd=newdata["Intelligence"].std()
sstd=newdata["Strength"].std()
ci_pearson=ci_cov/(cstd*istd)
cs_pearson=cs_cov/(cstd*sstd)
super_best_names=list(data[data["Total"]>data["Total"].quantile(q=0.99)]["Name"])



# Code starts here



