from classes.cartas import Carta 
from rich import inspect 


def main(): 
    c1 = Carta("Rj","A1", "Rio de janeiro", 1000, 10000, 1200, 23)

    c1.população = 3000

    inspect(c1,private=True, methods=True ) 



if __name__ == "__main__": 
    main()


