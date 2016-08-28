import correlations as cor
import dataset as dt
import runtime_functions as rt
import numpy as np

# Read user input
data_file = input("Entre com o nome do arquivo csv: ")
dataset = dt.read_raw_input(data_file)
#population_file = input("Entre com o nome do arquivo das populacoes: ")
#population = dt.read_population(population_file)
#dataset = dt.weight_population(dataset1, population)
focus_time = int(input("Entre com a quantidade de semanas do foco: "))

# First filter
cities = dataset.index.levels[0]
years = dataset.index.levels[1]
outbreaks = {}
for year in years:
    outbreak_cities = []
    for city in cities:
        occurred_outbreak, week = cor.find_outbreaks(dataset, city, year)
        if occurred_outbreak:
            outbreak_cities.append((city, week))
    outbreaks[year] = outbreak_cities

# Find graph
for year in years:
    focus = []
    outbreak_cities = outbreaks[year]
    outbreak_cities.sort(key=lambda x : x[1])
    i = 0

    # Focus
    startweek_focus = outbreak_cities[0][1]
    endweek_focus = startweek_focus + focus_time
    while outbreak_cities[i][1] <= endweek_focus:
        focus.append(outbreak_cities[i])
        i = i + 1
    print(year)
    print("Focos da doenca: ", focus)

    # Following graph levels, after focus
    j = 1
    all_levels = []
    all_levels.append(focus)
    while i < len(outbreak_cities):
        # level j
        level = []
        while i < len(outbreak_cities) and outbreak_cities[i][1] == (endweek_focus + j):
            level.append(outbreak_cities[i])
            i = i + 1
        if len(level) >= 1: # Do not print levels that don't have cities
            print("Nivel " + str(j) + ": " + str(level))
        all_levels.append(level)
         
        # Correlation between the levels of the graph
        print("Correlacoes:")   
        for k in range(j):
            cor.cities_correlations(all_levels[k], all_levels[j], dataset, year, j - k, year)
            
        j = j + 1
    print()
