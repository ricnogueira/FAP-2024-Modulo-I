from pandas import pandas as pd

BANCO = "./banco.csv"

def valida_id(id_aluno):
  
  # LE ARQUIVO CSV CONTENDO ALUNOS CADASTRADOS
  df = pd.read_csv(BANCO)

  # VERIFICA EXISTENCIA DO ID DO ALUNO 
  if id_aluno >= len(df):
    return True
  else:
    return False
