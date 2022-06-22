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
        self.hp = hp
        self.catchRate = self.pokebasePokemon.species.capture_rate

    def getBaseHP(self):
        return self.pokebasePokemon.stats[0].base_stat

    def getBaseAttack(self):
        return self.pokebasePokemon.stats[1].base_stat

    def getBaseDefense(self):
        return self.pokebasePokemon.stats[2].base_stat

    def getBaseSpecialAttack(self):
        return self.pokebasePokemon.stats[3].base_stat

    def getBaseSpecialDefense(self):
        return self.pokebasePokemon.stats[4].base_stat

    def getBaseSpeed(self):
        return self.pokebasePokemon.stats[5].base_stat
