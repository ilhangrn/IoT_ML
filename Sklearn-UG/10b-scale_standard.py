# https://www.kaggle.com/discdiver/guide-to-scaling-and-standardizing

# Use MinMaxScaler as your default
# Use RobustScaler if you have outliers and can handle a larger range
# Use StandardScaler if you need normalized features
# Use Normalizer sparingly - it normalizes rows, not columns

import numpy as np 
import pandas as pd 
from sklearn import preprocessing

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# %matplotlib inline
matplotlib.style.use('ggplot')

np.random.seed(7)

#create columns of various distributions
df = pd.DataFrame({ # Dataframe from a dictionary
    'beta': np.random.beta(5, 1, 1000) * 60,        # beta
    'exponential': np.random.exponential(10, 1000), # exponential
    'normal_l': np.random.normal(10, 2, 1000),      # normal leptokurtic 
    'normal_p': np.random.normal(10, 10, 1000),     # normal platykurtic
})
# Create 1000 samples with these distributions

# make bimodal distribution
first_half = np.random.normal(20, 3, 500) 
second_half = np.random.normal(-20, 3, 500) 
bimodal = np.concatenate([first_half, second_half])
# bimodal = np.concatenate([second_half, first_half]) # This is of course the same

df['bimodal'] = bimodal

# create list of column names to use later
col_names = list(df.columns)
print(col_names)

# plot original distribution plot
fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('Original Density estimation plots')

sns.kdeplot(df['beta'], ax=ax1)
sns.kdeplot(df['exponential'], ax=ax1)
sns.kdeplot(df['normal_l'], ax=ax1)
sns.kdeplot(df['normal_p'], ax=ax1)
sns.kdeplot(df['bimodal'], ax=ax1)
# Fit and plot a univariate or bivariate kernel density estimate.
plt.show()

# It's different from the actual distribution, whose histograms are plotted here:
fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('Distribution and denisty estimate')
sns.distplot(df['beta'], ax=ax1)
sns.distplot(df['exponential'], ax=ax1)
sns.distplot(df['normal_l'], ax=ax1)
sns.distplot(df['normal_p'], ax=ax1)
sns.distplot(df['bimodal'], ax=ax1)
plt.show()


print(df.head())
print(df) # Print the "whole" DF
print(df.mean()) # Columns
print(df.describe()) # Count, mean, std, quant

df.plot() # Plot all the DF values
plt.show()

normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values (one million)
df['normal_big'] = normal_big
print(df.normal_big.mean())

# plot original distribution plot with larger value feature
fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('Original Distributions')

sns.kdeplot(df['beta'], ax=ax1)
sns.kdeplot(df['exponential'], ax=ax1)
sns.kdeplot(df['normal_l'], ax=ax1)
sns.kdeplot(df['normal_p'], ax=ax1)
sns.kdeplot(df['bimodal'], ax=ax1)
sns.kdeplot(df['normal_big'], ax=ax1)
plt.show() # A flat island around the value 1,000,000

df.plot() # Only values around one million
plt.show()
print(df.describe())

