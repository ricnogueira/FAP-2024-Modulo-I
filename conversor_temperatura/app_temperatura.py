from custom.valida_input import valida_temperatura, valida_tipo_temperatura
from custom.converte_temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius

def main():
    tipo_temperatura = valida_tipo_temperatura()
    if tipo_temperatura is None:
        return
    
    temperatura = valida_temperatura()
    if temperatura is None:
        return

    if tipo_temperatura == 'C':
        convertido = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C é igual a {convertido:.2f}°F")
    
    elif tipo_temperatura == 'F':
        convertido = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F é igual a {convertido:.2f}°C")

if __name__ == "__main__":
    main()