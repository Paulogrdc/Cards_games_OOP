from classes.cartas import Carta 
from rich import print
import math 

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
    "2- O CÓDIGO DEVE SER UMA LETRA DE A ATÉ D E UM NÚMERO 1 ATÉ 4\n"
    "3- O JOGO TEM UM MODO DE BATALHA, ONDE QUEM GANNHA É QUEM TEM O [blue]SUPER PODER[/] MAIS FORTE. " \
    "SUPER PODE É UMA MÉDIA ARITIMETRICA ENTRE ALGUMAS CARACTERISTICAS DA CARTA(PIB, ÁREA, POPULAÇÃO...)[/]")


def guardar_cartas(): 
    # Abre o arquivo em modo de escrita 
    arq = open("database/guardar_cartas.txt", "w")

    # Cadastra a primeira carta
    print("Cadastre a primeira carta")
    c1= Carta(
        estado= input("Estado: "),  
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= int(input("População: ")),
        pib= int(input("Pib: ")), 
        area= int(input("Área: ")), 
        pontos_turistico= int(input("Pontos Turuisticos: "))) 

    # Guarda a carta 1 no arquivo guardar_cartas.txt
    dict_c1 = c1.__dict__ 
    arq.write(str(f"Carta 1:{dict_c1}\n"))
    arq.write(str(c1.super_poder()))
    arq.write(str("\n"))
    

    # Cadastra a segunda carta
    print("Cadastre a segunda carta")
    c2 = Carta(
        estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= int(input("População: ")),
        pib= int(input("Pib: ")), 
        area= int(input("Área: ")), 
        pontos_turistico= int(input("Pontos Turuisticos: ")))   
          
    # Guarda a carta 2 no arquivo guardar_cartas.txt
    dict_c2= c2.__dict__ 
    arq.write(str(f"Carta 2: {dict_c2} \n"))
    arq.write(str(c2.super_poder()))


def mostrar_cartas(): 
    with open("database/guardar_cartas.txt", "r", encoding='utf8') as arq: 
        lista = []
        for line in arq: 
            lista.append(line)
        carta1 = lista[0]
        carta2 = lista[2]
        print(f"{carta1}\n")
        print(f"{carta2} ") 



def batalhar():
    with open("database/guardar_cartas.txt", "r", encoding='utf8') as arq:
        list_power = []
        for line in arq:
            list_power.append(line)
        super_poder1 = math.floor(float(list_power[1]))
        super_poder2 = math.floor(float(list_power[3]))

        if super_poder1 > super_poder2:
            print(f"A Carta 1 tem o super poder de: {super_poder1} pontos de poder e ela é a vencedora")
        elif super_poder1 ==  super_poder2: 
            print(f"A Carta 1 tem o super poder de: {super_poder1}")
            print(f"A Carta 2 tem o super poder de: {super_poder2}")
            print("Os Pontos de super poder das cartas são iguais. não há vencedor")
        else: 
           print(f"A Carta 2 tem o super poder de: {super_poder2}pontos de poder  e ela é a vencedora")

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
                guardar_cartas()
                print("[green]Cartas Cadastradas com sucesso![/]")

                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))

            case 3:
                mostrar_cartas()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))
                

            case 4: 
                batalhar()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))

            case 5: 
                break

            case _: 
                print("Valor invalido! essa opção não existe.") 
 



