# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:20:47 2021

@author: Claw
"""
import matplotlib.pyplot as plt
from numpy import random

d1 = 0
d2 = 0
dt = 0
call = 0
rolls = 100

result = []
index = []

for i in range (11):
    result.append(0)
    index.append(i+2)

for i in range (100000):
    d1 = random.randint(1,7)
#    print("d1 = ",d1)
    d2 = random.randint(1,7)
#    print("d2 = ",d2)
    dt = d1 + d2
#    print("dt = ",dt)
    call = dt - 2
#    print("call = ",call)
    result[call] = result[call] + 1
#    print(result)
 
   
for i in range (11):
   print(i+2," was rolled ",result[i])

  
# x-coordinates of left sides of bars 
left = index
  
# heights of bars
height = result
  
# labels for bars
tick_label = result
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8)
  
# naming the x-axis
plt.xlabel('Value')
# naming the y-axis
plt.ylabel('Outcome')
# plot title
plt.title('Rolls')
  
# function to show the plot
plt.show()