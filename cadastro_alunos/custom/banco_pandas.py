from pandas import pandas as pd

BANCO = "./banco.csv"

def select_all(arquivo_csv):
  
  alunos = pd.read_csv(BANCO)
  if len(alunos) == 0 :
    return print("Não existe aluno cadastrado!"), None
  else:
    return print(alunos)


def create_aluno(nome, curso, matricula, n1, n2, n3, n4, media):
    
    try:
        # LE ARQUIVO CSV CONTENDO ALUNOS CADASTRADOS
        df = pd.read_csv(BANCO)
        
        # CRIA NOVO DICIONARIO COM AS INFORMACOES DO NOVO ALUNO
        novo_aluno = pd.DataFrame([{
            "NOME": nome,
            "CURSO": curso,
            "MATRICULA": matricula,
            "NOTA1": n1,
            "NOTA2": n2,
            "NOTA3": n3,
            "NOTA4": n4,
            "MEDIA": media
        }])

        # ADICIONA NOVO ALUNO AO ARQUIVO CSV
        df = pd.concat([df, novo_aluno])

        # SALVA O NOVO ALUNO NO ARQUIVO CSV
        df.to_csv(BANCO, index=False)

        # RETORNA MENSAGEM DE SUCESSO
        return f"Aluno {nome} adicionado com sucesso!"

    except Exception as e:
        # EXIBE MENSAGEM DE ERRO CASO O ALUNO NÃO SEJA ADICIONADO
        return f"Erro ao adicionar aluno: {e}"


# DELETA INDICE ESPECIFICO NO ARQUIVO CSV
def delete_aluno(id_aluno):

  try:
    # LE ARQUIVO CSV CONTENDO ALUNOS CADASTRADOS
    df = pd.read_csv(BANCO)

    # REMOVE A LINHA NO ARQUIVO CSV ESPECIFICADA PELO INDICE
    df.drop(id_aluno, inplace=True)

    # SALVA A ALTERAÇÃO NO ARQUIVO CSV
    df.to_csv(BANCO, index=False)

    # RETORNA NONE INDICANDO SUCESSO.
    return print(f"Aluno ID {id_aluno} excluído com sucesso!")

  except Exception as e:
    # EXIBE MENSAGEM DE ERRO CASO O ALUNO NÃO SEJA EXCLUIDO
    print(f"Erro ao remover linha: {e}")
    return f"Falha ao excluír ID {id_aluno}. Verifique o ID e tente novamente."

# ATUALIZA ALUNO PELO ID
def update_aluno(id_aluno, novos_dados):
  try:
    # LE ARQUIVO CSV CONTENDO ALUNOS CADASTRADOS
    df = pd.read_csv(BANCO)

    # VERIFICA SE O ID DO ALUNO EXISTE E SE NÃO É MAIOR DO QUE O COMPRIMENTO DA LISTA
    if id_aluno > len(df):
      raise IndexError(f"Não existe ID: {id_aluno}")

    # ATUALIZA OS DADOS DO ALUNO PELO INDICE ESPECIFICO
    df.loc[id_aluno, :] = novos_dados

    # SALVA A ALTERAÇÃO NO ARQUIVO CSV
    df.to_csv(BANCO, index=False)

    # RETORNA INDICANDO SUCESSO.
    return print(f"\nAluno ID {id_aluno} atualizado com sucesso!")

  except Exception as e:
    # EXIBE MENSAGEM DE ERRO CASO O ALUNO NÃO SEJA ATUALIZADO
    print(f"Erro ao atualizar linha: {e}")
    return f"Falha ao atualizar a linha {id_aluno} do arquivo {BANCO}"

# PESQUISA ALUNO PELO NOME
def search_aluno(nome_pesquisa):
  
  df = pd.read_csv(BANCO)
  
  resultado = df[df["NOME"].str.contains(nome_pesquisa, case=False, na=False)]
  
  if resultado.empty:
    print("----------------------------------------------")
    print(f"Aluno {nome_pesquisa} não encontrado na pesquisa")
    print("----------------------------------------------")
  else:
    print("----------------------------------------------")
    print("-------- ALUNO ENCONTRADO NA PESQUISA --------")
    print("----------------------------------------------")
    print(resultado)
    print("----------------------------------------------")
