# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:23:55 2020

@author: vikas chaudhari
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def values(subjects,s,y,col):
    x=np.arange(0,s)
    plt.xticks(x,subjects)
    
    plt.xlabel('Subjects')
    plt.ylabel('marks obtained')
    plt.bar(x,y,color=col)


subjects=[]
y=[]
print('enter the number of subjects you have')
s=int(input())
i=0
while i<s:
    print('enter the name of the  subject')
    su=str(input())
    subjects.append(su)
    i=i+1
i=0
print('enter the marks according to the sequence of the name of the subjects')
while i<s:
    print('enter marks')
    m=int(input())
    y.append(m)
    i=i+1
    

col=str(input(print(f'enter the colour for  plot')))
values(subjects,s,y,col)
