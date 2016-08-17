import scipy.stats as sp
import numpy as np

def pearson_correlation(time_series1, time_series2, start, maxdelay=0, time=4):
    # Pearson correlation of the disease frequency in time_series1 and time_series2
    # between weeks 'start' and 'start + time'.
    # If maxdelay is greater than 0, the function returns the maximum correlation between time_series1
    # and time_series2 with delays (0 <= delays <= maxdelay) applied on the second time_series, and the
    # delay number that gave the maximum correlation

    correlation_delay = 0
    max_correlation = -1
    
    for delay in range(maxdelay + 1):
        x = time_series1[start : start + time]
        y = time_series2[start + delay : start + time + delay]
        corr = sp.pearsonr(x, y)[0]
        if corr > max_correlation:
            max_correlation = corr
            correlation_delay = delay
            
    return max_correlation, correlation_delay

def two_derivatives(city, week):
    D1 = (city[week + 1] - city[week])/2
    D2 = (city[week + 2] - city[week + 1])/2
    if D1 > 0 and D2 > 0:
        return True
    return False

def find_outbreaks(city, population):
    # Function that returns a boolean array with the value true for each year where a significant outbreak occurred
    # Outbreak: Amount of infected people surpass 300 per 100000 of inhabitants
    years = city.index.levels[0]
    outbreak = []
    for year in years:
        city_year = city[year].values
        sum = 0;
        tmp = [year, False, 0]
        for i in range(len(city_year)):
            sum = city_year[i]
            if sum >= (3 / 1000): # Amount of notified diseases surpassed 300 per 100000 of inhabitants 
                if two_derivatives(city_year, i): # The disease frequency went up after that week
                    tmp = [year, True, i]
                    outbreak.append(tmp)
                    break
    return outbreak


def derivative_correlation(time_series1, time_series2, delay=0, start=0, time=4):
    # Derivative correlation
    pass

