
def valida_float(nota_input):
  """
  Valida se a string de entrada pode ser convertida para um float e continua solicitando
  a entrada até que um valor válido seja fornecido.

  Argumentos:
    entrada_str (str): A string a ser validada.

  Retorna:
    float: O número float convertido da string, ou `None` se a conversão falhar.
  """
  while True:
    try:
      return float(nota_input)
    except ValueError:
      print("Entrada inválida. Exemplo: 6 ou 7.5!")
      nota_input = input("Digite novamente: ")

def valida_int(nota_input):
  """
  Valida se a string de entrada pode ser convertida para um int e continua solicitando
  a entrada até que um valor válido seja fornecido.

  Argumentos:
    entrada_str (str): A string a ser validada.

  Retorna:
    int: O número int convertido da string, ou `None` se a conversão falhar.
  """
  while True:
    try:
      #return int(nota_input)
      return int(nota_input)
    except ValueError:
      print("Entrada inválida. Exemplo: 1, 12 ou 123!")
      nota_input = input("Digite novamente: ")