
# coding: utf-8

# In[1]:

import pandas as pd
# get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict


# In[2]:

csv1 = pd.read_csv('BX-Book-Ratings.csv',error_bad_lines=False, encoding='ISO-8859-1', sep=";" )
csv2 = pd.read_csv('BX-Books.csv',error_bad_lines=False, encoding='ISO-8859-1', sep=";" )
csv3 = pd.read_csv('BX-Users.csv',error_bad_lines=False, encoding='ISO-8859-1', sep=";" )


# In[3]:

# print(csv1.columns)
# print(csv2.columns)
# print(csv3.columns)



# In[4]:

# print(csv1.shape)
# print(csv2.shape)
# print(csv3.shape)


# # In[5]:

# csv1.head()
# # csv2.head()


# # In[6]:

# csv3.head()


# In[3]:

df1=pd.merge(csv1,csv2)


# In[4]:

df2=pd.merge(csv1,csv3)


# In[5]:

df=pd.merge(df1, df2)


# In[6]:

# df.head()


# # In[11]:

# df.columns


# In[12]:

# np.unique(df["Book-Title"],)[0]


# In[13]:

# df.head()


# In[7]:

df =df.drop([ 'ISBN', 'Image-URL-S', 'Image-URL-M',
       'Image-URL-L',],axis=1)


# In[8]:

df=df.sort_values(['Book-Title'])


# In[9]:

# df.head()


# In[10]:

df.reset_index(drop=True, inplace=True)


# In[11]:

# df.head()


# In[12]:

dic=OrderedDict()
rang = df.Age.shape[0]
for i in range(rang):
    if df['Book-Title'][i] not in dic.keys():
        ld=[]
        dic[df['Book-Title'][i]]=ld
        ld.append(df.Age[i])
#         print(df.Age[i])
    else:
#         print(df.Age[i])
        ld.append(df.Age[i])
    
# print(dic.values())
        


# In[13]:

vals=dic.values()


# In[14]:

# list(vals)[0]


# In[15]:

vals=list(vals)


# In[16]:

len_values=len(vals)


# In[17]:

print(len_values)


# ### discarding nan values

# In[18]:

for i,j in enumerate(list(dic.keys())):
    if False not in np.unique(np.isnan(vals[i])):
        del dic[j]


# In[19]:

print(list(dic.values())[0])


# ### filling nan with mean 

# In[20]:

print(len(list(dic.keys())))


# In[21]:

a=list(dic.values())


# In[22]:

for i in range(len(a)):
    temp = np.nanmean(a[i])
#     print(temp.dtype)
    for j in range(len(a[i])):
#         print (j)
#         assert j==np.nan
        if str(a[i][j])=="nan":
            a[i][j]=temp
            
    


# In[25]:

list(dic.values())[6]




# In[ ]:

Age=[]
# pd.DataFrame([lis.extend(i) for i in list(dic.values())])
for i in list(dic.values()):
    Age.extend(i)
    
Title=[]
for i,j in enumerate(list(dic.keys())):
    length = len(list(dic.values())[i])
    Title.extend(length*j)
mb=pd.DataFrame([Age,Title],columns=['Age','Title'])
print(mb.head())
