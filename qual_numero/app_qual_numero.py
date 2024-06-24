from custom.validar_input import validar_input
from custom.sortear import analisar_palpite
import random

# GERA O NUMERO ALEATORIO
numero = random.randint(0, 100)

# RECEBE O PALPITE INICIAL DO JOGADOR E CHAMA A FUNCAO VALIDAR_INPUT PARA VALIDAR
palpite = validar_input()

# SE PASSAR PELA VALIDACAO, CHAMA A FUNCAO ANALISAR_PALPITE E CASO CONTRÁRIO, IMPRIME A MENSAGEM DE ERRO.
if palpite is not False:
    analisar_palpite(numero, palpite)
else:
    print("Você não forneceu um palpite válido. Tente novamente seguindo as instruções.")
