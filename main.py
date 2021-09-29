# import pandas as pd
# import os
# df1 = pd.read_excel(
#      os.path.join("inventum.xlsx"),
#      engine='openpyxl',
# )



# print(df1)

import csv
from os import pardir, sep
import pandas as pd
import openpyxl

# Read Excel File
read_file = pd.read_excel("inventum.xlsx")
# Create CSV file with all data
read_file.to_csv("sample.csv" , index=None , header=True)

# Read Specific column
col_list = ['Order Date' , 'Sales']
df = pd.read_csv("sample.csv" , usecols=col_list)

# Print Two Columns in command
asd=df.sort_values("Order Date")
print(asd)
# df['Order Date'] = pd.to_datetime(df['Order Date'])
# max_date = df['Order Date'].max()
# print(max_date)

# Create new CSV file with only two column 
try:
    with open("new.csv" , "r") as new_csv:
        if new_csv:
            readcsv = pd.read_csv("new.csv" , usecols=col_list)
            print(readcsv) 
except:
    df.to_csv("new.csv" , sep=',' , )
    df.df.sort_values('order Date')
    