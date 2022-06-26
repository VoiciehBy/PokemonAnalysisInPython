import random
import utils as u
import math


def generateDV():
    return u.newRandomNewSeed(0, 15)


def generateHPDV(attack, defense, speed, special):
    a = u.toBinaryString(attack)[3]
    d = u.toBinaryString(defense)[3]
    sp = u.toBinaryString(speed)[3]
    sp1 = u.toBinaryString(special)[3]
    s = a + d + sp + sp1
    return u.fromBinaryStringToNumber(s)


def Stat(pokemon, baseStat, statEXP, dv, isHP):
    statEXPSqrt = math.sqrt(statEXP)
    level = pokemon.level
    numerator = (((baseStat + dv) * 2) + math.floor((statEXPSqrt/4))) * level
    denominator = 100
    result = math.floor(numerator/denominator)
    if isHP is True:
        result = result + level + 10
    else:
        result += 5
    return result


def HPStat(pokemon, statEXP, hpDV):
    return Stat(pokemon, pokemon.getBaseHP(), statEXP, hpDV, True)


def AttackStat(pokemon, statEXP, dv):
    return Stat(pokemon, pokemon.getBaseAttack(), statEXP, dv, False)


def DefenseStat(pokemon, statEXP, dv):
    return Stat(pokemon, pokemon.getBaseDefense(), statEXP, dv, False)


def SpecialAttackStat(pokemon, statEXP, dv):
    return Stat(pokemon, pokemon.getBaseSpecialAttack(), statEXP, dv, False)


def SpecialDefensekStat(pokemon, statEXP, dv):
    return Stat(pokemon, pokemon.getBaseSpecialDefense(), statEXP, dv, False)


def SpeedStat(pokemon, statEXP, dv):
    return Stat(pokemon, pokemon.getBaseSpeed(), statEXP, dv, False)
