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


def ballRate(ball):
    if(ball.type == e.BALLS.MASTERBALL):
        return 255
    elif(ball.type == e.BALLS.POKEBALL):
        return 1
    elif(ball.type in {e.BALLS.GREATBALL, e.BALLS.SAFARIBALL}):
        return 1.5
    elif(e.BALLS.ULTRABALL):
        return 2
    else:
        return 1


def printShake(x):
    for i in range(x):
        print("Shake...")


def printCaught(b, name):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("Gotcha! " + name + " was caught!")


def toBinaryString(x):
    return str(format(int(x), '04b'))


def fromBinaryStringToNumber(str):
    return int(str, 2)
