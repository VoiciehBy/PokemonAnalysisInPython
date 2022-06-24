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


def Stat(pokemon, baseStat, statEXP, dv):
    statEXPSqrt = math.sqrt(statEXP)
    level = pokemon.level
    numerator = (((baseStat + dv) * 2) + math.floor((statEXPSqrt/4))) * level
    denominator = 100
    result = math.floor(numerator/denominator) + 5
    return result


def HPStat(pokemon, statEXP, hpDV):
    baseHP = pokemon.baseHP
    statEXPSqrt = math.sqrt(statEXP)
    level = pokemon.level

    numerator = (((baseHP + hpDV) * 2) + math.floor((statEXPSqrt/4))) * level
    denominator = 100
    result = math.floor(numerator/denominator) + level + 10
    return result


def AttackStat(pokemon, statExp, dv):
    return Stat(pokemon, pokemon.baseAttack, statExp, dv)


def DefenseStat(pokemon, statExp, dv):
    return Stat(pokemon, pokemon.baseDefense, statExp, dv)


def SpecialAttackStat(pokemon, statExp, dv):
    return Stat(pokemon, pokemon.baseSpecialAttack, statExp, dv)


def SpecialDefensekStat(pokemon, statExp, dv):
    return Stat(pokemon, pokemon.baseSpecialDefense, statExp, dv)


def SpeedStat(pokemon, statExp, dv):
    return Stat(pokemon, pokemon.baseSpeed, statExp, dv)
