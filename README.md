# project-epidemio
Projeto de Iniciação Científica do IME-USP  
Aluno: Augusto César  
Orientadora: Claudia Peixoto  

O objetivo do projeto é desenvolver um software de codigo aberto que analise dados de uma doença infecciosa e crie um grafo que mostre como a doença se espalha através das cidades.  

O grafo:  
Um grafo direcionado e ponderado onde todos os vértices são cidades e existe uma aresta indo do vertice u até v com peso w se a correlação entre a cidade u e a cidade v com "delay" de w semanas é acima de um determinado limiar.  

A estrutura dos dados de entrada:  
Os dados de entrada podem estar de duas formas: dados brutos ou dados da incidencia por semana.
   Dados Brutos:
   Dados brutos são a quantidade de notificações por semana da doença. Cada linha representa uma cidade e cada coluna uma semana, em ordem cronológica. Dados de exemplo serão adicionados.
O programa também necessita de um arquivo de texto com duas colunas sendo a primeira o nome do município e a segunda a população urbana dele. 

   Dados de Incidencia:
   Dados de incidencia são os dados já divididos pelo tamanho da população de cada município.

Programa:  
O programa receberá os dados em .csv e fará um pré-processamento para mudá-los para o formato series do pandas. Com os dados nesse formato, o programa realizará um filtro para retirar os municípios em que não houve surto da doença (não houve incidência de mais de 300 casos a cada 100000 habitantes). O programa então reconhecerá os surtos significativos das doenças e usará isso para achar o foco (municípios que tiveram surto da doença em semanas anteriores ao surto dos outros municípios). Após isso, o algoritmo realizará correlações entre as cidades do foco e as cidades que tiveram surtos posteriores, montando assim o grafo direcionado da mobilidade da doença.

-----------------------------------------------------------------------------------------------------------------------

Undergraduate research project of IME-USP, developed by Augusto César

The main idea of the project is to develop an open source software to analyze data of an infectious disease, creating a network graph of how the disease spread through the cities.

The network graph:  
A weighted directed graph where all the vertices are cities and, if there is an edge going from city1 to city2 with weight w, the correlation between city1 and city2 with delay w is above a determined threshold.   

The input dataset structure:  
The input dataset must be in one of the two following structures: raw data or frequency data
    Raw data:
    Raw data is a dataset where each line represents one city and each column represents a week, in chronological order. Example datasets are going to be added soon.
    The program also needs a file with two columns, the first being the name of the city and the second the population of it. 

    Frequency data:
    Frequency data is a dataset already divided by the population of the city.

Program:  
The program will receive the dataset in a .csv file and it will pre-process it to change it to the pandas series format. After that, the program will filter the dataset to use only the cities where an significant outbreak occurred (that is, more than 300 cases per 100000 inhabitants). The program find where those outbreaks occurred and will use that to find the focus (cities that had outbreaks before the others). Then, the algoritm will do correlations between the focus and the other cities, therefore, creating a directed graph of the disease spread.
