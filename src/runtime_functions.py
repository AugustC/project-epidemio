def user_interaction(choice, dataset):
    choices = {
        0 : close_program,
        1 : list_cities,
        2 : choose_city }
    choices[choice](dataset)
    return
    
def close_program(dataset):
    return 0

def list_cities(dataset):
    # List all cities in the dataset
    for city in dataset.index.levels[0]:
        print(city)

def choose_city(dataset):
    # Print cities with the select number
    print("Escolha o numero da cidade que deseja selecionar: ")
    i = 1
    for city in dataset.index.levels[0]:
        print(str(i) + " - " + city)
        i = i + 1
        
    # Choices of what to do with the choosen city (print time_series graph, do the correlation with another)
    city_choices = {
        0 : "Fazer correlação com outra",
        1 : "Plotar o gráfico da incidência",
        2 : "Escolher outra cidade"
    }
    city_choices_function = {
        0 : correlation,
        1 : plot,
        2 : choose_city
    }
    city = int(input())
    print("Cidade escolhida: " + dataset.index.levels[0][city])
    print("Escolha o que deseja fazer com a cidade escolhida: ")
    print(city_choices)

    user_input = int(input())
    while user_input not in [0, 1, 2]:
        print("Por favor, escolha entre 0, 1 e 2")
        user_input = int(input())

    city_choices[user_input]()

def correlation():
    pass

def plot():
    pass



