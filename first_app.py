#Import statements

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import PowerTransformer
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Power Transformers (Box-Cox Transformation and Yeo-Johnson Transformations')
st.write('**By: Patrick L. Cavins, PhD**')
st.write('## Getting Started')
st.write('### What are power transformers?')
st.image('./sklearn_powertransform/boxcox_beforeafter.png')
st.write('As you can see in the image ab')

#Load the Data
df = pd.read_csv('train.csv')

df

# #Checking for Nulls / EDA
# nulls = df[‘Garage Area’].isnull().sum()
# print (f’The numbers of nulls: {nulls}’)
#
# #Replace the Null with 0
# df[‘Garage Area’] = df[‘Garage Area’].replace(np.nan, 0)
# nulls = df[‘Garage Area’].isnull().sum()
# print (f’The numbers of nulls: {nulls}’)
#
# #Drop Zeros from the pd.series (if zero we can assume that a garage is not around)
# garage_area = df[‘Garage Area’]
# garage_area = garage_area[garage_area != 0]
#
# #Plot a histogram of the data
# ax=sns.displot(garage_area, kde=True)
# ax.set(xlabel='Garage Area (ft^2)', ylabel='Counts')
# title=’Frequency of Garage Sizes (ft²)’)
# plt.show()