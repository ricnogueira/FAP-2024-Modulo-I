def valida_tipo_temperatura():
    tentativas = 0
    numero_tentativas = 4
    
    while tentativas < numero_tentativas:
        tipo = input("Digite 'C' para Celsius ou 'F' para Fahrenheit: ").strip().upper()
        if tipo in ['C', 'F']:
            return tipo
        else:
            print(f"Entrada inválida. Tente novamente. Restam {numero_tentativas - tentativas -1 } tentativas.")
            tentativas += 1
        if tentativas == numero_tentativas:
            print("PROGRAMA FINALIZADO. TENTE NOVAMENTE SEGUINDO AS INSTRUÇÕES!\n")
    return None


def valida_temperatura():
    tentativas = 0
    numero_tentativas = 4
    while tentativas < numero_tentativas:
        try:
            temperatura = float(input("Digite a temperatura: ").strip())
            return temperatura
        except ValueError:
            print(f"Entrada inválida. Deve ser um número. Restam {numero_tentativas - tentativas -1 } tentativas.")
            tentativas += 1
    print("PROGRAMA FINALIZADO. TENTE NOVAMENTE SEGUINDO AS INSTRUÇÕES!\n")
    return None