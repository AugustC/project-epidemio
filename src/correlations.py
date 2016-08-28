import scipy.stats as sp
import numpy as np

def pearson_correlation(time_series1, time_series2, delay=0):
    # Pearson correlation of the disease frequency in time_series1 and time_series2    
    x = time_series1[:-delay]
    y = time_series2[delay:]
    corr = sp.pearsonr(x, y)[0]
    return corr

def cities_correlations(city1, city2, dataset, year, delay, threshold):
    # Function that receives two arrays of (city, week) and perform the correlation between city 1 and city 2
    # in the year passed as argument, with a delay between the weeks,
    for c1 in city1:
        for c2 in city2:
            cor_city1 = dataset[c1[0]][year].values
            cor_city2 = dataset[c2[0]][year].values
            pcor = pearson_correlation(cor_city1, cor_city2, delay)
            if pcor > threshold:
                print(c1[0] + " --> " + c2[0] + " with delay " + str(delay))
    
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
    disease_frequency = dataset[city][year].values
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

