#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
#streamlit run C:\Users\gmaikelc\anaconda3\Lib\site-packages\ipykernel_launcher.py

# Create a layout with 3 columns
col1, col2, col3 = st.columns(3)

# Input for 'Degree of polymerization'
degree_of_polymerization = col1.number_input('Degree of polymerization', min_value=0)

# Input for 'Percent'
percent = col2.number_input('Percent', min_value=0, max_value=100)

# Dropdown for 'PM' and 'DP'
options = ['PM', 'DP']
choice = col3.selectbox('Choose an option', options)

st.write(f"You entered {degree_of_polymerization} for Degree of polymerization, {percent}% for Percent, and selected {choice} from the dropdown.")

# Define the strings
DM = '*[Si](C)(C)OI'
DP = '*[Si](c1ccccc1)(c1ccccc1)OI'
PM = '*[Si](c1ccccc1)(C)OI'
left_end = 'C[Si](C)(C)O*'
right_end = '*[Si](C)(C)C'
additional_string = 'ICCC*'

if st.button('Press to generate the silicon oil structure based on the parameters'):
  # Calculate Number_Rep_Unit_2
  Number_Rep_Unit_2 = round(percent / 100 * degree_of_polymerization)
  st.write('Number of repeating units:',Number_Rep_Unit_2)

  # Perform the division and get the integer quotient and remainder
  Number_Rep_Unit_1 = degree_of_polymerization - Number_Rep_Unit_2 -2   # Assuming a value for DiMethyl for the code to run
  ratio_rep_unit, remainder = divmod(Number_Rep_Unit_1, Number_Rep_Unit_2 + 1)

  # Print the results
  st.write("Ratio (Integer part):", ratio_rep_unit)
  st.write("Remainder:", remainder)

  # Number of iterations
  num_it = Number_Rep_Unit_2
  st.write('Number of iterations:', num_it)

  
  # Perform the concatenation for the specified number of iterations
 
  # Initialize the final string with the left end
  end_ru = DM*ratio_rep_unit
  f_ru =''
  for i in range(num_it):
      # Add the DM string ratio_DM times
      f_ru += DM * ratio_rep_unit
      if choice=='DP':
        f_ru+=DP
      elif choice=='PM':
        f_ru+=PM

  n_ru=f_ru+end_ru

  si_oil=left_end+n_ru+right_end
  
  # Print the final string
  st.write(si_oil)
