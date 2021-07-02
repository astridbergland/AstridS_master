import pandas as pd
header_list = ['Depth','Pres','Temp','Ptemp','Cnd','Sal','sigt', 'sigtheta']
df = pd.read_csv('SC97nocast',skiprows= 4,header = None,delim_whitespace=True,names=header_list)
df1 = df.loc[(df['Temp'])>=0]
print(df1['Temp'].mean())
