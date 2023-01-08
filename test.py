import pandas as pd 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sn

#import sequencing data
df = pd.read_csv("/home/arendscm/data-science-environment/data/raw/seq_data.csv")
#subset data frame
subdf = df[["Sample","Gene"]]
#transform into matrix
subdfdummy = pd.get_dummies(subdf,columns=['Gene']) #introduce dummies
df_mut = subdfdummy.groupby(by=['Sample']).sum() #sum by Sample
coocc = df_mut.T.dot(df_mut) # cooccurrence matrix

print(sn.heatmap(coocc,annot=True))


xaxis = np.array([2, 8])

# Y axis parameter:
yaxis = np.array([4, 9])

plt.plot(xaxis, yaxis)
plt.show()