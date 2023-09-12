
from datetime import datetime

def saudacao(nome):

    hora = datetime.now().hour


    if hora>=0 and hora <=12:
        print("bom dia!",nome)
    elif hora>17:
        print("boa noite!",nome)
    else:
        print("boa tarde!",nome)

nome=input("digite seu nome:")
saudacao(nome)