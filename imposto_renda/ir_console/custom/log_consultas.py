
import datetime
def log_consultas(log, nome):

    with open("logs/logs.txt", "a") as f:
        
        agora = datetime.datetime.now().strftime("%d-%m-%Y (%A) - %H:%M:%S")
        
        if nome == "":
            nome = "ANÔNIMO"
        
        f.write(f'{agora} - Consulta realizada por {str.upper(nome)} - {log}\n')