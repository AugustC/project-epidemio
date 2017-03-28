# -*- coding: utf-8 -*-
import correlations as cor
import dataset as dt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def calcula_grafo_correlacoes(data_file, year, aux=1, population_file="", focus_time=2, k=0.85):
    
    # Read user input
    if aux == 1:
        dataset = dt.read_raw_input(data_file)
        population = dt.read_population(population_file)
        dataset = dt.weight_population(dataset, population)
    else:
        dataset = dt.read_frequency_input(data_file)
    
    # First filter (Use only cities where an outbreak occurred)
    cities = dataset.index.levels[0]
    years = dataset.index.levels[1]
    all_outbreaks = {}
    for ano in years:
        outbreak = []
        for city in cities:
            occurred_outbreak, week = cor.find_outbreaks(dataset, city, ano)
            if occurred_outbreak:
                outbreak.append((city, week))
        all_outbreaks[ano] = outbreak
    
    # Find graph
    focus = []
    g = nx.DiGraph()
    outbreak = all_outbreaks[year]
    outbreak.sort(key=lambda x : x[1])
    i = 0
    
    # Focus
    if not outbreak:
        print("Nao houve incidencia no ano de " + year)
        return
    startweek_focus = outbreak[0][1]
    endweek_focus = startweek_focus + focus_time
    while outbreak[i][1] <= endweek_focus:
        focus.append(outbreak[i][0])
        g.add_node(outbreak[i][0])
        i = i + 1
        if len(outbreak) <= i:
            break
    # Table
    cities = [x[0] for x in outbreak]
    table = pd.DataFrame(index=cities, columns=cities)

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
    
    # Fill table and print
    for correlations in all_city_correlations:
        for corr in correlations:
            table.set_value(corr[0], corr[1], corr[2])
    table.to_csv(path_or_buf=year, sep=";")
    
    pos_spring = nx.spring_layout(g)
    nx.draw_networkx(g, with_labels=False, arrows=True, node_color='y', linewidth=0, pos=pos_spring)
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos_spring, edge_labels=labels)
    for p in pos_spring:         
        pos_spring[p][1] += 0.05
    nx.draw_networkx_labels(g, pos_spring)

    plt.title(year)
    plt.savefig(year + ".png")
