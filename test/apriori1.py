from apriori import *
import pandas as pd
filename="D:\各种数据集\专利数据\INVT：CITY.xlsx"
dframe=pd.read_excel(filename,header=None)
change=lambda x:pd.Series(1,index=x[pd.notnull(x)])
mapok=map(change,dframe.as_matrix())
data=pd.DataFrame(list(mapok)).fillna(0)
#设置置信度阈值和支持度阈值
surpport=0.2
cfd=0.3
print(find_rule(data,surpport,cfd))