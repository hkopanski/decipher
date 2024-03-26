# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:05:01 2024

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

be_nice_pt = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7
play_fair_pt = row_8 + row_9 + row_10 + row_11 + row_12 + row_13 + row_14 + row_15 + row_16

letter_freq = []
letter_list = []
letter_dict = {}

for i in string.ascii_lowercase:
    letter_freq.append(be_nice_pt.count(i))
    letter_list.append(i)
    letter_dict[i] = be_nice_pt.count(i)
    
df_freq = pd.Series(letter_dict)
df_freq = df_freq.rename('Count', axis = 'columns')
    
fig = plt.figure(figsize = (10, 5), dpi = 200)

df_freq.sort_values(ascending=True).plot.barh()

cipher_text_freq = df_freq.sort_values(ascending = False)


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
    two_letter_count.append(be_nice_pt.count(i))
    
for i in three_letter_seq:
    three_letter_count.append(be_nice_pt.count(i))
    
two_letter_info = pd.DataFrame({'Combo': two_letter_seq, 'Count': two_letter_count})
three_letter_info = pd.DataFrame({'Combo': three_letter_seq, 'Count': three_letter_count})

