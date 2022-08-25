
class character:
    def __init__(self,altura,largura,nome,vida,attacks):
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
        
    def vida(self):
        return self._vida;



    Example = character(1.65,1.10,characterName.Marceline,2000)



    
