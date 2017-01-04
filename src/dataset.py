# -*- coding: latin-1 -*-
import pandas as pd
import numpy as np

first_year = 2000
last_year = 2013

def read_raw_input(filename):
    # Receive the raw input from filename.csv and return the panda time series
    dataset = pd.read_csv(filename, sep=';', encoding='latin-1')

    labels = dataset.keys()
    city_label = labels[0]
    cities = dataset[city_label]
    weeks_str = labels[1:]
    weeks_int = weeks_str.map(int)
    years = np.unique(np.floor(weeks_int/100))

    matrix = np.empty((0, 52))
    tuples_cityear = []
    for cityI in range(len(cities)):
        for year in years:
            tuples_cityear.append((cities[cityI],str(int(year)))) # index
            notified = []
            for week in weeks_int:
                if (week >= year * 100 and week < (year + 1) * 100):
                    notified.append(dataset.get_value(cityI, str(week)))
            if len(notified) > 52:
                notified = notified[:52] # limit the amount of weeks in a year to 52
            matrix = np.vstack((matrix, notified))
            
    index = pd.MultiIndex.from_tuples(tuples_cityear, names=['Cidade', 'Ano'])
    series = pd.DataFrame(matrix, index=index)
    series = series.T.unstack()
    return series

def read_frequency_input(filename):
    # Receive the frequency input from filename.csv and return the panda time series
    df = pd.read_csv(filename, sep=';')
    dataset = df.set_index(["Cidade", "Ano"])
    series = dataset.T.unstack()
    return series

def read_population(filename):
    # Receive the file with the cities and number of inhabitants
    d = {}
    with open(filename, encoding="latin-1") as f:
        for line in f:
            (key, val) = line.split(";")
            d[key] = int(val)
    return d

def weight_population(dataset, population):
    # Function that receives a dataset of the disease and the population of each city
    # and returns a disease frequency series, weighted by the population of each city
    cities = dataset.index.levels[0]
    for city in cities:
        dataset.T[city] = dataset.T[city]/population[city]
    return dataset

