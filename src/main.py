import correlations as cor
import dataset as dt
import runtime_functions as rt

# Implement GUI
user_choices = {
    0 : "Fechar o programa",
    1 : "Listar as cidades do arquivo",
    2 : "Escolher uma cidade especifica"
    }

# Main
filename = input("Entre com o nome do arquivo csv: ")
dataset = dt.read_input(filename)

user_input = 1
while(user_input != 0):
    print("Selecione o que deseja fazer:")
    print(user_choices)
    user_input = int(input())
    
    # Input verification (change to dict default of user_input?)
    while user_input not in [0, 1, 2]:
        print("Por favor, escolha entre 0, 1 e 2")
        user_input = int(input())

    rt.user_interaction(user_input, dataset)

