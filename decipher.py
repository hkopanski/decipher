# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:09:58 2024

@author: hkopansk
"""

import hashlib
import numpy as np
import pandas as pd
import os
import string
import itertools

import matplotlib.pyplot as plt 

os.chdir(r"C:\Users\hkopansk\OneDrive - Biogen\Documents\Python Data")

print(hashlib.sha512('halid'.encode()).hexdigest())

row_1 =  'tvbscnrwdlrnlgpf'
row_2 =  'adnfbnrucbqprnoi'
row_3 =  'pbshfrcavqsnhpad'
row_4 =  'imrhlxebipkrcnbc'
row_5 =  'gtzarsirbospavql'
row_6 =  'pxtqmiahsrbaqowo'
row_7 =  'pbwncnvcqrrszpnr'
row_8 =  'sriernndxcadpmny'
row_9 =  'ebnpocpbvascaest'
row_10 = 'srcaxsrierangmse'
row_11 = 'rmtvsntfbargqlcn'
row_12 = 'btpupbvaqmsnecoq'
row_13 = 'srtvsnirzpipblah'
row_14 = 'apqrhtaqxlglclco'
row_15 = 'pqhagaqorpaepksn'
row_16 = 'tfqhwpbalivrbnsn'


full_string = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8 + row_9 + row_10 + row_11 + row_12 +row_13 + row_14 + row_15 + row_16


cipher_block = np.row_stack([row_1, row_2, row_3, row_4, row_5, row_6,
                             row_7, row_8, row_9, row_10, row_11, row_12,
                             row_13, row_14, row_15, row_16])

block_flat = ''

for i in cipher_block:
    for j in i: 
        block_flat = block_flat + j
        
number_block = np.zeros(16*16)

for i in range(len(full_string)):
    number_block[i] = ord(full_string[i])-96

number_block = number_block.reshape(16,16)

print(number_block)

number_block.tofile('number_block.csv', sep=',')

for i in list(string.ascii_lowercase):
    print([i, full_string.count(i)])

letter_block = []

for i in range(len(full_string)):
    letter_block.append(full_string[i])
    
letter_array = np.array(letter_block).reshape(16,16)
print(letter_array)
print(letter_array.T)

two_letter_seq = []
two_letter_count = []
three_letter_seq = []
three_letter_count = []

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        two_letter_seq.append(i + j)
        
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        for k in string.ascii_lowercase:
            three_letter_seq.append(i + j + k)
            
for i in two_letter_seq:
    two_letter_count.append(full_string.count(i))
    
for i in three_letter_seq:
    three_letter_count.append(full_string.count(i))
    
two_letter_info = np.array([two_letter_seq, two_letter_count]).T
three_letter_info = np.array([three_letter_seq, three_letter_count]).T


letter_freq = []
letter_list = []
letter_dict = {}

for i in string.ascii_lowercase:
    letter_freq.append(full_string.count(i))
    letter_list.append(i)
    letter_dict[i] = full_string.count(i)
    
df_freq = pd.Series(letter_dict)
df_freq = df_freq.rename('Count', axis = 'columns')
    
fig = plt.figure(figsize = (10, 5), dpi = 200)

df_freq.sort_values(ascending=True).plot.barh()

cipher_text_freq = df_freq.sort_values(ascending = False)


row_1p = row_1[0:5]

def new_parse(n):
    return lambda x: x[0] == n

seq_brute = []
    
for i in range(len(row_1p)):
    temp_func = new_parse(row_1p[i])
    for j in range(len(two_letter_seq)):
        if temp_func(two_letter_seq[j]) == True:
            seq_brute.append(two_letter_seq[j])
    
    
be_nice_pt = sum(row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8)
play_fair_pt = sum(row_9 + row_10 + row_11 + row_12 + row_13 + row_14 + row_15 + row_16)