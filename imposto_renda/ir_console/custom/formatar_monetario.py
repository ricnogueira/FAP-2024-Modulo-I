def format_brl(salario):
    
    valor = f'{salario:_.2f}'
    valor = valor.replace('.',',').replace('_','.')
    
    return f'R$ {valor}'