mm_scaler = preprocessing.MinMaxScaler()
df_mm = mm_scaler.fit_transform(df)
col_names.append('normal_big')
df_mm = pd.DataFrame(df_mm, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After MinMaxScaler')

sns.kdeplot(df_mm['beta'], ax=ax1)
sns.kdeplot(df_mm['exponential'], ax=ax1)
sns.kdeplot(df_mm['normal_l'], ax=ax1)
sns.kdeplot(df_mm['normal_p'], ax=ax1)
sns.kdeplot(df_mm['bimodal'], ax=ax1)
sns.kdeplot(df_mm['normal_big'], ax=ax1)
plt.show()
# Fit and plot a univariate or bivariate kernel density estimate.

# Here are the actual histograms
fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After MinMaxScaler')
sns.distplot(df_mm['beta'], ax=ax1)
sns.distplot(df_mm['exponential'], ax=ax1)
sns.distplot(df_mm['normal_l'], ax=ax1)
sns.distplot(df_mm['normal_p'], ax=ax1)
sns.distplot(df_mm['bimodal'], ax=ax1)
sns.distplot(df_mm['normal_big'], ax=ax1)
plt.show()

mins = [df[col].min() for col in df.columns]
print(mins)
maxs = [df[col].max() for col in df.columns]
print(maxs)
mins = [df_mm[col].min() for col in df_mm.columns]
print(mins)
maxs = [df_mm[col].max() for col in df_mm.columns]
print(maxs)

#######
# RobustScaler
#######
# RobustScaler subtracts the column median and divides by the interquartile range.

r_scaler = preprocessing.RobustScaler()
df_r = r_scaler.fit_transform(df)

df_r = pd.DataFrame(df_r, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After RobustScaler')

sns.kdeplot(df_r['beta'], ax=ax1)
sns.kdeplot(df_r['exponential'], ax=ax1)
sns.kdeplot(df_r['normal_l'], ax=ax1)
sns.kdeplot(df_r['normal_p'], ax=ax1)
sns.kdeplot(df_r['bimodal'], ax=ax1)
sns.kdeplot(df_r['normal_big'], ax=ax1)

plt.show()

mins = [df_r[col].min() for col in df_r.columns]
print(mins)

maxs = [df_r[col].max() for col in df_r.columns]
print(maxs)

# Although the range of values for each feature is much smaller than for the original features,
# it's larger and varies more than for MinMaxScaler.
# The bimodal distribution values are now compressed into two small groups.

######
# StandardScaler
######

# StandardScaler is scales each column to have 0 mean and unit variance.

s_scaler = preprocessing.StandardScaler()
df_s = s_scaler.fit_transform(df)

df_s = pd.DataFrame(df_s, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After StandardScaler')

sns.kdeplot(df_s['beta'], ax=ax1)
sns.kdeplot(df_s['exponential'], ax=ax1)
sns.kdeplot(df_s['normal_l'], ax=ax1)
sns.kdeplot(df_s['normal_p'], ax=ax1)
sns.kdeplot(df_s['bimodal'], ax=ax1)
sns.kdeplot(df_s['normal_big'], ax=ax1)
plt.show()

mins = [df_s[col].min() for col in df_s.columns]
print(mins)
maxs = [df_s[col].max() for col in df_s.columns]
print(maxs)

######
# Normalizer
######

# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html
# Divide each component of a vector by its norm (function used to measure the size of a vector)
# l1, norm is Manhattan distance
# l2, norm Euclidean distance
# max, norm is max component

X = [[4, 1, -2, 2],
     [1, -3, 9, 3],
     [5, 7, 5, -1]]
transformer = preprocessing.Normalizer().fit(X)  # fit does nothing.
print('l2 norm')
print(transformer.transform(X))

X = [[4, 1, -2, 2],
     [1, -3, 9, 3],
     [5, 7, 5, -1]]
transformer = preprocessing.Normalizer(norm='l1').fit(X)  # fit does nothing.
print('l1 norm')
print(transformer.transform(X))

X = [[4, 1, -2, 2],
     [1, -3, 9, 3],
     [5, 7, 5, -1]]
transformer = preprocessing.Normalizer(norm='max').fit(X)  # fit does nothing.
print('max norm')
print(transformer.transform(X)) # Normalized vector has norm 1, of course


n_scaler = preprocessing.Normalizer()
df_n = n_scaler.fit_transform(df)

df_n = pd.DataFrame(df_n, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After Normalizer')

sns.kdeplot(df_n['beta'], ax=ax1)
sns.kdeplot(df_n['exponential'], ax=ax1)
sns.kdeplot(df_n['normal_l'], ax=ax1)
sns.kdeplot(df_n['normal_p'], ax=ax1)
sns.kdeplot(df_n['bimodal'], ax=ax1)
sns.kdeplot(df_n['normal_big'], ax=ax1)

plt.show()

mins = [df_n[col].min() for col in df_s.columns]
print(mins)

maxs = [df_n[col].max() for col in df_s.columns]
print(maxs)

# Transformation brought sample norm equal to 1
# But you usually want to transform the features (columns), not the samples (rows)

# Normalizer also moved the features to similar scales.
# Notice that the range for our much larger feature's values
# is now extremely small and clustered around .9999999999.

#####
# Combined Plot
#####

# Let's look at our original and transformed distributions together.
# We'll exclude Normalizer because you generally want to tranform your features, not your samples.

# Combined plot.

fig, (ax0, ax1, ax2, ax3) = plt.subplots(ncols=4, figsize=(20, 8))


ax0.set_title('Original Distributions')

sns.kdeplot(df['beta'], ax=ax0)
sns.kdeplot(df['exponential'], ax=ax0)
sns.kdeplot(df['normal_l'], ax=ax0)
sns.kdeplot(df['normal_p'], ax=ax0)
sns.kdeplot(df['bimodal'], ax=ax0)
sns.kdeplot(df['normal_big'], ax=ax0)


ax1.set_title('After MinMaxScaler')

sns.kdeplot(df_mm['beta'], ax=ax1)
sns.kdeplot(df_mm['exponential'], ax=ax1)
sns.kdeplot(df_mm['normal_l'], ax=ax1)
sns.kdeplot(df_mm['normal_p'], ax=ax1)
sns.kdeplot(df_mm['bimodal'], ax=ax1)
sns.kdeplot(df_mm['normal_big'], ax=ax1)


ax2.set_title('After RobustScaler')

sns.kdeplot(df_r['beta'], ax=ax2)
sns.kdeplot(df_r['exponential'], ax=ax2)
sns.kdeplot(df_r['normal_l'], ax=ax2)
sns.kdeplot(df_r['normal_p'], ax=ax2)
sns.kdeplot(df_r['bimodal'], ax=ax2)
sns.kdeplot(df_r['normal_big'], ax=ax2)


ax3.set_title('After StandardScaler')

sns.kdeplot(df_s['beta'], ax=ax3)
sns.kdeplot(df_s['exponential'], ax=ax3)
sns.kdeplot(df_s['normal_l'], ax=ax3)
sns.kdeplot(df_s['normal_p'], ax=ax3)
sns.kdeplot(df_s['bimodal'], ax=ax3)
sns.kdeplot(df_s['normal_big'], ax=ax3)

plt.show()

# You can see that after any transformation the distributions are on a similar scale.
# Also notice that MinMaxScaler doesn't distort the distances between the values in each feature.