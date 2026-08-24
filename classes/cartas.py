

class Carta:
    def __init__(self, estado:str , codigo:str, nome_cidade:str, população:int|float , pib:int|float , area: int|float , pontos_turistico:int ):
         self._estado = estado 
         self._codigo = None
         self._nome_cidade = nome_cidade 
         self._populacao = população 
         self._pib = pib 
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
    def populacao(self): 
         return self._populacao

    @populacao.setter
    def populacao(self,valor): 
         if valor <= 0: 
              raise ValueError("Valor invalido! ")
         else: 
              self._populacao = valor

    @property
    def pib(self): 
         return self._pib

    @pib.setter 
    def pib(self,valor): 
         if valor <= 0: 
              raise ValueError("Valor invalido!")
         else: 
              self._pib = valor


    def densidade_populacional(self): #população/area 
         return self._populacao/self._area 


    def pib_per_capita(self): # pib/população
         return self.pib/self.populacao


    def super_poder(self): #fazer uma media aritimetrica 
         pib_per_capita = self.pib_per_capita()
         densidade_populacional = self.densidade_populacional() 

         super_poder = pib_per_capita + densidade_populacional + self.populacao + self._area + self.pib +  self._pontos_turistico/6 

         return super_poder

    # Polirmorfismo de overlooding tipo operador
    def __lt__(self, outro):
         super_poder = self.super_poder()

         if self.super_poder < outro.super_poder: 
               return True 
         else: 
               return False

    def __eq__(self, outro):
         super_poder = self.super_poder()
         if self.super_poder ==  outro.super_poder: 
               return True 
         else: 
              return False 

    def __gt__(self, outro):
         super_poder = self.super_poder()
         if self.super_poder > outro.super_poder: 
               return True 
         else: 
              return False











