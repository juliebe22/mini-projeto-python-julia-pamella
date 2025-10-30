# Projetos com estrutura de repetição e estrutura de dados 💻
## Sistema de Cadastro de Produtos 
### Funções do sistema:
#### • Cadastrar produtos:
Solicita código, nome, preço, quantidade e categoria, evita códigos duplicados usando o set e adiciona o produto à lista.
#### • Listar produtos:
Percorre a lista e mostra todos os produtos cadastrados com suas especificações.
#### • Buscar produtos:
Permite procurar produtos pelo código e o exibe com suas especificações. Caso o produto não esteja cadastrado imprimi-se uma mensagem de "Produto não encontrado".
#### • Atualizar produtos:
Permite atualizar uma espeficificação de um produto existente. 
#### • Excluir produtos:
Remove um produto pelo código.
#### • Sair do sistema:
Encerra o programa.

#### É um sistema simples, feito em python, usando estruturas de repetição e de dados.

### Estrutura de repetição ultilizadas:
#### • For:
Usado para percorrer a lista de produtos.
#### • While:
Usado para manter o menu interativo em execução.
### Estrutura de dados ultilizadas:
#### • Lista:
Armazena os produtos cadastrados.
#### • Conjunto(set):
Garante que não haja produtos duplicados.
#### • Tupla:
Armazena as categorias fixas.
#### • Dicionário:
Representa um único produto, armazenando informações em pares chave: valor.

## Sistema de Controle de Alunos e Notas 

O sistema de controle de alunos e notas foi desenvolvido em Python, utilizando
estruturas de repetição e estruturas de dados para gerenciar informações sobre
alunos e suas notas.
### Funções do sistema:
#### • Cadastrar alunos
Solicita a matrícula e o nome do aluno e evita matrículas e nomes duplicados usando
set e dicionário.
#### • Registrar notas
Permite registrar 3 notas para um aluno já cadastrado, usando a matrícula como
referência.
#### • Listar alunos e médias
Mostra todos os alunos cadastrados com suas notas e a média final.
Caso o aluno ainda não tenha notas registradas, mostra a mensagem "Aluno X não
possui notas registradas no sistema”.
#### • Buscar aluno
Permite procurar um aluno pela matrícula e exibe suas notas e média.
Caso não exista, mostra a mensagem “Aluno não encontrado”.
#### • Mostrar aprovados e reprovados
Calcula a média dos alunos e exibe sua situação:
#### • Aprovado se a média for maior ou igual a 7
#### • Reprovado se for menor que 7
#### • Relatórios
### Gera relatórios com:
1. Alunos cadastrados
2. Médias individuais
3. Aprovados e reprovados
• Sair do sistema
Encerra o programa.
### Estruturas de repetição utilizadas:
#### • While
Mantém o menu interativo em execução até o usuário escolher sair (opção 0).
#### • For
Usado para:
• Percorrer a lista de notas dos alunos.
• Mostrar os alunos em listagens e relatórios.
### Estruturas de dados utilizadas:
#### • Dicionário (dict)
Armazena os alunos em um dicionário principal, usando a matrícula como chave e o
nome e notas como valor.
#### • Conjunto (set)
Evita que nomes duplicados sejam cadastrados.
#### • Lista (list)
Usada temporariamente para receber as notas antes de transformá-las em tupla.
#### • Tupla (tuple)
Armazena as notas do aluno de forma imutável.
Como funciona?
O sistema apresenta um menu principal com as opções numeradas.
O usuário escolhe uma opção e segue as instruções exibidas no console.
Exemplo:
------------ SISTEMA DE CONTROLE DE ALUNOS E NOTAS -----------------
---- MENU PRINCIPAL ------------------------------------------
1. Cadastrar novo aluno
2. Registrar notas
3. Listar alunos e médias
4. Buscar aluno
5. Mostrar aprovados e reprovados
6. Relatórios
7. Sair
Exemplo de uso:
### Exemplo 1: Cadastro de aluno
Digite a matrícula do aluno: 101
Digite o nome do aluno: Ana
ALUNO CADASTRADO COM SUCESSO!

### Exemplo 2: Registro de notas

Digite a matrícula do aluno: 101

Digite a 1ª nota: 8

Digite a 2ª nota: 7

Digite a 3ª nota: 9

Notas registradas com sucesso!

### Exemplo 3: Listagem de alunos e médias
Matrícula: 101
Nome: Ana
Notas: (8.0, 7.0, 9.0)
Média: 8.0
#Exemplo 4: Situação final
Aluno: Ana
Média: 8.0
Situação: APROVADO!
