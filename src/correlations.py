import scipy.stats as sp

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


def find_outbreaks(timeseries, population):
    # Function that creates a boolean array with value True where an epidemic outbreak occurs
    # Outbreak: Infected people surpass 300 per thousand of habitants
    outbreak = timeseries/population > 0.3
    return outbreak


def derivative_correlation(time_series1, time_series2, delay=0, start=0, time=4):
    # Derivative correlation
    pass

