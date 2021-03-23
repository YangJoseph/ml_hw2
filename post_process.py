# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 01:37:40 2021

@author: User
"""

import csv
import numpy as np


path = 'prediction.csv'
with open(path, 'r') as f:
    reader = csv.reader(f)
    data = np.array(list(reader))
datax = data[1:,1:]
datay = []
for i in range(len(datax)):
    num = int(datax[i])
    datay.append(num)


count = 0
#print(datay)
#data = list(csv.reader(f))
#data = np.array(data[1:])[:, 1:].astype(float)
#datax = np.transpose(data)

#for i in range(len(datay)):
#    datax.append(data[i])

fix  = []
fix_num = []
fix_before = []

for i in range(len(datay)-4):
    if datay[i]==datay[i+1]==datay[i+3]==datay[i+4] and datay[i+2]!=datay[i]:
        fix_before.append(datay[i+2])
        datay[i+2]=datay[i]
        fix.append(i)
        fix_num.append(datay[i])
        count = count + 1

print(datay)
print(count)
print(fix)
print(fix_num)
print(fix_before)
#count = 0
#for i in range(451552):
#    print(datax[i])
#print(count)

with open('predictionx.csv', 'w') as f:
    f.write('Id,Class\n')
    for i, y in enumerate(datay):
        f.write('{},{}\n'.format(i, y))