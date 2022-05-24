import random
import utils as u
import math


def generateIV():
    random.seed()
    return random.randint(0, 15)


def generateHPIV(attack, defense, speed, special):
    a = u.toBinaryString(attack)[3]
    d = u.toBinaryString(defense)[3]
    sp = u.toBinaryString(speed)[3]
    sp1 = u.toBinaryString(special)[3]
    s = a + d + sp + sp1
    return u.fromBinaryStringToNumber(s)


def generateStat(pokemon,id):
    hpIV = generateIV()
    baseHP = pokemon.pokebasePokemon.stats[id].base_stat
    EV = pokemon.pokebasePokemon.stats[id].effort
    EVSqrt = math.sqrt(EV)
    level = 1
    numerator = ((baseHP + hpIV) * 2 + math.floor(EV / 4) * level)
    denominator = 100
    result = math.floor(numerator/denominator) + 5
    return result


def generateHPStat(pokemon,attackIV,defenseIV,speedIV,SpecialIV):
    hpIV = generateHPIV(1, 1, 1, 1)
    baseHP = pokemon.pokebasePokemon.stats[0].base_stat
    EV = pokemon.pokebasePokemon.stats[0].effort
    EVSqrt = math.sqrt(EV)
    level = 1
    numerator = ((baseHP + hpIV) * 2 + math.floor(EV / 4) * level)
    denominator = 100
    result = math.floor(numerator/denominator) + level + 10
    return result
