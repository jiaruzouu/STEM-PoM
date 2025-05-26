import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
# Importing the HTTP library
import requests as req
from tqdm import tqdm
#from extract import filename 
import os 
data = pd.read_csv('/home/jiaruz2/extract/MDTE.csv')
txt = data["context"]


# Specify the CSV file name and column name
column_name = 'Source'

for i in range(len(txt)):
    with open('/home/jiaruz2/extract/test.out', 'r') as fp:
        lines = fp.readlines()
        string = txt[i]
        for line in lines:
            if line.find(string) != -1 and line.find(':string exists in file') != -1:
                filename_linenumber  = lines.index(line) + 4
                #print(lines[filename_linenumber])
                filename = lines[filename_linenumber]
                filename = filename.split('.htmloutput')[0]
                # Add the new element to the specific block of the column
                data.loc[i, column_name] = str(data.loc[i, column_name])
                if data.loc[i, column_name].find(filename) == -1:
                    data.loc[i, column_name] += ' | ' + filename
                # Save the updated DataFrame to a CSV file
                data.to_csv('/home/jiaruz2/extract/MDTE.csv', index=False)




# select rows where the value in the third column is not empty
selected_rows = data[data.iloc[:, -1].notna()]
# write the selected rows to a new CSV file
selected_rows.to_csv('MDTE_contain_source_1.csv', index=False)

