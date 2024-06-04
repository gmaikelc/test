#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
#streamlit run C:\Users\gmaikelc\anaconda3\Lib\site-packages\ipykernel_launcher.py

# Input for 'Degree of polymerization'
#degree_of_polymerization = st.number_input('Degree of polymerization', min_value=0)


# Create a layout with 3 columns
col1, col2, col3 = st.beta_columns(3)

# Use the middle column for the input box
degree_of_polymerization = col2.number_input('Degree of polymerization', min_value=0)

# Input for 'Percent'
percent = st.number_input('Percent', min_value=0, max_value=100)

# Dropdown for 'PM' and 'DP'
options = ['PM', 'DP']
choice = st.selectbox('Choose an option', options)

st.write(f"You entered {degree_of_polymerization} for Degree of polymerization, {percent}% for Percent, and selected {choice} from the dropdown.")

# Given values
Degree_Polymerization = 35
Percent_PhenylMethyl = 10

# Calculate Phenyl_Metyl
Phenyl_Metyl = round(Percent_PhenylMethyl / 100 * Degree_Polymerization)
print('Number of PM repeating units:',Phenyl_Metyl)

# Perform the division and get the integer quotient and remainder
DiMethyl = Degree_Polymerization - Phenyl_Metyl -2   # Assuming a value for DiMethyl for the code to run
ratio_DM, remainder = divmod(DiMethyl, Phenyl_Metyl + 1)

# Print the results
print("Ratio (Integer part):", ratio_DM)
print("Remainder:", remainder)

# Number of iterations
num_it = Phenyl_Metyl
print('Number of iterations:', num_it)

# Define the strings
DM = '*[Si](C)(C)OI'
DP = '*[Si](c1ccccc1)(c1ccccc1)OI'
PM = '*[Si](c1ccccc1)(C)OI'
left_end = 'C[Si](C)(C)O*'
right_end = '*[Si](C)(C)C'
additional_string = 'ICCC*'

# Perform the concatenation for the specified number of iterations
# Perform the concatenation for the specified number of iterations
# Initialize the final string with the left end
end_ru = DM*ratio_DM
f_ru =''
for i in range(num_it):
    # Add the DM string ratio_DM times
    f_ru += DM * ratio_DM
    f_ru+=DP

n_ru=f_ru+end_ru

si_oil=left_end+n_ru+right_end
  
# Add the right end to the final string
#final_string += right_end

# Print the final string
print(si_oil)

