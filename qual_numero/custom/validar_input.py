# VALIDA O PALPITE
def validar_input():
    tentativa = 0
    numero_tentativas = 4
    
    # ENQUANTO A TENTATIVA FOR MENOR QUE A NUMERO DE TENTATIVAS, PEDE QUE O JOGADOR DIGITE UM NUMERO
    while tentativa < numero_tentativas:
        palpite = input("Digite um numero entre 0 e 100: ")
        # SE O PALPITE FOR UM NUMERO E ESTIVER ENTRE 0 E 100, RETORNA O PALPITE
        if palpite.isdigit() and 0 <= int(palpite) <= 100:
            return int(palpite)
        # CASO CONTRÁRIO, INCREMENTA A TENTATIVA E IMPRIME A MENSAGEM DE ERRO
        else:
            tentativa += 1
            print(f"Digite apenas numeros entre 0 e 100. Restam {numero_tentativas - tentativa} tentativas.")
        
    # RETORNA FALSO CASO A TENTATIVA SEJA IGUAL AO NUMERO DE TENTATIVAS
    return False
