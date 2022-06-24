import pokebase
import generateStats as gS


class pokemon:
    def __init__(self, name, level, status, hp):
        self.pokebasePokemon = pokebase.pokemon(name)
        self.name = name.upper()
        self.level = level
        self.status = status
        self.baseHP = self.pokebasePokemon.stats[0].base_stat
        self.baseAttack = self.pokebasePokemon.stats[1].base_stat
        self.baseDefense = self.pokebasePokemon.stats[2].base_stat
        self.baseSpecialAttack = self.pokebasePokemon.stats[3].base_stat
        self.baseSpecialDefense = self.pokebasePokemon.stats[4].base_stat
        self.baseSpeed = self.pokebasePokemon.stats[5].base_stat
        self.stats = gS.generateStats(self)
        self.hpMax = self.stats.hp.current
        self.hp = self.hpMax * (hp/100)
        self.catchRate = self.pokebasePokemon.species.capture_rate
