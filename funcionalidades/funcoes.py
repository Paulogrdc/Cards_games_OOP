from classes.cartas import Carta 
from rich import print

# --- função para guardar as mensagem de opação ---
def guardar_mensagem():
    print("---------------------------SEJA BEM-VINDO AO JOGO DE CARTAS---------------------------")
    print("1-Como funciona o jogo")
    print("2-Cadastrar cartas")
    print("3-Mostrar cartas cadastradas")
    print("4-Batalhar")
    print("5-Fechar jogo") 



def regras_jogo(): 
    print("[blue]--------------------------REGRAS DO JOGO--------------------------[/]")
    print("[yellow]1-DIGITE O ESTADO DE FORMA ABREVIADA. EX: RJ, PA, SP... \n"
    "2- O CÓDIGO DEVE SER UMA LETRA DE A ATÉ F E UM NÚMERO 1 ATÉ 6\n"
    "3- O JOGO TEM UM MODO DE BATALHA, ONDE QUEM GANNHA É QUEM TEM O [blue]SUPER PODER[/] MAIS FORTE. " \
    "SUPER PODE É UMA MÉDIA ARITIMETRICA ENTRE ALGUMAS CARACTERISTICAS DA CARTA(PIB, ÁREA, POPULAÇÃO...)[/]")

def cadastrar_cartas(): 
    arq = open("database/guardar_cartas.txt", "w")

    print("Cadastre a primeira carta")
    c1= Carta(
        estado= input("Estado: "),  
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))
    
    dict_c1 = c1.__dict__ 
    arq.write(str(f"Carta 1:{dict_c1}\n"))
    arq.write(str("\n"))
  

    print("Cadastre a segunda carta")
    c2 = Carta(
        estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))
    
    dict_c2= c2.__dict__ 
    arq.write(str(f"Carta 2: {dict_c2}"))

    return c1, c2 

def mostrar_cartas(): 
    arq = open("database/guardar_cartas.txt", "r")
    for line in arq: 
        print(line)


def menu(): 
    guardar_mensagem()
    opcao = int(input("Escolha uma opação: "))

    while True: 
        match opcao: 

            case 1: 
                regras_jogo()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))    

            case 2: 
                cadastrar_cartas()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))

            case 3:
                mostrar_cartas()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))
                

            case 4: 
                pass

            case 5: 
                break

            case _: 
                print("Valor invalido! essa opção não existe.") 
 



