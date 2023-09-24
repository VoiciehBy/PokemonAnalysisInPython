import DVGen1 as dv
import StatEXPGen1 as sEXP


def generateStats(pokemon) -> dict:
    attackDV: int = dv.generateDV()
    defenseDV: int = dv.generateDV()
    speedDV: int = dv.generateDV()
    specialDV: int = dv.generateDV()
    hpDV: int = dv.generateHPDV(attackDV, defenseDV, speedDV, specialDV)

    hpStatEXP: int = sEXP.generateStatEXP()
    attackStatEXP: int = sEXP.generateStatEXP()
    defenseStatEXP: int = sEXP.generateStatEXP()
    specialStatEXP: int = sEXP.generateStatEXP()
    speedStatEXP: int = sEXP.generateStatEXP()

    hp: int = dv.HPStat(pokemon, hpStatEXP, hpDV)
    attack: int = dv.AttackStat(pokemon, attackStatEXP, attackDV)
    defense: int = dv.DefenseStat(pokemon, defenseStatEXP, defenseDV)
    specialAttack: int = dv.SpecialAttackStat(
        pokemon, specialStatEXP, specialDV)
    specialDefense: int = dv.SpecialAttackStat(
        pokemon, specialStatEXP, specialDV)
    speed: int = dv.SpeedStat(pokemon, speedStatEXP, speedDV)

    hpStat: dict = {
        "current": hp,
        "ev": hpStatEXP,
        "iv": hpDV
    }
    attackStat: dict = {
        "current": attack,
        "ev": attackStatEXP,
        "iv": attackDV
    }
    defenseStat: dict = {
        "current": defense,
        "ev": defenseStatEXP,
        "iv": defenseDV
    }
    specialAttackStat: dict = {
        "current": specialAttack,
        "ev": specialStatEXP,
        "iv": specialDV
    }
    specialDefenseStat: dict = {
        "current": specialDefense,
        "ev": specialStatEXP,
        "iv": specialDV
    }
    speedStat: dict = {
        "current": speed,
        "ev": speedStatEXP,
        "iv": speedDV
    }

    result: dict = {
        "hp": hpStat,
        "attack": attackStat,
        "defense": defenseStat,
        "specialAttack": specialAttackStat,
        "specialDefense": specialDefenseStat,
        "speed": speedStat
    }
    return result
