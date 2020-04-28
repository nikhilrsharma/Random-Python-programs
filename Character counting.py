# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:34:07 2020

@author: Public
"""

sentence = "i am like this only"
count={}
for char in sentence:
    if char not in count:
        count[char]=1
    else:
        count[char]+=1

print('Method-1:')
print(count)


count={}
for char in sentence:
    count.setdefault(char,0)
    count[char]+=1

print('Method-2:')
print(count)