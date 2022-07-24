#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 19:47:03 2022

@author: kruttikasoni
"""

import streamlit as st
import numpy as np
import pandas as pd

st.write('''
         Subtraction of two numbers
         ''')
#get input 
st.header("User Input Parameters")

def user_input_features():
    number_1 = st.number_input('A',step=1)
    number_2 = st.number_input('B',step=1)
    
    data={'A': a,
          'B':b
          }
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(st.to_dict())

#usecase working

output = a-b

st.write('Answer:')
st.write(output)

!pip requirements.txt
