import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('ola_dataset.csv')

# print(df.isnull().sum())

# print(df.drop(columns=['Unnamed: 20'], inplace=True))
# print(df['Payment_Method'].fillna('Not Applicable', inplace=True))
# print(df['Driver_Ratings'].fillna(df['Driver_Ratings'].mean(), inplace=True))
# print(df['Customer_Rating'].fillna(df['Customer_Rating'].mean(), inplace=True))

num_cols = df.select_dtypes(include=np.number).columns

for col in num_cols:
    print(df[col].fillna(df[col].median(), inplace=True))
    
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
    print(df[col].fillna(df[col].mode()[0], inplace=True))
# Show info 
print("\nDataset Info After Handling Missing Values:")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(df.isnull().sum())
# save cleaned data
df.to_csv('ola_dataset_cleaned.csv', index=False)
