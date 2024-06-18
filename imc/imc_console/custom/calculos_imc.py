def calcula_imc(peso, altura):
    dados_imc = peso / (altura ** 2)
    imc_resultado = resultado_imc(dados_imc)
    print(imc_resultado)
    return imc_resultado

def resultado_imc(imc_resultado):
    if imc_resultado < 18.5:
        return f'O seu IMC é {imc_resultado:.1f} - ATENÇÃO! Você foi classificado como (MAGREZA)!'
    elif 18.5 <= imc_resultado <= 24.9:
        return f'O seu IMC é {imc_resultado:.1f} - PARABÉNS! Você está com o peso ideal (NORMAL)!'
    elif 25 <= imc_resultado <= 29.9:
        return f'O seu IMC é {imc_resultado:.1f} - ATENÇÃO! Você está com sobrepeso (SOBREPESO)!'
    elif 30 <= imc_resultado <= 34.9:
        return f'O seu IMC é {imc_resultado:.1f} - ATENÇÃO! Obesidade grau I (OBESIDADE)!'
    elif 35 <= imc_resultado <= 39.9:
        return f'O seu IMC é {imc_resultado:.1f} - ATENÇÃO! Obesidade grau II (OBESIDADE)!'
    else:
        return f'O seu IMC é {imc_resultado:.1f} - ATENÇÃO! Obesidade grau III (OBESIDADE GRAVE)!'