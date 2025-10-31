alunos = {}
nomes = set()
opcao = 7

while opcao != 0:
    print("\n------------ SISTEMA DE CONTROLE DE ALUNOS E NOTAS -----------------")
    print("---- MENU PRINCIPAL ------------------------------------------")
    print("---- 1) CADASTRAR NOVO ALUNO -------------------------------")
    print("---- 2) REGISTRAR NOTAS ------------------------------------")
    print("---- 3) LISTAR ALUNOS E MÉDIAS -----------------------------")
    print("---- 4) BUSCAR ALUNO ---------------------------------------")
    print("---- 5) MOSTRAR APROVADOS E REPROVADOS ---------------------")
    print("---- 6) RELATÓRIOS -----------------------------------------")
    print("---- 0) SAIR -----------------------------------------------")
    print(" ")

    opcao = int(input("Selecione uma opcao: "))
    print(" ")

    if opcao == 1:
        print(" ")
        print("\n------------ SISTEMA DE CADASTRO DE ALUNOS -----------------")
        print("---- 1) CADASTRAR NOVO ALUNO -------------------------------")

        mat = int(input("Digite a matrícula do aluno: "))
        nome = str(input("Digite o nome do aluno: "))

        if mat in alunos:
            print("Esta matrícula já está cadastrada.")
        elif nome in nomes:
            print("Este nome já está cadastrado.")
        else:
            alunos[mat] = [nome, []]
            nomes.add(nome)
            print("ALUNO CADASTRADO COM SUCESSO!")

   
    elif opcao == 2:
        print(" ")
        print("\n------------ SISTEMA DE CADASTRO DE ALUNOS -----------------")
        print("---- 2) REGISTRAR NOTAS -----------------------------------")

        mat = int(input("Digite a matrícula do aluno: "))

        if mat not in alunos:
            print("Aluno não encontrado!")
        else:
            notas = []
            print("\nDigite as 3 notas do aluno:")
            for i in range(1, 4):
                nota = float(input("Digite a {}º nota: ".format(i)))
                notas.append(nota)

            alunos[mat][1] = tuple(notas)
            print("\nNotas registradas com sucesso!")

  
    elif opcao == 3:
        print(" ")
        print("\n------------ SISTEMA DE CADASTRO DE ALUNOS -----------------")
        print("---- 3) LISTAR ALUNOS E MÉDIAS -----------------------------")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for mat in alunos:
                nome, notas = alunos[mat]
                if len(notas) > 0:
                    media = sum(notas) / len(notas)
                    print("\nMatrícula: {}".format(mat))
                    print("Nome: {}".format(nome))
                    print("Notas: {}".format(notas))
                    print("Média: {:.1f}".format(media))
                else:
                    print("\nMatrícula: {}".format(mat))
                    print("Nome: {}".format(nome))
                    print("Notas não registradas no sistema.")


    elif opcao == 4:
        print(" ")
        print("\n------------ SISTEMA DE CONTROLE DE ALUNOS E NOTAS -----------------")
        print("---- 4) BUSCAR ALUNO --------------------------------------")

        mat = int(input("Digite a matrícula do aluno: "))

        if mat in alunos:
            nome, notas = alunos[mat]
            print("\nAluno encontrado: {}".format(nome))

            if len(notas) > 0:
                media = sum(notas) / len(notas)
                print("Notas: {}".format(notas))
                print("Média: {:.1f}".format(media))
            else:
                print("Este aluno ainda não tem notas registradas.")
        else:
            print("Aluno não encontrado.")


    elif opcao == 5:
        print(" ")
        print("\n------------ SISTEMA DE CONTROLE DE ALUNOS E NOTAS -----------------")
        print("---- 5) MOSTRAR APROVADOS E REPROVADOS ---------------------")

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for mat in alunos:
                nome, notas = alunos[mat]
                if len(notas) > 0:
                    media = sum(notas) / len(notas)
                    if media >= 7:
                        print("Aluno: {}".format(nome))
                        print("Média: {:.1f}".format(media))
                        print("Situação: APROVADO!")
                    else:
                        print("Aluno: {}".format(nome))
                        print("Média: {:.1f}".format(media))
                        print("Situação: REPROVADO!")
                else:
                    print("\n{} não possui notas registradas no sistema!".format(nome))

    
    elif opcao == 6:
        print(" ")
        print("\n------------ SISTEMA DE CONTROLE DE ALUNOS E NOTAS -----------------")
        print("---6) RELATÓRIOS -----------------")
        print("1 - Alunos cadastrados")
        print("2 - Médias individuais")
        print("3 - Aprovados e Reprovados")

        op = int(input("\nEscolha uma opção para gerar um relatório: "))

        if op == 1:
            print("\n1) ALUNOS CADASTRADOS -----------------")
            for mat in alunos:
                nome, notas = alunos[mat]
                print("{} - {}".format(mat, nome))

        elif op == 2:
            print("\n2) MÉDIAS INDIVIDUAIS -----------------")
            for mat in alunos:
                nome, notas = alunos[mat]
                if len(notas) > 0:
                    media = sum(notas) / len(notas)
                    print("Aluno: {}".format(nome))
                    print("Média: {:.1f}".format(media))
                else:
                    print("{} não possui notas registradas no sistema!".format(nome))

        elif op == 3:
            print("\n3) APROVADOS E REPROVADOS -----------------")
            for mat in alunos:
                nome, notas = alunos[mat]
                if len(notas) > 0:
                    media = sum(notas) / len(notas)
                    if media >= 7:
                        print("Aluno: {}".format(nome))
                        print("Média: {:.1f}".format(media))
                        print("Situação: APROVADO!")
                    else:
                        print("Aluno: {}".format(nome))
                        print("Média: {:.1f}".format(media))
                        print("Situação: REPROVADO!")
                else:
                    print("{} não possui notas registradas no sistema!".format(nome))

    elif opcao == 0:
        print("\nVoce saiu do sistema!")

    else:
         print("\nOpção Inválida! Tente novamente.")
