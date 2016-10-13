import scipy.stats as sp
import numpy as np

def pearson_correlation(time_series1, time_series2, delay=0):
    # Pearson correlation of the disease frequency in time_series1 and time_series2    
    if delay > 0:
        x = time_series1[:-delay]
        y = time_series2[delay:]
    else:
        x = time_series1[:]
        y = time_series2[:]
        
    corr = sp.pearsonr(x, y)[0]
    return corr

def correlation_cities(cities1, cities2, dataset, year, delay, threshold):
    # Function that receives two arrays of cities' names and returns a list of cities' names from cities2 that has a
    # pearson correlation above threshold
    cor_cities = []
    for city1 in cities1:
        for city2 in cities2:
            cor_city1 = dataset[city1[0]][year].values
            cor_city2 = dataset[city2[0]][year].values
            p = pearson_correlation(cor_city1, cor_city2, delay)
            if p > threshold:
                cor_cities.append((city1[0], city2[0]))
    return cor_cities
    
def two_derivatives(city, week):
    # Function that returns true if the disease_frequency still grows after it reached 300 per 100000 of inhabitants
    if (len(city) - 2 <= week):
        return False
    D1 = (city[week + 1] - city[week])/2
    D2 = (city[week + 2] - city[week + 1])/2
    if D1 > 0 and D2 > 0:
        return True
    return False

def find_outbreaks(dataset, city, year):
    # Function that returns true if an outbreak occurred in that city, during that year,
    # and the week that the outbreak started. If there wasn't an outbreak that year, week returns -1
    disease_frequency = dataset[city][year]
    count = 0;
    for i in range(len(disease_frequency)):
        count = count + disease_frequency[i]
        if count >= (3 / 1000):
            if two_derivatives(disease_frequency, i):
                return True, i
    return False, -1


def derivative_correlation(time_series1, time_series2, delay=0, start=0, time=4):
    # Derivative correlation
    pass

