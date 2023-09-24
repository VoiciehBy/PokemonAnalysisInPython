import pokemon
import enums as e
import random


def isFrozenOrAsleep(pokemon) -> bool:
    if(pokemon.status in {e.STATUS.FROZEN, e.STATUS.ASLEEP}):
        return True
    else:
        return False


def isParalyzedOrBurnedOrPoisoned(pokemon) -> bool:
    if(pokemon.status in {e.STATUS.PARALYZED, e.STATUS.BURNED, e.STATUS.POISONED}):
        return True
    else:
        return False


def hasNegativeStatus(pokemon) -> bool:
    if (isFrozenOrAsleep(pokemon) or isParalyzedOrBurnedOrPoisoned(pokemon)):
        return True
    else:
        return False


def ballRate(ball_type : e.BALL_TYPES) -> int:
    if(ball_type == e.BALL_TYPES.MASTERBALL):
        return 255
    elif(ball_type == e.BALL_TYPES.POKEBALL):
        return 1
    elif(ball_type in {e.BALL_TYPES.GREATBALL, e.BALL_TYPES.SAFARIBALL}):
        return 1.5
    elif(ball_type == e.BALL_TYPES.ULTRABALL):
        return 2
    else:
        return 1


def printShake(x : int):
    for i in range(x):
        print("Shake...")


def printCaughtGen1(b : bool, name : str):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("All right! " + name + " was caught!")


def printCaught(b : bool, name : str):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("Gotcha! " + name + " was caught!")


def toBinaryString(x : int) -> str:
    return str(format(int(x), '04b'))


def fromBinaryStringToNumber(str) -> int:
    return int(str, 2)


def newRandomNewSeed(a : int, b : int) -> int:
    random.seed()
    return random.randint(a, b)
