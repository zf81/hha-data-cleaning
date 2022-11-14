# hha-data-cleaning
HHA 507 Assignment 2 

1. For step 1, loaded the csv data file into python using "df=pd.read_csv" function 
2. Using "df.shape" printed out the total counts of both columns and rows 
3. Using "df.columns" printed out the column names  
4. Begin data cleaning: Cleaning the column names and column strings. 
5. Used "df.rename" to assess white spaces or special characters within each column. Converted the column types to the correct types 
6. Can use "df.dftypes" to ensure all columns consist of correct data types 
7. Use "df.duplicated" to see if there are any duplicate rows, then proceed to next step 
8. Use "df.isnull" to assess missingness. Column titled "Student count" had null on line 23.
9. Use "df.fillna" to put in value of 0  
10. Create a new column named modality_inperson. Used function label_modalityinperson. If learning_modality is entered as in person, then label_modality_inperson will return as "True." If learning_modality entered is remote or hybrid, then label_modality_inperson will return "False."
