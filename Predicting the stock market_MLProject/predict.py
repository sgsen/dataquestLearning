import pandas as pd
from datetime import datetime 
import numpy as np

# read in the df

data = pd.read_csv('sphist.csv')

# cleaning

data.Date = pd.to_datetime(data.Date)

data = data.sort_values('Date')

print(data.head())

## trailing average function

def trailing_five(row):
    row