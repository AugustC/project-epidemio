import scipy as sp

def correlation_pearson(time_series1, time_series2, start, delay=0, time=4):
    # Pearson correlation of the disease frequency in time_series1 and time_series2
    # between weeks 'start' and 'start + time'.
    # The delay is applied on time_series2.
    x = time_series1[start : start + time]
    y = time_series2[start + delay : start + time]
    (corr,,) = sp.stats.pearsonr(x, y)
    return corr

def find_outbreaks(timeseries, population):
    # Function that creates a boolean array with value true where an epidemic outbreak occurs
    # Outbreak: Infected people surpass 300 per thousand of habitants
    outbreak = timeseries/population > 0.3
    return outbreak

def correlation_derivative(time_series1, time_series2, delay=0, start=0, time=4):
    # Derivative correlation
    pass



