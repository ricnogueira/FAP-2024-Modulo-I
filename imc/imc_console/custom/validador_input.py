def valida_idade():
    tentativas = 0
    numero_tentativas = 4

    while tentativas < numero_tentativas:
        idade_input = input("Digite sua idade *: ")
        
        if idade_input.isdigit():
            idade = int(idade_input)
            if 1 <= idade <= 100:
                return idade
            else:
                print(f"Entrada inválida! A idade deve estar entre 1 e 100. Você tem mais {numero_tentativas - tentativas - 1} tentativa(s).\n")
        else:
            print(f"Entrada inválida! A idade deve estar entre 1 e 100. Você tem mais {numero_tentativas - tentativas - 1} tentativa(s).\n")
        
        tentativas += 1
        if tentativas == numero_tentativas:
            print("PROGRAMA FINALIZADO. TENTE NOVAMENTE SEGUINDO AS INSTRUÇÕES!\n")
            exit()

def valida_peso():
    tentativas = 0
    numero_tentativas = 4
    
    while tentativas < numero_tentativas:
        peso_input = input("Digite seu peso *: ").replace('.', '')
        if peso_input.isnumeric():
            peso_float = float(peso_input)
            peso = peso_float / 1000
            peso_input = round(peso, 3)
            if 1.0 <= peso_input <= 250.0:
                return peso
            else:
                print(f"Entrada inválida. O peso deve estar entre 1.000 e 250.000! Exemplo para 60 Kilos: 60.000. Para 75 Kilos e 255 gramas: 75.255 - Você tem mais {numero_tentativas - tentativas} tentativa(s).\n")
        else:
            print(f"Entrada inválida. O peso deve estar entre 1.000 e 250.000! Exemplo para 60 Kilos: 60.000. Para 75 Kilos e 255 gramas: 75.255 - Você tem mais {numero_tentativas - tentativas} tentativa(s).\n")
        
        tentativas += 1
        if tentativas == numero_tentativas:
            print("PROGRAMA FINALIZADO. TENTE NOVAMENTE SEGUINDO AS INSTRUÇÕES!\n")
            exit()

def valida_altura():
    tentativas = 0
    numero_tentativas = 4

    while tentativas < numero_tentativas:
        altura_input = input("Digite sua altura *: ").replace('.', '')
        if altura_input.isnumeric():
            altura_float = float(altura_input)
            altura = altura_float / 100
            altura_input = round(altura, 2)
            if 1.0 <= altura_input <= 2.55:
                return altura
            else:
                print(f"Entrada inválida! A altura deve estar entre 1.00 e 2.55 metros. Exemplo para 1,68 metros: 1.68 - Você tem mais {numero_tentativas - tentativas - 1} tentativa(s).\n")
        else:
            print(f"Entrada inválida! A altura deve estar entre 1.00 e 2.55 metros. Exemplo para 1,68 metros: 1.68 - Você tem mais {numero_tentativas - tentativas - 1} tentativa(s).\n")
        
        tentativas += 1
        if tentativas == numero_tentativas:
            print("PROGRAMA FINALIZADO. TENTE NOVAMENTE SEGUINDO AS INSTRUÇÕES!\n")
            exit()