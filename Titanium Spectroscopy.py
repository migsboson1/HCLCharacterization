#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt


# In[35]:



wave,voltage = np.loadtxt('Ti_spec', unpack = True)
wave_cal = wave - 95

max_amp = max(voltage[350:450])

for i in range(len(wave)):
    if voltage[i] == max_amp:
        print(voltage[i])
        print(i)
        print(wave_cal[i])


plt.figure(figsize = (15,15))
plt.plot(wave_cal[500:1000] ,voltage[500:1000],'b-' )
plt.show()


# In[32]:


# Need to analyze the data. Resolution was at .1A for these recorded runs.
# 
wave_400, amp_400 = np.loadtxt('Ti400nm', unpack = True)

wv_400 = wave_400 - 95
plt.figure(figsize = (10,10))
plt.plot(wv_400[2500:2800], amp_400[2500:2800], 'k-')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Voltage (volts)')
plt.show()


wv_400 = wave_400 - 95
plt.figure(figsize = (10,10))
plt.plot(wv_400, amp_400, 'k-')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Voltage (volts)')
plt.show()

max_amp = max(amp_400[2500:2800])

for i in range(len(wv_400)):
    if amp_400[i] == max_amp:
        print(i)
        print('wavelength is:', wv_400[i])
        print('amplitude is:', amp_400[i])

    


# In[ ]:




