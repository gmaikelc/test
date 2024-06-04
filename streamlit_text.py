#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
#streamlit run C:\Users\gmaikelc\anaconda3\Lib\site-packages\ipykernel_launcher.py
# Create a layout with 3 columns
#col1, col2, col3 = st.beta_columns(3)


# Input for 'Degree of polymerization'
degree_of_polymerization = col1.number_input('Degree of polymerization', min_value=0)





# Input for 'Percent'
percent = col2.number_input('Percent', min_value=0, max_value=100)

# Dropdown for 'PM' and 'DP'
options = ['PM', 'DP']
choice = col3.selectbox('Choose an option', options)

st.write(f"You entered {degree_of_polymerization} for Degree of polymerization, {percent}% for Percent, and selected {choice} from the dropdown.")


