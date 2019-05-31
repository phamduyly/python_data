# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import pandas_profiling
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("Metro_Interstate_Traffic_Volume.csv") 
# Preview the first 5 lines of the loaded data 

print(data.describe())
print(data.isnull().any())
print(data.info())
