#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
#streamlit run C:\Users\gmaikelc\anaconda3\Lib\site-packages\ipykernel_launcher.py

# Input for 'Degree of polymerization'
degree_of_polymerization = st.number_input('Degree of polymerization', min_value=0)

# Input for 'Percent'
percent = st.number_input('Percent', min_value=0, max_value=100)

# Dropdown for 'PM' and 'DP'
options = ['PM', 'DP']
choice = st.selectbox('Choose an option', options)

st.write(f"You entered {degree_of_polymerization} for Degree of polymerization, {percent}% for Percent, and selected {choice} from the dropdown.")

