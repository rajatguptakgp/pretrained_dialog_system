#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from tqdm import tqdm

label='test'
f = open(f"dataset/{label}.txt","r",encoding='utf-8') 
data=f.read()

dialogs = data.split('\n')

df=[]
SRC=[]
TRG=[]

for i in tqdm(range(len(dialogs))):
    df.append(dialogs[i].split(' __eou__ '))
    
for i in range(len(df)-1):
    
    j=1
    if (len(df[i])>2):
        for j in range(2,len(df[i])-1):
            SRC.append(df[i][:j])
            TRG.append(df[i][j])
            
        j+=1
        
        SRC.append(df[i][:j])
        TRG.append(df[i][j].split(' __eou__')[0])
        
    else:
        
        SRC.append(df[i][0])
        TRG.append(df[i][1].split(' __eou__')[0]) 
        
data = pd.DataFrame(list(zip(SRC,TRG)),columns=['SRC','TRG'])

data.to_csv(f'dataset/{label}.csv',index=False)

