#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np 
import scipy.interpolate 


# In[8]:


field_vals = np.genfromtxt('ROTATED_TOPO_BATHY.csv', delimiter=' ')


# In[9]:


x_max, x_min = field_vals[:,0].max(), field_vals[:,0].min()


# In[10]:


y_max, y_min = field_vals[:,1].max(), field_vals[:,1].min()


# In[11]:


############  ############  ############


# In[12]:


x_vals = np.linspace(x_min,x_max,200) 
y_vals = np.linspace(y_min,y_max,200) 


# In[13]:


x_new = np.tile(np.array(x_vals), (200,1)) 
print(np.shape(x_new)) 
np.savetxt('x_new.csv', x_new) 


# In[14]:


y_new = np.empty_like(x_new)
np.shape(y_new)


# In[15]:


x_range = np.arange(0,np.shape(y_new)[0],1)
y_range = np.arange(0,np.shape(y_new)[1],1)


# In[16]:


for i in (x_range):
    for j in (y_range):
        y_new[i,j] = y_vals[i]


# In[17]:


np.savetxt('y_new.csv', y_new) 


# In[18]:


############  ############  ############


# In[19]:


interpolator_mv = scipy.interpolate.NearestNDInterpolator((field_vals[:,0], field_vals[:,1]), field_vals[:,2])


# In[20]:


z_new = np.empty_like(x_new)


# In[21]:


for i in range (0,np.shape(y_new)[0],1):
    for j in range (0,np.shape(y_new)[1],1):
        print (i,j)
        val =  interpolator_mv(x_new[i,j],y_new[i,j])
        print (val)
        z_new[i,j] = val


# In[22]:


np.savetxt('z_new.csv', z_new) 


# In[23]:


ne_layer = np.empty_like(x_new)
for i in range (0,np.shape(y_new)[0],1):
    for j in range (0,np.shape(y_new)[1],1):
        print (i,j)
        val =  interpolator_mv(x_new[i,j],y_new[i,j])
        if 0.1 < val < 3:
            ne_layer[i,j] = 0.0
        else:
            ne_layer[i,j] = 0.5


# In[24]:


np.savetxt('ne_layer.csv', ne_layer) 


# In[ ]:




