from custom.calculos_imc import calcula_imc
from custom.validador_input import *

print("############################")
print("###  PROGRAMA IMC CHECK  ###")
print("############################\n")
print("OS CAMPOS COM * SÃO OBRIGATÓRIOS")
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n")

nome = input("Informe seu nome: ").upper()
if nome == "":
    nome = "ANÔNIMO"

idade = valida_idade()
peso = valida_peso()
altura = valida_altura()

print("")
print(f'Prezado paciente, {nome}!\n')
calcula_imc(peso, altura)
print("")
print("###############################")
print("###  TABELA REFERÊNCIA IMC  ###")
print("###############################")
print("-------------------------------------------------------------------")
print("| IMC                     CLASSIFICACAO          OBESIDADE (grau) |")
print("-------------------------------------------------------------------")
print("  MENOR QUE 18.5          MAGREZA                0")
print("  ENTRE 18.5 e 24.9       NORMAL                 0")
print("  ENTRE 25.0 e 29.9       SOBREPESO              0")
print("  ENTRE 30,0 e 34,9       OBESIDADE              I")
print("  ENTRE 35,0 e 39,9       OBESIDADE              II")
print("  MAIOR que 40.0          OBESIDADE GRAVE        III")


print("")
peso = str(peso).replace('.',',')
altura = str(altura).replace('.',',')
print(f"Resumo das informações fornecidas:\nNome: {nome}\nIdade: {idade} anos \nPeso: {peso} Kg\nAltura: {altura} m\n")
