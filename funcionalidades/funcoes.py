from classes.cartas import Carta 

# --- função para guardar as mensagem de opação ---
def guardar_mensagem():
    print("---------------------------SEJA BEM-VINDO AO JOGO DE CARTAS---------------------------")
    print("1-Como funciona o jogo")
    print("2-Cadastrar cartas")
    print("3-Mostrar cartas cadastradas")
    print("4-Jogar")
    print("5-Fechar jogo") 


def casdatrar_Carta(): 
    print("Cadastre a primeira carta")
    c1= Carta(estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        Pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))
                        
    print("Cadastre a segunda carta")
    c2 = Carta(estado= input("Estado: "),
        codigo= input("Codigo: "),
        nome_cidade= input("Nome da cidade : "),
        população= input("População: "),
        Pib= input("Pib: "), 
        area= input("Área: "), 
        pontos_turistico= input("Pontos Turuisticos: "))

    return c1 ,c2 




def menu(): 

    while True: 
        guardar_mensagem()
        opcao = input("Escolha uma opação: ")

        match opcao: 

            case 1: 
                print("Está funcionando!") 
                guardar_mensagem()
                opcao = input("Escolha uma opação: ")
                
            case 2: 
                pass 

            case 3: 
                pass 

            case 4: 
                pass 

            case 5:
                break
 



