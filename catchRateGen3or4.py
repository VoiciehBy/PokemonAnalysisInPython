import pokemon
import math
import random
import utils as u

from quotes import QUOTES


def statusBonus(pokemon) -> float:
    if(u.isFrozenOrAsleep(pokemon)):
        return float(2.0)
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return float(1.5)
    else:
        return float(1.0)


def A(pokemon, ball_type) -> float:
    bR: int = u.ballRate(ball_type)
    rate: int = pokemon.catchRate
    bonus: float = statusBonus(pokemon)

    numerator: float = ((3*pokemon.hpMax) - (2 * pokemon.hp)) * rate * bR
    denominator: float = (3*pokemon.hpMax)
    numerator *= 1.0
    denominator *= 1.0
    result: float = float(float(numerator/denominator) * bonus)
    return float(result)


def B(x) -> float:
    numerator: float = 1048560.0
    c: float = 16711680.0
    denominator: float = math.sqrt(math.sqrt(c/x))
    result: float = float(numerator / denominator)
    return float(result)


def ballShake(x: int) -> int:
    c: int = 0
    while(3 != 5 and c != 3):
        random.seed()
        r: int = random.randint(0, 65535)
        if(r >= B(x)):
            break
        else:
            c = c + 1
    return int(c)


def printQuote(x: int):
    if(x == 0):
        print(QUOTES[4])
    elif(x == 1):
        print(QUOTES[2])
    elif(x == 2):
        print(QUOTES[5])
    elif(x == 3):
        print(QUOTES[6])


def printShakeAndQuote(x):
    shakeCount: int = ballShake(x)
    u.printShake(shakeCount)
    printQuote(shakeCount)


def printCaught(b, name):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("Gotcha! " + name + " was caught!")


def throw(ball_type, pokemon) -> bool:
    random.seed()
    r: int = random.randint(0, 255)
    a: float = A(pokemon, ball_type)

    if((a >= 255) or (ballShake(a) == 4)):
        printCaught(True, pokemon.name)
        return True
    else:
        printShakeAndQuote(a)
        return False
