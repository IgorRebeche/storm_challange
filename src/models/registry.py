class Registry:
    def __init__(self, entity, attribute, value, isAdded):
        self.entity = entity
        self.attribute = attribute
        self.value = value
        self.isAdded = isAdded
        
    def toTuple(self):
        return (self.entity, self.attribute, self.value, self.isAdded)




class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    
        

thayna = Pessoa()

igor = Pessoa()