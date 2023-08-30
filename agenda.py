from os import system
system("cls")


def encontraPosicao(nick, array):
    query = []
    j = 0
    for i in array:
        if nick in i[0]:
            query.append(j)
        j = j + 1
    return query
            

# Lista Vazia para Armazenar nome e número
lista_tel = []

while (True):
    system("cls")
    print("AGENDA TELEFÔNICA\n\n1 - ADICIONAR NOVO CONTATO\n2 - EXIBIR LISTA TELEFÔNICA\n3 - EDITAR LISTA TELEFÔNICA\n4 - EXCLUIR CONTATO\n0 - SAIR")

    comando = input("COMANDO: ")

    # ADICIONA CONTATO
    if comando == "1":
        system("cls")

        nome =   input("Digite o nome do contato:   ")
        numero = input("Digite o número do contato: ")
        lista_tel.append([nome, numero])

    # EXIBE LISTA TELEFÔNICA
    elif comando == "2":
        system("cls")

        for i in lista_tel:
            print("Nome: ", i[0], "    Telefone: ", i[1])
        
        wait = input("\n\n\nPRIMA ENTER PARA CONTINUAR")

    # EDITA LISTA TELEFÔNICA
    elif comando == "3":
        system("cls")


        # Anota as posições de todos os matches de nome na lista_tel em query_results
        nome = input("Informe o nome do contato a ser editado: ")
        query_results = encontraPosicao(nome, lista_tel)

        
        
        # Se não encontrar nenhum match len(query_results) = 0
        if len(query_results) == 0:
            print("Não foi encontrado nenhum contato com este nome.")
        
        #Caso encontre, eu peço ao usuário para dizer qual deve ser excluído
        else:
            print("Foram encontrados resultados para a sua pesquisa. Digite o código do contato para renomear")
            k = 0
            for i in query_results:
                print("CÓD.:", k, "Nome: ", lista_tel[i][0], "    Telefone: ", lista_tel[i][1])
                k =  k + 1
            codigo = int(input("\nDigite qual deles você deseja alterar: "))
            num_or_name = input("\nDeseja alterar nome (1), número (2) ou ambos (3)?  ")

            if num_or_name == "1":
                lista_tel[query_results[codigo]][0] = input("Digite o nome:   ")
            elif num_or_name == "2":
                lista_tel[query_results[codigo]][1] = input("Digite o número: ")
            elif num_or_name == "3":
                lista_tel[query_results[codigo]][0] = input("Digite o nome:   ")
                lista_tel[query_results[codigo]][1] = input("Digite o número: ")
            else:
                print("Comando inválido!")



    # EXCLUI UM CONTATO DA LISTA TELEFÔNICA
    elif comando == "4":
        system("cls")


        nome = input("Informe o nome do contato a ser excluído: ")
        query_results_temp = encontraPosicao(nome, lista_tel)

        if len(query_results_temp) == 0:
            print("Não foi encontrado nenhum contato com este nome.")
        else:
            print("Foram encontrados resultados para a sua pesquisa. Digite o código do contato para renomear")
            k = 0
            for i in query_results_temp:
                print("CÓD.:", k, "Nome: ", lista_tel[i][0], "    Telefone: ", lista_tel[i][1])
                k =  k + 1
            codigo = int(input("Digite qual deles você deseja excluir: "))

            lista_tel.pop(query_results_temp[codigo])
    

    # TERMINA O PROGRAMA
    elif comando == "0":
        break
    

    # COMANDO INVÁLIDO
    else:
        system("cls")
        print("Comando não consta na base de dados.")
