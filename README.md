# project-epidemio
Projeto de Inicia��o Cient�fica do IME-USP  
Aluno: Augusto C�sar  
Orientadora: Claudia Peixoto  

O objetivo do projeto � desenvolver um software de codigo aberto que analise dados de uma doen�a infecciosa e crie um grafo que mostre como a doen�a se espalha atrav�s das cidades.  

O grafo:  
Um grafo direcionado e ponderado onde todos os v�rtices s�o cidades e existe uma aresta indo do vertice u at� v com peso w se a correla��o entre a cidade u e a cidade v com "delay" de w semanas � acima de um determinado limiar.  

A estrutura dos dados de entrada:  
Os dados de entrada podem estar de duas formas: dados brutos ou dados da incidencia por semana.
   Dados Brutos:
   Dados brutos s�o os dados em que cada linha � um caso da doen�a. Esses dados precisam estar em formato csv e possuir as seguintes colunas: CIDADE(cidade ou munic�pio em que foi notificada a doen�a), NU_ANO(numero do ano em que ocorreu a doen�a) e SEM_NOT(semana do ano em que ocorreu a doen�a, i. e., primeira semana (1), segunda semana(2), etc.)
   Dados da incidencia:
   Dados da incidencia da doen�a por semana, i. e., uma matriz em que cada linha � um munic�pio e cada coluna � uma semana e os valores s�o a incidencia da doen�a naquela cidade durante aquela semana. 
O programa tamb�m necessita de um arquivo de texto com duas colunas sendo a primeira o nome do munic�pio e a segunda a popula��o urbana dele. 

Programa:  
O programa receber� os dados em .csv e far� um pr�-processamento para mud�-los para o formato series do pandas. Com os dados nesse formato, o programa realizar� um filtro para retirar os munic�pios em que n�o houve surto da doen�a (n�o houve incid�ncia de mais de 300 casos a cada 100000 habitantes). O programa ent�o reconhecer� os surtos significativos das doen�as e usar� isso para achar o foco (munic�pios que tiveram surto da doen�a em semanas anteriores ao surto dos outros munic�pios). Ap�s isso, o algoritmo realizar� correla��es entre as cidades do foco e as cidades que tiveram surtos posteriores, montando assim o grafo direcionado da mobilidade da doen�a.

-----------------------------------------------------------------------------------------------------------------------

Undergraduate research project of IME-USP, developed by Augusto C�sar

The main idea of the project is to develop an open source software to analyze data of an infectious disease, creating a network graph of how the disease spread through the cities.

The network graph:  
A weighted directed graph where all the vertices are cities and, if there is an edge going from city1 to city2 with weight w, the correlation between city1 and city2 with delay w is above a determined threshold.   

The input dataset structure:  
The input dataset must be in one of the two following structures: raw data or frequency data
    Raw data:
    Raw data is a dataset where each line is a case of the disease. This dataset must be in csv format and have the following columns: CIDADE (city where the disease was notified), NU_ANO(the year when the disease was notified), SEM_NOT(the week of the year in which the disease was notified, that is, first week (1), second week(2), so forth)
    Frequency data:
    Frequency data of the disease per week, that is, a matrix where each line is a city and each column is a week and the values are the disease frequency of that city during that week.


Program:  
The program will receive the dataset in a .csv file and it will pre-process it to change it to the pandas series format. After that, the program will filter the dataset to use only the cities where an significant outbreak occurred (that is, more than 300 cases per 100000 inhabitants). The program find where those outbreaks occurred and will use that to find the focus (cities that had outbreaks before the others). Then, the algoritm will do correlations between the focus and the other cities, therefore, creating a directed graph of the disease spread.