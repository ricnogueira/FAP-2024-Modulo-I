from custom.formatar_monetario import format_brl
from custom.log_consultas import log_consultas

def calcula_ir(salario, nome):
    
    salario = float(salario)
    
    if salario < 2259.21:
        salario = format_brl(salario)
        log_consultas(f'O valor informado de {salario} está isento do IR 2024.', nome)
        return f'O valor informado de {salario} está isento do IR 2024.'
    
    elif salario > 2259.20 and salario < 2826.66:
        aliquota_str = "7,5%"
        aliquota = 0.075 # FAIXA 2 - 7,5%
        deducao = 169.44
        imposto = salario * aliquota
        imposto_final = salario * aliquota - deducao
        log_consultas(f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}', nome)
        return f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}'
    
    elif salario > 2826.65 and salario < 3751.06:
        aliquota_str = "15%"
        aliquota = 0.15 # FAIXA 3 - 15%
        deducao = 381.44
        imposto = salario * aliquota
        imposto_final = salario * aliquota - deducao
        log_consultas(f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}', nome)
        return f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}'
    
    elif salario > 3751.05 and salario < 4664.69:
        aliquota_str = "22,5%"
        aliquota = 0.225 # FAIXA 4 - 22,5%
        deducao = 662.77
        imposto = salario * aliquota
        imposto_final = salario * aliquota - deducao
        log_consultas(f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}', nome)
        return f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}'
    
    else:
        aliquota_str = "27,5%"
        aliquota = 0.275
        deducao = 896.00
        imposto = salario * aliquota
        imposto_final = salario * aliquota - deducao
        log_consultas(f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}', nome)
        return f'Valor informado: {format_brl(salario)} || Aliquota: {aliquota_str} || Imposto: {format_brl(imposto)} || Dedução: {format_brl(deducao)} || IMPOSTO A PAGAR: {format_brl(imposto_final)}'

