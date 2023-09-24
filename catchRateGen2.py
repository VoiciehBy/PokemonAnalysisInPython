import pokemon
import math
import random
import utils as u
import shakeLookUpTable as sLT

from enums import BALL_TYPES
from quotes import QUOTES


def statusBonus(pokemon: pokemon) -> int:
    if(u.isFrozenOrAsleep(pokemon)):
        return 10
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 5
    else:
        return 0


def A(pokemon: pokemon, ball_type: BALL_TYPES) -> int:
    bR: int = u.ballRate(ball_type)
    rate: int = pokemon.catchRate * bR
    bonus: int = statusBonus(pokemon)

    numerator: int = ((3 * pokemon.hpMax) - (2 * pokemon.hp)) * rate
    denominator: int = (3 * pokemon.hpMax)
    x: int = math.floor(numerator / denominator)
    result: int = max(x, 1) + bonus
    return result


def ballShake(x: int) -> int:
    c: int = 0
    while(3 != 5 and c != 3):
        random.seed()
        r: int = random.randint(0, 255)
        if(r >= sLT.B(x)):
            break
        else:
            c = c + 1
    return c


def printQuote(x):
    if(x == 0):
        print(QUOTES[4])
    elif(x == 1):
        print(QUOTES[2])
    elif(x == 2):
        print(QUOTES[5])
    elif(x == 3):
        print(QUOTES[x])


def printShakeAndQuote(x: int):
    shakeCount: int = ballShake(x)
    u.printShake(shakeCount)
    printQuote(shakeCount)


def throw(ball_type: BALL_TYPES, pokemon: pokemon):
    random.seed()
    r: int = random.randint(0, 255)
    a: int = A(pokemon, ball_type)
    if(r <= a):
        return True
    else:
        printShakeAndQuote(a)
        return False
