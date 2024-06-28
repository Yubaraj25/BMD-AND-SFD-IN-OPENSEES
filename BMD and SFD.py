#!/usr/bin/env python
# coding: utf-8

# In[34]:


import planesections as ps
import openseespy.opensees as ops
from planesections import plotBeamDiagram
import matplotlib.pyplot as plt


# In[35]:


L = 25
beam = ps.newEulerBeam(L)
pinned = [1,1,0]
beam.setFixity=(0, pinned)
beam.setFixity=(L*0.8, pinned)


# In[36]:


Pz= -1000
beam.addLabel(0, label='A')
beam.addLabel(10, label='E')
beam.addVerticalLoad(15, 2*Pz)
beam.addLabel(20, label='B')
beam.addVerticalLoad(15, 3*Pz)
beam.addDistLoadVertical(0, L*0.4, 5*Pz)


# In[39]:


ps.plotBeamDiagram(beam)


# In[40]:


analysis = ps.PyNiteAnalyzer2D(beam)
analysis.runAnalysis()
ps.plotShear(beam)
ps.plotMoment(beam)


# In[ ]:




