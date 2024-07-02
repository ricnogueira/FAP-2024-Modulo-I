from custom.banco_pandas import *
from custom.valida_id import valida_id
from custom.valida_input import *

BANCO = "banco.csv"

# INICIO DO PROGRAMA
alunos = [] # Lista para armazenar os alunos

while True:
    print("\nMenu de Cadastro de Alunos:")
    print("[1] Cadastrar novo aluno")
    print("[2] Listar alunos cadastrados")
    print("[3] Para atualizar aluno")
    print("[4] Para excluir aluno")
    print("[5] Para pesquisar aluno")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRA NOVO ALUNO
    if opcao == "1":
       
        # INICIA DICIONARIO VAZIO PARA O ALUNO
        novo_aluno = {}
        novo_aluno["nome"] = input("Nome do aluno: ").upper()
        novo_aluno["curso"] = input("Curso: ").title()
        
        matricula_input = input("Matrícula: ")
        novo_aluno["matricula"] = valida_int(matricula_input)
        
        nota_input = input("Digite a nota 1: ")
        novo_aluno['n1'] = valida_float(nota_input)
        
        nota_input = input("Digite a nota 2: ")
        novo_aluno['n2'] = valida_float(nota_input)
        
        nota_input = input("Digite a nota 3: ")
        novo_aluno['n3'] = valida_float(nota_input)
        
        nota_input = input("Digite a nota 4: ")
        novo_aluno['n4'] = valida_float(nota_input)
        
        novo_aluno["media"] =  (novo_aluno["n1"] + novo_aluno["n2"] + novo_aluno["n3"] + novo_aluno["n4"]) / 4
        # CHAMA FUNÇÃO PARA CADASTRAR ALUNO
        create_aluno(novo_aluno["nome"], novo_aluno["curso"], novo_aluno["matricula"], novo_aluno["n1"], novo_aluno["n2"], novo_aluno["n3"], novo_aluno["n4"], novo_aluno["media"])
        
    # LISTA ALUNOS
    elif opcao == "2":
        # LISTA ALUNOS CADASTRADOS
        select_all(BANCO)

    # ATUALIZA ALUNO
    elif opcao == "3":
        # LISTA ALUNOS CADASTRADOS
        select_all(BANCO)

        id_aluno = valida_int(input("\nDigite o ID do aluno que deseja atualizar: "))

        # VALIDA ID ALUNO É VALIDO E NÃO EXISTE ALUNO CADASTRADO COM ESSE ID 
        if id_aluno == None or valida_id(id_aluno) == True:
            print("ID inválido!")
            
        else:    
            nome = input("Digite o novo nome: ").upper()
            curso = input("Digite o novo curso: ").title()
            
            matricula = valida_int(input("Digite a nova matricula: "))
            n1 = valida_float(input("Digite a nova nota 1: "))
            n2 = valida_float(input("Digite a nova nota 2: "))
            n3 = valida_float(input("Digite a nova nota 3: "))
            n4 = valida_float(input("Digite a nova nota 4: "))

            # CRIA UM DICIONARIO COM AS NOVAS INFROMACOES DO ALUNO
            novos_dados = {"NOME": nome, 
                        "CURSO": curso,
                        "MATRICULA": matricula,
                        "NOTA1": n1,
                        "NOTA2": n2,
                        "NOTA3": n3,
                        "NOTA4": n4,
                        "MEDIA": (n1 + n2 + n3 + n4) / 4
                        }

            # CHAMA FUNÇÃO PARA ATUALIZAR ALUNO
            update_aluno(id_aluno, novos_dados)

    # APAGA ALUNO
    elif opcao == "4":
        print("")
        print("--------------------------------------")
        print("LISTA DE ALUNOS CADASTRADOS NO SISTEMA")
        print("--------------------------------------")
        # CHAMA FUNÇÃO PARA VERIFICAR SE EXISTE ALUNO CADASTRADO
        if select_all(BANCO) is not None:
            print("Acesse o menu [1] para cadastrar novo aluno.")
        else:
            id_aluno = valida_int(input("\nDigite o ID do aluno que deseja apagar: "))
            if id_aluno == None or valida_id(id_aluno) == True:
                print("ID inválido!")
            else:
            # CHAMA FUNção PARA APAGAR ALUNO
                delete_aluno(id_aluno)
    
    # PESQUISA ALUNO
    elif opcao == "5":
        # SOLICITA NOME DO ALUNO A SER PESQUISADO
        nome_pesquisa = input("Digite o nome do aluno que deseja pesquisar: ").upper()
        # CHAMA FUNÇÃO PARA PESQUISAR ALUNO
        search_aluno(nome_pesquisa)
        
    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

