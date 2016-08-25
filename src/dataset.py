import pandas as pd
import numpy as np

first_year = 2000
last_year = 2013

def read_raw_input(filename):
    # Receive the raw input from filename.csv and return the panda time series
    dataset = pd.read_csv(filename, sep=';')
    datagroup = dataset.groupby(['CIDADE', 'NU_ANO', 'SEM_NOT'])
    series = datagroup.size()
    return series

def read_frequency_input(filename):
    # Receive the frequency input from filename.csv and return the panda time series
    pass

def read_population(filename):
    # Receive the file with the cities and number of inhabitants
    d = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d

def weight_population(dataset, population):
    # Function that receives a dataset of the disease and the population of each city
    # and returns a disease frequency series, weighted by the population of each city
    pass
