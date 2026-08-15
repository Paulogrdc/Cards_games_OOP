from classes.cartas import Carta 

# --- função para guardar as mensagem de opação ---
def guarda_mensagem():
    print("---------------------------SEJA BEM-VINDO AO JOGO DE CARTAS---------------------------")
    print("1-Como funciona o jogo")
    print("2-Cadastrar cartas")
    print("3-Mostrar cartas cadastradas")
    print("4-Jogar")
    print("5-Fechar jogo")



def menu(): 

    while True: 
        guarda_mensagem()
        opcao = input("Escolha uma opação: ")

        match opcao: 

            case 1: 
                print("Está funcionando!") 
                
            case 2: 

                c1= Carta()
                c2 = Carta()

            case 3: 
                pass 

            case 4: 
                pass 

            case 5:
                break
 



