import DVGen1 as dv
import StatEXPGen1 as sEXP
import stats as s


def generateStats(pokemon):
    attackDV = dv.generateDV()
    defenseDV = dv.generateDV()
    speedDV = dv.generateDV()
    specialDV = dv.generateDV()
    hpDV = dv.generateHPDV(attackDV, defenseDV, speedDV, specialDV)

    hpStatEXP = sEXP.generateStatEXP()
    attackStatEXP = sEXP.generateStatEXP()
    defenseStatEXP = sEXP.generateStatEXP()
    specialStatEXP = sEXP.generateStatEXP()
    speedStatEXP = sEXP.generateStatEXP()

    hp = dv.HPStat(pokemon, hpStatEXP, hpDV)
    attack = dv.AttackStat(pokemon, attackStatEXP, attackDV)
    defense = dv.DefenseStat(pokemon, defenseStatEXP, defenseDV)
    specialAttack = dv.SpecialAttackStat(pokemon, specialStatEXP, specialDV)
    specialDefense = dv.SpecialAttackStat(pokemon, specialStatEXP, specialDV)
    speed = dv.SpeedStat(pokemon, speedStatEXP, speedDV)

    hpStat = s.stat(hp, hpStatEXP, hpDV)
    attackStat = s.stat(attack, attackStatEXP, attackDV)
    defenseStat = s.stat(defense, defenseStatEXP, defenseDV)
    specialAttackStat = s.stat(specialAttack, specialStatEXP, specialDV)
    specialDefenseStat = s.stat(specialDefense, specialStatEXP, specialDV)
    speedStat = s.stat(speed, speedStatEXP, speedDV)

    return s.stats(hpStat, attackStat, defenseStat, specialAttackStat, specialDefenseStat, speedStat)
