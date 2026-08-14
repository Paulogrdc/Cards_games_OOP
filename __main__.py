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

    #inspect(c1,private=True, methods=True ) 



if __name__ == "__main__": 
    main()


