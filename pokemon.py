import pokebase
import enums as e
import generateStats as gS


class pokemon:
    def __init__(self, name : str, gender : e.GENDERS, lvl: int, status : e.STATUS, hp : int):
        self.pokebasePokemon: pokebase.interface.APIResource = pokebase.pokemon(name)
        self.name : str = name.upper()
        self.gender: e.GENDERS = gender
        self.lvl : int = lvl
        self.status : e.STATUS = status
        
        self.baseHP = self.pokebasePokemon.stats[0].base_stat
        self.baseAttack = self.pokebasePokemon.stats[1].base_stat
        self.baseDefense = self.pokebasePokemon.stats[2].base_stat
        self.baseSpecialAttack = self.pokebasePokemon.stats[3].base_stat
        self.baseSpecialDefense = self.pokebasePokemon.stats[4].base_stat
        self.baseSpeed = self.pokebasePokemon.stats[5].base_stat

        self.stats : dict = gS.generateStats(self)
        self.hpMax : int = self.stats["hp"]["current"]
        self.hp : int = self.hpMax * (hp/100)
        
        self.catchRate : int = self.pokebasePokemon.species.capture_rate
        self.sprite = pokebase.SpriteResource("pokemon", self.pokebasePokemon.id).img_data
