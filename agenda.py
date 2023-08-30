from os import system
import re

system("cls")

# Lista Vazia para Armazenar nome e número
lista_tel = [["Ana", "000000"], ["Beto", "1111111"], ["Carlos", "222222"], ["Carlos", "3333333"]]

print("AGENDA TELEFÔNICA")

nome =   input("Digite o nome do contato:   ")
numero = input("Digite o número do contato: ")
lista_tel.append([nome, numero])

for i in lista_tel:
    print("Nome: ", i[0], "    Telefone: ", i[1])


print("--- Editando lista ---")


# Anota as posições de todos os matches de nome na lista_tel em query_results
query_results = [] 
nome = input("Informe o nome do contato a ser editado: ")
j = 0
for i in lista_tel:
    if nome in i[0]:
        query_results.append(j)
    j = j + 1


# Se não encontrar nenhum match len(query_results) = 0
if len(query_results) == 0:
    print("Não foi encontrado nenhum contato com este nome.")


# Caso contrário, eu encontrei pelo menos um contato
else:
    # print(query_results)
    print("Foram encontrados resultados para a sua pesquisa. Digite o código do contato para renomear")
    k = 0
    for i in query_results:
        print("CÓD.:", k, "Nome: ", lista_tel[i][0], "    Telefone: ", lista_tel[i][1])
        k =  k + 1
    codigo = int(input("Digite qual deles você deseja alterar: "))
    num_or_name = input("Deseja alterar nome (1), número (2) ou ambos (3)?  ")

    if num_or_name == "1":
        lista_tel[query_results[codigo]][0] = input("Digite o nome:   ")
    elif num_or_name == "2":
        lista_tel[query_results[codigo]][1] = input("Digite o número: ")
    elif num_or_name == "3":
        lista_tel[query_results[codigo]][0] = input("Digite o nome:   ")
        lista_tel[query_results[codigo]][1] = input("Digite o número: ")
    else:
        print("Comando inválido!")

query_results_temp = [] 
nome = input("Informe o nome do contato a ser excluído: ")
j = 0
for i in lista_tel:
    if nome in i[0]:
        query_results_temp.append(j)
    j = j + 1

if len(query_results_temp) == 0:
    print("Não foi encontrado nenhum contato com este nome.")


# Caso contrário, eu encontrei pelo menos um contato
else:
    # print(query_results)
    print("Foram encontrados resultados para a sua pesquisa. Digite o código do contato para renomear")
    k = 0
    for i in query_results_temp:
        print("CÓD.:", k, "Nome: ", lista_tel[i][0], "    Telefone: ", lista_tel[i][1])
        k =  k + 1
    codigo = int(input("Digite qual deles você deseja excluir: "))

    lista_tel.pop(query_results_temp[codigo])

print("Nova lista: ")
for i in lista_tel:
    print("Nome: ", i[0], "    Telefone: ", i[1])
