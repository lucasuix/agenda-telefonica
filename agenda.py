from os import system
import re

system("clear")

# Lista Vazia para Armazenar nome e número
lista_tel = [["Ana", "000000"], ["Beto", "1111111"], ["Carlos", "222222"], ["Carlos", "3333333"]]

print("AGENDA TELEFÔNICA")

nome =   input("Digite o nome do contato:   ")
numero = input("Digite o número do contato: ")
lista_tel.append([nome, numero])

for i in lista_tel:
    print("Nome: ", i[0], "    Telefone: ", i[1])

