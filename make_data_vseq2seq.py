#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from tqdm import tqdm

label='test'
f = open(f"dataset/{label}.txt","r",encoding='utf-8') 
data=f.read()

utterances = data.split(' __eou__ ')
SRC=utterances
TRG=utterances

data = pd.DataFrame(list(zip(SRC,TRG)),columns=['SRC','TRG'])
data.to_csv(f'dataset/{label}.csv',index=False)


# In[ ]:




