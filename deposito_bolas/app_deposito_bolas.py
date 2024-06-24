from custom.calculos_volume import *
from custom.valida_input import valida_input

# FUNÇÃO QUE EXIBE A ESTIMATIVA DE BOLAS
def exibir_resultado(numero_bolas):
    print(f"\nNúmero aproximado de bolas que cabem no depósito: {numero_bolas:,}".replace(',', '.'))

# DEFINA COMO FUNÇÃO PRINCIPAL
def main():
    comprimento, largura, altura, diametro = valida_input()
    if comprimento is None or largura is None or altura is None or diametro is None:
        print("O programa foi finalizado devido a entradas inválidas repetidas.")
        return

    volume_deposito = calcula_volume_deposito(comprimento, largura, altura)
    volume_bola = calcula_volume_bola(diametro)
    numero_bolas = estima_numero_bolas(volume_deposito, volume_bola)
    
    exibir_resultado(numero_bolas)

# EXECUTA A FUNÇÃO PRINCIPAL - MAIN
if __name__ == "__main__":
    main()