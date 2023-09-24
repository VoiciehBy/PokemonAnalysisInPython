import utils as u
import pokemon
import math


def generateDV() -> int:
    return u.newRandomNewSeed(0, 15)


def generateHPDV(attack: int, defense: int, speed: int, special: int) -> int:
    a: str = u.toBinaryString(attack)[3]
    d: str = u.toBinaryString(defense)[3]
    sp: str = u.toBinaryString(speed)[3]
    sp1: str = u.toBinaryString(special)[3]
    s: str = a + d + sp + sp1
    return u.fromBinaryStringToNumber(s)


def Stat(pokemon: pokemon, baseStat: int, statEXP: int, dv: int, isHP: bool) -> int:
    statEXPSqrt: float = math.sqrt(statEXP)
    level: int = pokemon.lvl
    numerator: int = (((baseStat + dv) * 2) +
                      math.floor((statEXPSqrt/4))) * level
    denominator: int = 100
    result: int = math.floor(numerator/denominator)
    if isHP is True:
        result = result + level + 10
    else:
        result += 5
    return result


def HPStat(pokemon: pokemon, statEXP: int, hpDV: int) -> int:
    return Stat(pokemon, pokemon.baseHP, statEXP, hpDV, True)


def AttackStat(pokemon: pokemon, statEXP: int, dv: int) -> int:
    return Stat(pokemon, pokemon.baseAttack, statEXP, dv, False)


def DefenseStat(pokemon: pokemon, statEXP: int, dv: int) -> int:
    return Stat(pokemon, pokemon.baseDefense, statEXP, dv, False)


def SpecialAttackStat(pokemon: pokemon, statEXP: int, dv: int) -> int:
    return Stat(pokemon, pokemon.baseSpecialAttack, statEXP, dv, False)


def SpecialDefensekStat(pokemon: pokemon, statEXP: int, dv: int) -> int:
    return Stat(pokemon, pokemon.baseSpecialDefense, statEXP, dv, False)


def SpeedStat(pokemon, statEXP, dv) -> int:
    return Stat(pokemon, pokemon.baseSpeed, statEXP, dv, False)
