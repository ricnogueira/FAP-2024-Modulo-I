
# FUNCAO QUE VALIDA AS INFORMAÇÕES INSERIDAS PELO O USUARIO. COMPRIMENTO, LARGURA E ALTURA DO DEPÓSITO E TAMANHO DA BOLA.
# A FUNÇÃO WHILE TRATA A QUANTIDADE DE TENTATIVAS DE ENTRADAS INVALIDAS.
def valida_input():
    
    max_tentativas = 3  # Número máximo de tentativas permitidas
    tentativas_restantes = max_tentativas

    while tentativas_restantes > 0:
        try:
            comprimento = float(input("Digite o comprimento do depósito (em cm): "))
            largura = float(input("Digite a largura do depósito (em cm): "))
            altura = float(input("Digite a altura do depósito (em cm): "))
            break
        except ValueError:
            tentativas_restantes -= 1
            print(f"Entrada inválida. Você tem {tentativas_restantes} tentativa(s) restante(s).")
            if tentativas_restantes == 0:
                return None, None, None, None
    
    if tentativas_restantes == 0:
        return None, None, None, None

    bolas = {
        1: ("Bola de Basquete Adulto", 24),
        2: ("Bola de Basquete Infantil", 22),
        3: ("Bola de Futebol Oficial", 22),
        4: ("Bola de Vôlei", 21),
        5: ("Bola de Handball", 19),
        6: ("Bola de Futebol de Salão", 20),
        7: ("Outro tamanho de bola", None)
    }

    tentativas_restantes = max_tentativas

    while tentativas_restantes > 0:
        try:
            print("\nSelecione o tipo de bola:")
            for key, value in bolas.items():
                print(f"{key}: {value[0]} ({'Personalizado' if value[1] is None else value[1]} cm)")

            escolha = int(input("Digite o número correspondente ao tipo de bola: "))
            if escolha not in bolas:
                tentativas_restantes_escolha = max_tentativas
                while tentativas_restantes_escolha > 0:
                    try:
                        escolha = int(input("Digite o número correspondente ao tipo de bola: "))
                        break
                    except ValueError:
                        tentativas_restantes_escolha -= 1
                        print(f"Entrada inválida. Você tem {tentativas_restantes_escolha} tentativa(s) restante(s).")
                        if tentativas_restantes_escolha == 0:
                            return None, None, None, None
            if escolha == 7:
                tentativas_restantes_diametro = max_tentativas
                while tentativas_restantes_diametro > 0:
                    try:
                        diametro = float(input("Digite o diâmetro da bola (em cm): "))
                        break
                    except ValueError:
                        tentativas_restantes_diametro -= 1
                        print(f"Entrada inválida. Você tem {tentativas_restantes_diametro} tentativa(s) restante(s).")
                        if tentativas_restantes_diametro == 0:
                            return None, None, None, None
            else:
                diametro = bolas[escolha][1]
            break
        except ValueError as e:
            tentativas_restantes -= 1
            print(f"{e} Você tem {tentativas_restantes} tentativa(s) restante(s).")
            if tentativas_restantes == 0:
                return None, None, None, None

    return comprimento, largura, altura, diametro
