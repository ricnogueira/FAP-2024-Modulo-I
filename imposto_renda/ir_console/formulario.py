from custom.calculos_ir import calcula_ir

print("###########################################")
print("###  PROGRAMA CALCULA IMPOSTO DE RENDA  ###")
print("###########################################\n")
print("OS CAMPOS COM * SÃO OBRIGATÓRIOS")
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n")

nome = input("Digite o seu nome: ")
print("")

tentativas = 0
numero_tentativas = 4

while tentativas < numero_tentativas:
    print("-> Exemplo para R$ 1.250,25: 1250.25 <-"'\n')
    salario = input("Insira o valor do seu salário * : ")
    try:
        salario = float(salario)
        break
    except ValueError:
        print("")
        tentativas += 1
        print(f"Entrada inválida. Você tem mais {numero_tentativas - tentativas} tentativa(s).")
else:
    print("Entrada inválida. Exemplo para R$ 1.250,25: 1250.25 \n")

resultado_consulta = calcula_ir(salario, nome)
print("")
print(resultado_consulta)
print("")