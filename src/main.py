# -*- coding: utf-8 -*-
import correlations as cor
import dataset as dt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Read user input
aux = input("1 - Ler dados brutos, 2 - Ler dados de frequencia: ")
data_file = input("Entre com o nome do arquivo csv: ")
if aux == '1':
    dataset = dt.read_raw_input(data_file)
    population_file = input("Entre com o nome do arquivo das populacoes: ")
    population = dt.read_population(population_file)
    dataset = dt.weight_population(dataset, population)
else:
    dataset = dt.read_frequency_input(data_file)

focus_time = int(input("Entre com a quantidade de semanas do foco: "))
k = float(input("Entre com o threshold da correlacao: "))

# First filter (Use only cities where an outbreak occurred)
cities = dataset.index.levels[0]
years = dataset.index.levels[1]
all_outbreaks = {}
for year in years:
    outbreak = []
    for city in cities:
        occurred_outbreak, week = cor.find_outbreaks(dataset, city, year)
        if occurred_outbreak:
            outbreak.append((city, week))
    all_outbreaks[year] = outbreak

# Find graph
year = input("Entre com o ano desejado: ")                     # user input
focus = []
g = nx.DiGraph()
outbreak = all_outbreaks[year]
outbreak.sort(key=lambda x : x[1])
i = 0

# Focus
startweek_focus = outbreak[0][1]
endweek_focus = startweek_focus + focus_time
while outbreak[i][1] <= endweek_focus:
    focus.append(outbreak[i][0])
    i = i + 1
    g.add_node(outbreak[i][0])

# Other levels of the graph
remains = [city[0] for city in outbreak if city[0] not in focus]
i = 1 
all_city_correlations = []
levels = [focus]
while remains:
    # Do the correlation between the cities on the graph and the remaining ones with a delay
    city_correlation = cor.correlation_cities(focus, remains, dataset, year, i, k)
    for j in range(1,i):
        l = cor.correlation_cities(levels[j - 1], remains, dataset, year, i - j, k)
        if l:
            city_correlation.extend(l)
    if not city_correlation:                   # there's no more correlations
        g.add_nodes_from(remains)
        remains = []
    else:                                         # add another level
        g.add_nodes_from([x[1] for x in city_correlation])
        g.add_edges_from([(x[0], x[1], { 'weight' : x[2]}) for x in city_correlation])
        all_city_correlations.append(city_correlation)
        new_cities = [x[1] for x in city_correlation]
        levels.append(new_cities)
        remains = [city for city in remains if city not in new_cities]
        i += 1

# TODO: Change color of focus, put weight(delay) on edges
pos_spring = nx.spring_layout(g)
nx.draw_networkx(g, with_labels=False, arrows=True, node_color='y', linewidth=0, pos=pos_spring)
for p in pos_spring:
    pos_spring[p][1] += 0.05
nx.draw_networkx_labels(g, pos_spring)
plt.show()
