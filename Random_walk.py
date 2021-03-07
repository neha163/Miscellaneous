#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

#creating space for 2 subplots
fig, (ax1,ax2)  = plt.subplots( 1 , 2 , figsize = (20 , 10))

#the three times 
start_points = [10, 100, 1000]

#For each time
for i in start_points:
    walk_position=[]
    
    # We are going to generate 10000 walks of length i for enough stimulations
    for j in range(10000):
        
        #genetaing random probability of size time
        random_walk = np.random.choice([-1, 0, 1], p = [1/3, 1/3, 1/3], size = i)
        
        #to get the netdisplacent for each iterations 
        net_displacements = np.sum(random_walk)
        
        #appending the net displacements for each walk
        walk_position.append(net_displacements)
        
        #sorting for mulutative distributions
        walk_position.sort()
        relative_rank = np.arange(np.size(walk_position))/np.size(walk_position)
    
    #ploting for each of the three t's. histogram and line plot 
    ax1.hist(walk_position, histtype = 'stepfilled', label = 't = {}'.format(i), density = True, alpha = 0.4)
    ax2.plot(walk_position, relative_rank, label = 't = {}'.format(i), linestyle = '-.')

#adding basic essentials for the plot to look aesthtical and comprehensive    
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper left')
ax1.set_title('Probability density', fontsize = 30)
ax1.set_xlabel('displacement', fontsize =20)
ax1.set_ylabel('probability', fontsize  =20)
plt.title('Cumulative distribution', fontsize = 30)
plt.xlabel('Displacement', fontsize = 20)
plt.ylabel('Probability', fontsize =20)


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

#creating space for 2 subplots
fig, (ax1,ax2)  = plt.subplots( 1 , 2 , figsize = (20 , 10))

#the three times 
start_points = [10, 100, 1000]

#For each time
for i in start_points:
    walk_position=[]
    
    # We are going to generate 10000 walks of length i for enough stimulations
    for j in range(10000):
        
        #genetaing random probability of size time
        random_walk = np.random.choice([-1, 0, 1], p = [0, 1/2, 1/2], size = i)
        
        #to get the netdisplacent for each iterations 
        net_displacements = np.sum(random_walk)
        
        #appending the net displacements for each walk
        walk_position.append(net_displacements)
        
        #sorting for mulutative distributions
        walk_position.sort()
        relative_rank = np.arange(np.size(walk_position))/np.size(walk_position)
    
    #ploting for each of the three t's. histogram and line plot 
    ax1.hist(walk_position, histtype = 'stepfilled', label = 't = {}'.format(i), density = True, alpha = 0.4)
    ax2.plot(walk_position, relative_rank, label = 't = {}'.format(i), linestyle = '-.')

#adding basic essentials for the plot to look aesthtical and comprehensive    
ax1.legend(loc = 'upper left')
ax2.legend(loc = 'upper left')
ax1.set_title('Probability density', fontsize = 30)
ax1.set_xlabel('displacement', fontsize =20)
ax1.set_ylabel('probability', fontsize  =20)
plt.title('Cumulative distribution', fontsize = 30)
plt.xlabel('Displacement', fontsize = 20)
plt.ylabel('Probability', fontsize =20)


# In[ ]:




