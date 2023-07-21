import numpy as np
import pandas as pd


df=pd.DataFrame(pd.read_excel('bom3.xlsx'))
print("done")
print("df.shape is :",df.shape,end="\n")
print("df.length is :",len(df))
#print("df.info is :",df.info,end="\n")
#print("df.dtype is :",df.dtypes,end="\n")
rc_all = []
print("df.columns is:\n",df.columns)
print("df.插件位置 is:\n",df['插件位置'])


rc_all = df['插件位置']
print("all 插件位置 is:\n",rc_all)
print("all 插件位置 shape is :\n",rc_all.shape)

print("all 插件位置 第五个 is :\n",rc_all[4])


test_r ='ACE1'
for each in rc_all:
    if str(each) != 'nan':
        #print(len(each))
        print(each)
        if test_r in each:
            print("true")
        else:
            print("false")


#