from classes.cartas import Carta 
from rich import inspect 


def main(): 
    c1 = Carta(
        estado = "Rj", 
        codigo = "A1", 
        nome_cidade = "Rio de janeiro", 
        população= 1_000, 
        pib=10_000, 
        area=1200, 
        pontos_turistico= 23)

    c1.população = 3000
    c1.pib = 20_000

    print(f"A densidade Populacional é: {c1.densidade_populacional()}")
    print(f"O Pib per capoita é: {c1.pib_per_capita():.2f}")
    print(f"O Super Poder é: {c1.super_poder():.2f}")

    #inspect(c1,private=True, methods=True ) 



if __name__ == "__main__": 
    main()


