import pokebase

class pokemon:
    #def __init__(self, name, status, hpMax, hp, catchRate):
    #    self.name = name.upper()
    #    self.status = status
    #    self.hpMax = hpMax
    #    self.hp = hp
    #    self.catchRate = catchRate
    
    def __init__(self, name, status, hpMax, hp):
        self.pokebasePokemon = pokebase.pokemon(name)
        self.name = name.upper()
        self.status = status
        self.hpMax = hpMax
        self.hp = hp
        self.catchRate = self.pokebasePokemon.species.capture_rate