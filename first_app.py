# Import statements

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
# st.image('images/boxcox_beforeafter.png')
st.write(
    'Power transformers are type of data tranformation which can be used to make your data appear more gaussian-like')

st.write('## Preparing the data',
         'In theme of being transparent, I am going to walk you through my EDA for this project')
st.write(
    'In theme of being transparent, I am going to walk you through my EDA for this project... this writing widgeting blows.')

st.write(
    '''
    -   test 
        -   test
    '''
)

# Load the Data
df = pd.read_csv('./data/train.csv')
df.columns = map(str.lower, df.columns)
correct_columns = []
for entry in df.columns:
    new_entry = entry.replace(" ", "-")
    correct_columns.append(new_entry)

print(correct_columns)

# replace column whitespace with dash
df.columns = correct_columns

df['garage-area']

# Checking for Nulls / EDA
nulls = df['garage-area'].isnull().sum()
st.write('The numbers of nulls: %d' % (nulls))

# Replace the null with a 0
df['garage-area'] = df['garage-area'].replace(np.nan, 0)
nulls = df['garage-area'].isnull().sum()
print(f'The numbers of nulls:{nulls}')

# Drop Zeros from the pd.series (if zero we can assume that a garage is not around)
garage_area = df['garage-area']
garage_area = garage_area[garage_area != 0]

# Plot a histogram of the data
ax = sns.displot(garage_area, kde=True)
ax.set(xlabel='Garage Area (ft^2)', ylabel='Counts', title='Frequency of Garage Sizes (ft²)')
st.pyplot(ax)

st.write('Lets explore the effect of lambda on the data')
st.write('Choose a value for lambda below:')

# Alt graph version

# ax = sns.kdeplot(garage_area, shade=True)
# ax.set(xlabel='Garage Area (ft^2)', ylabel='Counts', title='Frequency of Garage Sizes (ft²)')
# st.pyplot(ax)

lambda_value_input = st.slider(label='Lambda',
                               max_value=1.0,
                               min_value=-1.0,
                               value=0.5,
                               step=.1)

print(lambda_value_input)

# Calculating Values in the Box-Cox Transformation
# xt = (x**lambda - 1) / lambda

# define the set of lambda's that we want to search over
# lmbda = [0.1, 1.5]

garage_area_xt = []

for value in garage_area:
    # box-cox transformation
    transform = (value ** lambda_value_input) / lambda_value_input
    garage_area_xt.append(transform)


# for i in lambda_value_input:
#     # x = the input data
#     x = garage_area
#     # box-cox transformation
#     transform = (x ** i - 1) / i
#     # appending the list
#     garage_area_xt.append(transform)

ax = sns.displot(garage_area_xt, kde=True)
ax.set(xlabel='Garage Area (ft^2)', ylabel='Counts', title='Frequency of Garage Sizes (ft²), Lambda: %f' % (lambda_value_input))
st.pyplot(ax)

st.write('As you can see in the above histograms, the scale of lambda greatly effects the resultant distribution of the feature.'
         'Because the distributions are now on different scales it is difficult to compare them. A good strategy, the default '
         'in sklearn’s power transformer module, is to **standardize** the data before you transform it.')

st.write('### Visualizing Changes')

with st.echo():
    garage_area_zscore = stats.zscore(garage_area) #z-score normalization
    garage_area_lbmd1 = stats.yeojohnson(garage_area_zscore, lmbda=lambda_value_input)
    garage_area_lbmd2 = stats.yeojohnson(garage_area_zscore, lmbda=1.5)
    garage_area_lbmd3, lmbda = stats.yeojohnson(garage_area_zscore) #if you don't use lmbda it will find the optimal lambda






