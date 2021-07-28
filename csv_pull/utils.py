# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:58:52 2021

@author: ebenezer.an
"""

import pandas as pd 
import numpy as np
import string


def transform_data(d_frame):
    data_pivot = pd.pivot_table(d_frame, values=['length'], index=['user_id'], columns=['path'], aggfunc=np.sum, fill_value=0)
    data_pivot.reset_index(level=data_pivot.index.names, inplace=True)        
    data_pivot.columns = data_pivot.columns.map(lambda x: (x[1] + " " + x[0].replace('length', '')).strip() if x[1] != '' else (x[0].replace('length', '')).strip())

    return data_pivot


def pull_files(path):
    lowercase_letters = list(string.ascii_lowercase)
    dataframe = pd.DataFrame()

    for letter in lowercase_letters:
        data = pd.read_csv(path + letter + '.csv')
        dataframe = pd.concat([dataframe, data], sort = False, ignore_index=True)            
        print('Pulling file: ' + letter + '.csv')

    return dataframe

def create_csv(pivot, file_name):
    pivot.to_csv(file_name, index = False)
    
    
