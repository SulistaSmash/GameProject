from enum import Enum
class character:
    def __init__(self,altura,largura,nome):
        self._altura=altura;
        self._largura=largura;
        self._nome=nome;
        self._attacks=[];

    def largura(self):
        return self._largura;
    
    def altura (self):
        return self._altura;
    def nome (self):
        return self._nome;
    
    def attacks(self):
        return self._attacks;

class characterName (Enum):
    Generic = 1
    Marceline = 2
    


    
