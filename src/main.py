import correlations as cor
import dataset as dt
import runtime_functions as rt
import numpy as np

# Read Dataset
data_file = input("Entre com o nome do arquivo csv: ")
dataset = dt.read_raw_input(data_file)
population_file = input("Entre com o nome do arquivo das populações: ")
population = dt.read_population(population_file)

# First filter
cities = dataset.index.levels[0]
years = data.index.levels[1]
outbreaks = []
for city in cities:
    out = find_outbreaks(dataset[city], population[city])
    outbreaks.append(out)
outbreaks = np.reshape(outbreaks, (len(cities), len(years), 3))

# Find focus
