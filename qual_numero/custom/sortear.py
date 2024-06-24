from custom.validar_input import validar_input

def analisar_palpite(numero, palpite):
    if palpite == numero:
        return print(f"Isto é INCRÍVEL! Você acertou de primeira. O número secreto é {numero} e o palpite é {palpite}.")
    else:
        numero_palpites = 1
        
        # LAÇO DE REPETIÇÃO ATÉ QUE O PALPITE SEJA IGUAL AO NUMERO RANDÔMICO
    while palpite != numero:
            numero_palpites += 1
            # SE O PALPITE FOR MENOR DO QUE O NUMERO RANDÔMICO
            if palpite < numero:
                print("Seu palpite está baixo...")
            else:
                print("Seu palpite está alto...")
            
	    # VALIDA NOVO PALPITE
            palpite = validar_input()
            if palpite is False:
                print(f"Você excedeu o número de tentativas. O número secreto era {numero}.")
                return

    print(f"Fim de jogo! Você acertou após {numero_palpites} tentativas válidas. O número secreto é {numero} e o palpite é {palpite}.")
