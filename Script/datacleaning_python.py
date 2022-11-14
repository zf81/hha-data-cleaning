import pandas as pd
import datetime as dt
import uuid
import numpy as np

# 1. Load data titled School Learning Modalities csv file into python 
df = pd.read_csv("data/School_Learning_Modalities.csv")

# 2. Print the counts of columns and rows 
print(df.shape)

# 3. Providing print out of column names 
print(df.columns)

# 4. Cleaning the column names #
# First, clean the strings that might exist within each column 
df.rename(columns={'District NCES ID' :' district_nes_id','District Name': 'district_name','Learning Modality': 'learning_modality', 'Operational Schools': 'operational_schools', 'Student Count': 'student_count', 'ZIP Code':'zip_code', 'City' : 'city', 'State':'state', 'Week':'week'}, inplace=True)
print(df.columns)

# 5. Assessing white space or special characters #
# Convert the column types to the correct types 
print(df.dtypes)

# 7. Remove any duplicate rows 
print(len(df[df.duplicated()])) 

# 8. Assess any missing values per column 
print(df[df.isnull().any(axis=1)])
print(df.loc[:, df.isnull().any()])
df.fillna(value=0, inplace=True)
print(df[df.isnull().any(axis=1)])

# 9. Create column titled modality_inperson and attempted function 
def label_modality_ineperson(row):
    if row['learning_modality'] == 'In Person':
        return True
    if row['learning_modality'] == 'Remote':
        return False
    if row['learning_modality'] == 'Hybrid':
        return False
df['modality_inperson']=df.apply (lambda row: label_modality_ineperson(row),axis =1)
print(df.columns)
print(df['modality_inperson'])
