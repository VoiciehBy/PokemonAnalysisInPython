import pokemon 
import enums as e

def isFrozenOrAsleep(pokemon):
    if(pokemon.status in {e.STATUS.FROZEN, e.STATUS.ASLEEP}):
        return True
    else:
        return False


def isParalyzedOrBurnedOrPoisoned(pokemon):
    if(pokemon.status in {e.STATUS.PARALYZED, e.STATUS.BURNED, e.STATUS.POISONED}):
        return True
    else:
        return False

def hasNegativeStatus(pokemon):
    if (isFrozenOrAsleep(pokemon) or isParalyzedOrBurnedOrPoisoned(pokemon)):
        return True
    else:
        return False

def printShake(x):
    for i in range(x):
        print("Shake...")