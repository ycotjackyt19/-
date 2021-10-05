#!/usr/bin/env python
# coding: utf-8

# In[1]:


1


# In[2]:


1.2


# In[3]:


import numpy as np


# In[4]:



v= [1, 2, 3, 4]
v


# In[5]:


v= np.array(v)
v


# In[6]:


v.shape


# In[7]:


A= [[1,2,3,4],
    [5,6,7,8]]
A


# In[8]:


A= np.array(A)
A


# In[9]:


A.shape


# In[10]:


T=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
T


# In[11]:


T= np.array(T)
T


# In[12]:


T.shape


# In[13]:


T= T.reshape((2,2,4))
T


# In[14]:


T.shape


# In[15]:


T[0]


# In[16]:


T[1]


# In[17]:


v.ndim


# In[18]:


A.ndim


# In[19]:


T.ndim


# In[20]:


T4d= T.reshape(2,2,2,2)
T4d


# In[21]:


T4d.shape


# In[22]:


v, A, T, T4d


# In[23]:


v


# In[24]:


v14= v.reshape(1,4)
v14


# In[25]:


v41= v.reshape(4,1)
v41


# In[26]:


v.shape, v14.shape, v41.shape


# In[ ]:




