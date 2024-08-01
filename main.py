from weather01 import*
from banco_mysql import*
from alerta import*
from chatbot_gemini import*

import os

os.system('cls')

def menu():
    print("Menu:")
    print("1. Ver previsão para os próximos dias/horários")
    print("2. Pedir ajuda do Gemini")
    print("3. Sair")


def solicitar_input():
    try:
        cidade = input("Digite a sua cidade: ")
        if not cidade:
            raise ValueError("Entrada vazia. Por favor, digite algo.")
    except ValueError as e:
        print(e)
        return solicitar_input()
    else:
        return cidade

cidade = solicitar_input()
print(cidade)

# enquanto a cidade for inválida, solicitar novamente o nome da cidade
while previsao_dia(cidade) == "Cidade não encontrada":
    print("Cidade inválida. Tente novamente.")
    cidade = solicitar_input()


while True: 
    menu()
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("Ver previsão para os próximos dias/horários")
        nome = input("Digite o seu nome: ")
        email = input("Digite o seu email para receber alerta de tempo: ")
        # registrar dados no mysql
        inserir_contato(nome, email, cidade) 
        # verificar temperatura e emitir alerta        
        check_temperature(temperatura(cidade) , email, nome) 
        # gerar gráfico de temperatura para proximos dias         
        previsao_tempo(cidade)
        menu()
    elif opcao == "2":
        print("Pedir ajuda do Gemini")
        chat_with_bot()
    elif opcao == "3":
        break
    else:
        print("Opção inválida!")


