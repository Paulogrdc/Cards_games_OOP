

class Carta:
    def __init__(self, estado:str , codigo:str, nome_cidade:str, população:int|float , pib:int|float , area: int|float , pontos_turistico:int ):
         self._estado = estado 
         self._codigo = None
         self._nome_cidade = nome_cidade 
         self._população = população #
         self._pib = pib #
         self._area = area 
         self._pontos_turistico = pontos_turistico 

         self.codigo = codigo

    #@property
    #def codigo(self):
         #return self._codigo
    
    #@codigo.setter
    #def codigo(self,valor):
         #letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
         #numeros = [0,1,2,3,4]
         #if valor in numeros and valor.upper() in letras: 
          #    self._codigo = valor
         #else: 
          #    raise ValueError("Código invalido! O codigo deve ser composto por um número entre 0 até 4 e uma letra entre A até J.")


    @property 
    def população(self): 
         return self._população 

    @população.setter
    def população(self,valor): 
         if valor <= 0: 
              raise ValueError("Valor invalido! ")
         else: 
              self._população = valor

    @property
    def pib(self): 
         return self._pib

    @pib.setter 
    def pib(self,valor): 
         if valor <= 0: 
              raise ValueError("Valor invalido!")
         else: 
              self._pib = valor


    def densidade_populacional(self): 
         pass 


    def pib_per_capita(self): 
         pass 


    def super_poder(self): 
         pass












