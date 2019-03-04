
# coding: utf-8

# 0 = agreement equivalent to chance.
# 0.1 – 0.20 = slight agreement.
# 0.21 – 0.40 = fair agreement.
# 0.41 – 0.60 = moderate agreement.
# 0.61 – 0.80 = substantial agreement.
# 0.81 – 0.99 = near perfect agreement
# 1 = perfect agreement.

# weighted kappa for ordinal values

# In[1]:


import pandas as pd


# In[7]:


df=pd.read_excel("/home/joshi_anurag/Desktop/PRA/SingleRater.xlsx",sheetname='Ranks')


# In[8]:


print(df)


# In[9]:


import sklearn.metrics


# In[10]:



x=df['Student Rating'].values.tolist()


# In[11]:


y=df['Instructor Rating'].values.tolist()


# In[12]:


print(x)


# In[13]:


print(y) 

# In[14]:


from sklearn.metrics import cohen_kappa_score


# In[18]:


cohen=cohen_kappa_score(x, y, labels=None, weights='linear', sample_weight=None)


# In[19]:


print(cohen)

