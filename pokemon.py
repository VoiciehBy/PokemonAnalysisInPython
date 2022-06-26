import pokebase
import generateStats as gS


class pokemon:
    def __init__(self, name, level, status, hp):
        self.pokebasePokemon = pokebase.pokemon(name)
        self.name = name.upper()
        self.level = level
        self.status = status
        self.stats = gS.generateStats(self)
        self.hpMax = self.stats.hp.current
        self.hp = self.hpMax * (hp/100)
        self.catchRate = self.pokebasePokemon.species.capture_rate
    def getBaseStat(self,id):
        return self.pokebasePokemon.stats[id].base_stat
    def getBaseHP(self):
        return self.getBaseStat(0)
    def getBaseAttack(self):
        return self.getBaseStat(1)
    def getBaseDefense(self):
        return self.getBaseStat(2)
    def getBaseSpecialAttack(self):
        return self.getBaseStat(3)
    def getBaseSpecialDefense(self):
        return self.getBaseStat(4)
    def getBaseSpeed(self):
        return self.getBaseStat(5)