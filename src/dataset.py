import pandas as pd
import numpy as np

first_year = 2000
last_year = 2013

def read_input(filename):
    # Receive input from filename.csv and return the panda time series
    dataset = pd.read_csv(filename, sep=';')
    datagroup = dataset.groupby(['CIDADE', 'NU_ANO', 'SEM_NOT'])
    series = datagroup.size()
    return series
