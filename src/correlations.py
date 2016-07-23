import scipy as sp
import City

def correlation_pearson(city1, city2, start, delay=0, time=4):
    # Pearson correlation of the disease frequency in city1 and city2
    # between weeks 'start' and 'start + time'.
    # The delay is applied on city2.
    x = city1.frequency[start : start + time]
    y = city2.frequency[start + delay : start + time]
    (corr,,) = sp.stats.pearsonr(x, y)
    return corr

def correlation_derivative(city1, city2, delay=0, start=0, time=4):
    # Derivative correlation
    pass



