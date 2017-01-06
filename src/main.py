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
outbreaks = {}
for year in years:
    outbreak_cities = []
    for city in cities:
        occurred_outbreak, week = cor.find_outbreaks(dataset, city, year)
        if occurred_outbreak:
            outbreak_cities.append((city, week))
    outbreaks[year] = outbreak_cities

# Find graph
year = input("Entre com o ano desejado: ")                     # user input
focus = []
g = nx.DiGraph()
outbreak_cities = outbreaks[year]
outbreak_cities.sort(key=lambda x : x[1])
i = 0

# Focus
startweek_focus = outbreak_cities[0][1]
endweek_focus = startweek_focus + focus_time
while outbreak_cities[i][1] <= endweek_focus:
    focus.append(outbreak_cities[i])
    i = i + 1
    g.add_node(outbreak_cities[i][0])
f_print = tuple(city[0] for city in focus)
print("Focos da doenca: ", f_print)
    
# S1, first graph level
S1 = [city for city in outbreak_cities if city not in focus]
S1_cities = cor.correlation_cities(focus, S1, dataset, year, 1, k)

print()
print("Cidades que tiveram correlacao maior que " + str(k) + " com delay 0")
for cities in S1_cities:
    print(cities)
    g.add_node(cities[1])    
    g.add_edge(cities[0], cities[1])

# TODO: Change color of focus
pos_spring = nx.spring_layout(g)
nx.draw_networkx(g, with_labels=False, arrows=True, node_color='y', linewidth=0, pos=pos_spring)
for p in pos_spring:
    pos_spring[p][1] += 0.03
nx.draw_networkx_labels(g, pos_spring)
plt.show()

# S2 = [city for city in outbreak_cities if city not in focus]
    

