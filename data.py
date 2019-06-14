#!/usr/bin/env python
# coding: utf-8

# In[69]:


import pandas as pd
import numpy as np
import gc
import sys
from pymatgen import Lattice, Structure
import numpy
import xrayutilities as xru
from xrayutilities.materials.cif import CIFFile
from xrayutilities.materials.material import Crystal
from IPython.display import Image, display


df = pd.read_csv("data.csv")
task_id = df["Material_id"]
two_theta = numpy.arange(0, 80,.2)
theta = numpy.arange(0,400)
len_ = int(sys.argv[1])
try :
    df_x = pd.read_csv("final_data_x.csv")
except:
    df_x = pd.DataFrame(columns=theta)

if len_ !=0:
    del df_x["Unnamed: 0"]


   


# In[70]:



L = []
M = []
c = 0
for x  in range(len_*20,len_*20+20):
 try:
     xu_cif = CIFFile("cif/"+task_id[x]+".cif")
     xu_crystal = Crystal(name="XRD" ,lat=xu_cif.SGLattice())
     powder = xru.simpack.smaterials.Powder(xu_crystal, 1)
     pm = xru.simpack.PowderModel(powder,I0=100)
     intensities = pm.simulate(two_theta)
     M.append(intensities)
     print(np.shape(M))
     pm.close()
 except ValueError:
     print("some_error")


# In[71]:


df_x_ = pd.DataFrame(M,columns=df_x.columns)


# In[72]:





# In[73]:





# In[74]:


df_x_s=df_x.append(df_x_)


# In[75]:


df_x_s.to_csv("final_data_x.csv") 


# In[76]:




# In[ ]:




