#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt
import numpy as np
import math


# In[17]:


COORDS = np.loadtxt('TOPO_BATHY.csv', delimiter=',')


# In[18]:


COORDS


# In[19]:


center_x, center_y = COORDS[:,0].min(), COORDS[:,1].min()


# In[20]:


plt.scatter(COORDS[:,0], COORDS[:,1], c=COORDS[:,2], cmap=plt.cm.jet)


# In[21]:


def rotate_matrix (x, y, angle, x_shift=0, y_shift=0, units="DEGREES"):
    """
    Rotates a point in the xy-plane counterclockwise through an angle about the origin
    https://en.wikipedia.org/wiki/Rotation_matrix
    :param x: x coordinate
    :param y: y coordinate
    :param x_shift: x-axis shift from origin (0, 0)
    :param y_shift: y-axis shift from origin (0, 0)
    :param angle: The rotation angle in degrees
    :param units: DEGREES (default) or RADIANS
    :return: Tuple of rotated x and y
    """

    # Shift to origin (0,0)
    x = x - x_shift
    y = y - y_shift

    # Convert degrees to radians
    if units == "DEGREES":
        angle = math.radians(angle)

    # Rotation matrix multiplication to get rotated x & y
    xr = (x * math.cos(angle)) - (y * math.sin(angle)) + x_shift
    yr = (x * math.sin(angle)) + (y * math.cos(angle)) + y_shift

    return xr, yr


# In[26]:


xr, yr = rotate_matrix(COORDS[:,0],COORDS[:,1],180)


# In[27]:


plt.scatter(xr, yr, c=COORDS[:,2], cmap=plt.cm.jet)


# In[28]:


#ROTATED GRID SAVE


# In[34]:


ROT_GRD = np.c_[xr, yr,COORDS[:,2]]


# In[37]:


np.savetxt('ROTATED_TOPO_BATHY.csv',ROT_GRD)


# In[ ]:




