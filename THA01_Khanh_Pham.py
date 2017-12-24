
# coding: utf-8

# In[ ]:

import pandas as pd


# In[ ]:

import numpy as np


# In[ ]:

import  matplotlib.pyplot as plt 


# # Import Personel data

# In[ ]:

Personel = pd.read_table('CaliforniaHospitalData_Personnel.txt', sep = '\t')
Personel


# In[ ]:

#Import Hospital data
Hospital = pd.read_csv('CaliforniaHospitalData.csv',sep=',')
Hospital



# # Join Two Tables

# In[ ]:

df = pd.concat([Personel, Hospital], axis=1, join='inner')
df


# # Drop columns

# In[ ]:

df.drop(['Work_ID','Position_ID','Website'], axis=1, inplace=True)


# In[ ]:

df.columns


# # Delete Duplicate Columns

# In[ ]:

df = df.loc[:, ~df.columns.duplicated()]


# In[ ]:

df.columns


# In[ ]:

df[df['OperInc']<0]['OperInc']


# In[ ]:

df1 = (df['Teaching'] == "Small/Rural")
df2 = (df['AvlBeds'] >= 15)
df3 = (df['OperInc']<0)
df4 = df[df1 & df3 & df2]
df4.columns


# # Export your data as tabdelimited

# In[ ]:

df4.to_csv(r'hospital_data_new.txt', header=None, index=None, sep='\t', mode='a')


# # Change the name the file hospital_data_new.txt

# In[ ]:

df5 = df4.rename(columns={'NoFTE':'FullTimeCount','NetPatRev':'NetPatientRevenue','InOperExp' : 'InpatientOperExp','OutOperExp':'OutpatientOperExp','OperRev':'Operating_Revenue','OperInc':'Operating_Income'}) 


# In[ ]:

df5.columns


# In[ ]:

df6 = df5[:2]
df6


# # INSERT

# In[ ]:

ppf = Personel.copy()


# In[ ]:

ppf[:1]


# In[ ]:

ppf['PositionTitle'].unique()


# In[ ]:

ppf.loc[61]=[20266, 231581, 'Khanh', 'Pham', 'M', 1, 'Regional Representative', 46978, 4, '09/03/2017']


# In[ ]:

ppf.loc[62]=[20266, 231581, 'Khanh', 'Pham', 'M', 2, 'State Board Representative', 89473, 3, '09/03/2017']


# In[ ]:

ppf.dtypes


# # # Convert to datetime dtype

# In[ ]:

ppf['StartDate'] =  pd.to_datetime(ppf['StartDate'], format='%m/%d/%Y')


# In[ ]:

ppf


# # Export hospital which is non-profit, 250 em or NetPatRen <=109

# In[ ]:

df


# # Reprensentative &Income > 100000

# In[ ]:

cn1 = df['PositionTitle'] == 'State Board Representative'
cn2 = df['OperInc']  > 100000
dfE = df[cn1&cn2] 
dfE


# # Group by and count

# In[ ]:

dfnum = df.groupby(['HospitalID'])['HospitalID'].count().reset_index(name='Num_Employees') 


# In[ ]:

dfT = pd.concat([dfnum, Hospital], axis=1, join='inner')
dfT


# In[ ]:

cnd1 = dfT['Num_Employees'] > 250
cnd2 = dfT['TypeControl']=='Non Profit'
cnd3 = dfT['NetPatRev'] < 109000

dfNew = dfT[(cnd1&cnd2)|cnd3]
dfNew


# # Export Text File

# In[ ]:

dfNew.to_csv(r'New DataFrame.txt', header=None, index=None, sep='\t', mode='a')


# # Kfold

# In[ ]:

from sklearn.cross_validation import KFold
kf = KFold(len(df.index),n_folds = 4)
for train, test in kf:
    print("%s %s" %(train,test))


# # Save Training_Data File

# In[ ]:

df.ix[train]


# In[ ]:

df.to_csv(r'training_data.txt', header=None, index=None, sep=',', mode='a')


# # Save Text_Data File

# In[ ]:

df.ix[test]


# In[ ]:

df.to_csv(r'test_data.txt', header=None, index=None, sep=',', mode='a')

