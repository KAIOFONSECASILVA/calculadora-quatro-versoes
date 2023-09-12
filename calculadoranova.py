import biblioteca_funcoes as f

print("escolha:\n---------------------\n1)soma\n2)subtração\n3)multiplicação\n4)divisao\n5)potencia\n6)radiação\n---------------------")

op=int (input("digite o nummero da opção:"))
match op:
    case 1:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.soma(a,b)
    case 2:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.sub(a,b)
    case 3:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.mult(a,b)
    case 4:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.div(a,b)
    case 5:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.pot(a,b)
    case 6:
        a= int (input("digite o primeiro valor:"))
        b= int (input("digite o segundo valor:"))
        f.rad(a,b)