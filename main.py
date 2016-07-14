import correlations
import dataset

# Implement GUI for input
filename = input("Entre com o nome do arquivo csv: ")
dataset = read_input(filename)

cities = data_to_frequency(dataset)

# User choices (correlation, graphs)

""" 
correlation between cities := correlation of the amount of infected people between city1 and city2
Disease network
 - For each epidemic outbreak of each city, do the correlation between the city and all the other cities.
   If the correlation is above a determined threshold, put the cities in a cluster.
   Do it again, with a delay of one, two and three weeks between city1 and city2. 
   If the correlation is above the threshold, put a link between city1 and city2.
"""
