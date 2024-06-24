import math

# CALCULA O VOLUME DO DEPÓSITO
def calcula_volume_deposito(comprimento, largura, altura):
    return comprimento * largura * altura

# CALCULA O VOLUME DA BOLA
def calcula_volume_bola(diametro):
    raio = diametro / 2
    volume = (4/3) * math.pi * (raio ** 3) # OU -> volume = (4/3) * 3.14159 * (raio ** 3)
    return volume

# CALCULA A ESTIMATIVA DO NUMERO DE BOLAS QUE CABEM NO DEPÓSITO
def estima_numero_bolas(volume_deposito, volume_bola):
    if volume_bola == 0:
        return 0
    return int(volume_deposito // volume_bola)