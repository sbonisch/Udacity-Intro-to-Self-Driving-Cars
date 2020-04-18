#!/usr/bin/env python
# coding: utf-8

# # Joy Ride - Part 1: Drag Race
# 
# The goal here is to get you familiar with how to control the simulated car with code. To get started:
# 
# 1. Run the cell below this one by pressing `Ctrl + Enter`
# 1. The simulator will appear below the cell.
# 1. Run the cell below the simulator, marked `CODE CELL` (hit `Ctrl + Enter`). The car in the simulator should start moving. You should notice a problem...
# 1. Press the **Reset** button in the simulator and then modify the code in the code cell. You should only need to change one line of code...
# 1. When you think you've fixed the problem, run the code cell again. Did the car make it over the trees?
# 
# #### NOTE - depending on your computer it may take a few minutes for the simulator to load! Please be patient.

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<script src="setupLauncher.js"></script><div id="simulator_frame"></sim>')


# In[9]:


# CODE CELL
# 
# This is the code you should 
# edit and run to control the car.

from Car import Car # you don't need to change this line of code...
import time

def jump(car):
    # TODO - make modifications in this function
    #   so that your car makes it safely over the trees.
    time.sleep(2)
    
    car.steer(0.0) # any value between -25 and 25 works here for
                   # steering angle (in degrees)
        
    car.gas(0.9)   # any value between -1.0 (full reverse) and 
                   # 1.0 (full throttle) works here
        
    
car = Car()  
jump(car)


# In[ ]:




