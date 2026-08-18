from classes.cartas import Carta 

# --- função para guardar as mensagem de opação ---
def guardar_mensagem():
    print("---------------------------SEJA BEM-VINDO AO JOGO DE CARTAS---------------------------")
    print("1-Como funciona o jogo")
    print("2-Cadastrar cartas")
    print("3-Mostrar cartas cadastradas")
    print("4-Batalhar")
    print("5-Fechar jogo") 


def cadastrar_cartas(): 
    print("Cadastre a primeira carta")
    c1= Carta(
        estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))
                        
    print("Cadastre a segunda carta")
    c2 = Carta(
        estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))

    return c1 ,c2 


def mostrar_cartas(): 
    pass



def menu(): 
    guardar_mensagem()
    opcao = int(input("Escolha uma opação: "))

    while True: 
        match opcao: 

            case 1: 
                print("Está funcionando!") 
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))    

            case 2: 
                cadastrar_cartas()
                guardar_mensagem()
                opcao = int(input("Escolha uma opação: "))

            case 3: 
                pass 

            case 4: 
                pass

            case 5: 
                break

            case _: 
                print("Valor invalido! essa opção não existe.") 
 



