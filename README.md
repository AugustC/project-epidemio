# project-epidemio
Projeto de Iniciação Científica do IME-USP  
Aluno: Augusto César  
Orientadora: Claudia Peixoto  

O objetivo do projeto é desenvolver um software de codigo aberto que analise dados de uma doença infecciosa e crie um grafo que mostre como a doença se espalha através das cidades.  

O grafo:  
Um grafo direcionado e ponderado onde todos os vértices são cidades e existe uma aresta indo do vertice u até v com peso w se a correlação entre a cidade u e a cidade v com "delay" de w semanas é acima de um determinado limiar.  

A estrutura dos dados de entrada:  
Os dados atualmente usados estão em formato csv, com a seguinte estrutura:  
1 - ID  
2 - MUNIRES  
3 - Data de Notificação  
4 - Semana da Notificação  
5 - Ano  
6 - Sigla UF  
7 - ID do municipio  
8 - ID da unidade de saúde  
9 - NU_IDADE  
10- Idade  
11- Data de nascimento  
12- Região  
13- Estado  
14- Cidade  
Possivelmente essa estrutura será mudada para uma mais simples e mais abrangente no futuro, sem os atributos não usados.  
O programa necessita também da população de cada cidade.  

Programa:  
O programa receberá os dados em .csv e fará um pré-processamento para criar os objetos da classe City, onde cada um será uma cidade com a frequencia da doença, o nome da cidade, a população total e as semanas em que houve um pico significativo da doença. Com isso o programa poderá desenhar os gráficos de frequencia de cada cidade e fazer a correlação entre as cidades para criar uma rede que mostre como a doença se espalha.  

-----------------------------------------------------------------------------------------------------------------------

Undergraduate research project of IME-USP, developed by Augusto César

The main idea of the project is to develop an open source software to analyze data of an infectious disease, creating a network graph of how the disease spread through the cities.

The network graph:  
A weighted directed graph where all the vertices are cities and, if there is an edge going from city1 to city2 with weight w, the correlation between city1 and city2 with delay w is above a determined threshold.   

The input dataset structure:  
The actual dataset have the following structure, where each line is one case of the disease:  
1 - ID  
2 - MUNIRES  
3 - Notification date  
4 - Notification week  
5 - Year  
6 - UF initials  
7 - City ID  
8 - Health unit ID  
9 - NU_IDADE  
10- Age  
11- Birthday  
12- Region  
13- State  
14- City  
Possibly this structure will change in the future to a simpler one, without the useless atributes.  
The program will also receive the total population of each city.  

Program:  
The program will receive the dataset in a .csv file and it will pre-process it to create the objects of the class City, where each object has the name of the city, the disease frequency, the total population and the weeks of a significant outbreak. Then, the program can plot the frequency graphs of the disease in each city and do the correlation between cities to create the network graph of how the disease spread.