# -*- coding: utf-8 -*-
"""
Created on Fri July 19 17:41:37 2024

@author: Gerardo Casanola
"""


#%% Importing libraries

from pathlib import Path
import pandas as pd
import pickle
from molvs import Standardizer
from rdkit import Chem
from openbabel import openbabel
from mordred import Calculator, descriptors
from multiprocessing import freeze_support
import numpy as np
from rdkit.Chem import AllChem
import plotly.graph_objects as go
import networkx as nx

#Import Libraries
import math 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error

# packages for streamlit
import streamlit as st
from PIL import Image
import io
import base64
import tqdm


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
  st.write('RU:',choice)
  
  # Perform the concatenation for the specified number of iterations
 
  # Initialize the final string with the left end
  end_ru = DM * ratio_rep_unit
  f_ru = ''

   # Depending on the choice, add the string DP or PM at the end of f_ru after each iteration
  if choice == 'PM':
    for i in range(num_it):
       #Add the DM string ratio_DM times
       f_ru += DM * ratio_rep_unit
       f_ru += PM
    
     
  if choice == 'DP':
      for i in range(num_it):  
        #Add the DM string ratio_DM times
        f_ru += DM * ratio_rep_unit
        f_ru += DP
  
  n_ru=f_ru+end_ru

  si_oil=left_end+n_ru+right_end
  
  # Print the final string
  #st.write(si_oil)

 # Remove the patterns
  si_oil_final = si_oil.replace('**', '').replace('I*', '')
  st.write(si_oil_final)

if st.button('Press to see the pattern for the assembled silicon oil'):
  Number_Rep_Unit_2 = round(percent / 100 * degree_of_polymerization)
  
  # Perform the division and get the integer quotient and remainder
  Number_Rep_Unit_1 = degree_of_polymerization - Number_Rep_Unit_2 -2   # Assuming a value for DiMethyl for the code to run
  ratio_rep_unit, remainder = divmod(Number_Rep_Unit_1, Number_Rep_Unit_2 + 1)
  num_it = Number_Rep_Unit_2
  
  num_1=1
  name_left_end= '3MSi0'
  name_right_end='-Si3M'
  name_dm = f'-[DM({ratio_rep_unit})]'
  name_pm = f'-[PM({num_1})]'
  name_dp = f'-[DP({num_1})]'
  # Specify the number of times to repeat the pattern
  num_repeats = num_it  # For example, repeat the pattern 5 times
  
  if choice == 'DP':
    # Construct the pattern
    pattern = f'{name_dm}{name_dp}' * num_repeats

  if choice == 'PM':
    # Construct the pattern
    pattern = f'{name_dm}{name_pm}' * num_repeats

  # Print the pattern along with left and right ends
  
  st.write(f'{name_left_end}{pattern}{name_dm}{name_right_end}')

#mol = Chem.MolFromSmiles(si_oil_final)

def smiles_to_mol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())
        return mol
    else:
        return None

def save_mol_file(mol, filename):
    writer = Chem.SDWriter(filename)
    writer.write(mol)
    writer.close()

# Convert SMILES to mol
mol = smiles_to_mol(si_oil_final)

# Save as a mol file
save_filename = "output.mol"
save_mol_file(mol, save_filename)
