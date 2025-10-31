produtos = []
codigos_cadastrados = set()
categorias = ("Alimentos", "Limpeza", "Bebidas")

while True:
    print("\n=== Sistema de cadastro de produtos===") 
    print ("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        codigo = int(input("Digite o código do produto (apenas números): "))
        if codigo in codigos_cadastrados:
            print("Código já cadastrado!")    
            continue 

        nome = input("Nome do produto: ")
        preco = input("Preço do produto: ")

        quantidade = input("Quantidade em estoque: ")

        print("\n=== Categorias disponíveis ===")
        print("1 - Alimentos")
        print("2 - Limpeza")
        print("3 - Bebidas")
        print("4 - Outros produtos")
        categoria_escolhida = input("Digite a categoria: ")
        
        if categoria_escolhida == "1":
            categoria = "Alimentos"

        elif categoria_escolhida == "2":
            categoria = "Limpeza"

        elif categoria_escolhida == "3":
            categoria = "Bebidas"

        elif categoria_escolhida == "4":
            categoria = "Outros produtos"            

        produto = {
            "Código": codigo,
            "Nome": nome,
            "Preço": preco,
            "Quantidade": quantidade,
            "Categoria": categoria
        }
        produtos.append(produto)
        codigos_cadastrados.add(codigo)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":

        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== Lista de Produtos ===")
            for produto in produtos:
                print(produto)
    
    elif opcao == "3":

           codigo_busca = int(input("Digite o código do produto: "))
           encontrado = False
           
           for produto in produtos:
              if produto["codigo"] == codigo_busca:
                print(f"Produto encontrado: {produto}")
                encontrado = True
                break    

           if not encontrado:
               
               print("Produto não encontrado.")

    elif opcao == "4":
          
          codigo_atualizar = int(input("Digite o código do produto a atualizar: "))
          encontrado = False
 
          print("O que você deseja atualizar?")
          print("1 - Nome")
          print("2 - Preço")
          print("3 - Quantidade") 
          print("4 - Categoria")
          atualizar = input()

          for produto in produtos:
              if produto["codigo"] == codigo_atualizar:

                if atualizar == "1":
                   produto["nome"] = input("Novo nome: ").strip()
                
                elif atualizar == "2":   
                   produto["preco"] = float(input("Novo preço: "))   
                
                elif atualizar == "3":                 
                   produto["quantide"] = int(input("Nova quantidade: "))

                elif atualizar == "4":
                    print("\n=== Categorias disponíveis ===")
                    print("1 - Alimentos")
                    print("2 - Limpeza")
                    print("3 - Bebidas")
                    print("4 - Outros produtos")
                    produto["categoria"] = input("Digite a categoria: ").strip()
            
                else:
                    print("Opção inválida para atualização.")
                    break
                
                print("Produto atualizado com sucesso!")
                encontrado = True
                break

          if not encontrado:
             print("Produto não encontrado.")


    elif opcao == "5": 

          codigo_excluir = int(input("Digite o código do produto a ser excluido: "))
          
          encontrado = False

          for produto in produtos:
              if produto["codigo"] == codigo_excluir:
                  produtos.remove(produto)
                  codigos_cadastrados.remove(codigo_excluir)
                  print("Produto excluído com sucesso!")
                  encontrado = True
                  break
              
          if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "0":
          
          print("Saindo do sistema..." )
          break 
   
    else:
          print("Opção inválida, digite um número de 1 a 5.")