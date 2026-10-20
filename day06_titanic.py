import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types and non-null values:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())
