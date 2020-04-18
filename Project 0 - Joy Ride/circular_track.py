#!/usr/bin/env python
# coding: utf-8

# # Joy Ride - Part 2: Circular Track
# 
# In this part, you'll write code to steer a car around a circular track. In doing so you'll explore the relationship between steering angle and turning radius. To get started:
# 
# 1. Run the cell below this one by pressing `Ctrl + Enter`
# 1. The simulator will appear below the cell.
# 1. Run the cell below the simulator, marked `CODE CELL` (hit `Ctrl + Enter`). The car in the simulator should start moving. You should notice a problem...
# 1. Press the **Reset** button in the simulator and then modify the code in the `CODE CELL` as per instruction in TODO comment.
# 1. When you think you've fixed the problem, run the code cell again. 
# 
# #### NOTE - depending on your computer it may take a few minutes for the simulator to load! Please be patient.
# 

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<script src="setupLauncher.js"></script><div id="simulator_frame"></sim>')


# In[7]:


# CODE CELL
#
# This is the code you should edit and run to control the car.

from Car import Car
import time

# TODO: Make changes to the steering and gas values and see how they affect the car's motion
def circle(car):
    car.steer(4)
    car.gas(0.2)
    
car = Car()

circle(car)

