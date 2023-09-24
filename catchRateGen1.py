import random
import pokemon
import math
import utils as u

from enums import BALL_TYPES
from quotes import QUOTES


def N(ball_type: BALL_TYPES) -> int:
    random.seed()

    if(ball_type == BALL_TYPES.POKEBALL):
        return random.randint(0, 255)
    elif(ball_type == BALL_TYPES.GREATBALL):
        return random.randint(0, 200)
    elif(ball_type in {BALL_TYPES.SAFARIBALL, BALL_TYPES.ULTRABALL}):
        return random.randint(0, 150)
    else:
        return -1


def bShake(ball_type: BALL_TYPES) -> int:
    if(ball_type == BALL_TYPES.POKEBALL):
        return 255
    elif(ball_type == BALL_TYPES.GREATBALL):
        return 200
    else:
        return 150


def S(pokemon: pokemon) -> int:
    if(u.isFrozenOrAsleep(pokemon)):
        return 10
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 5
    else:
        return 0


def F(pokemon: pokemon, ball_type: BALL_TYPES) -> int:
    bC: int = 8 if(ball_type == BALL_TYPES.GREATBALL) else 12
    return math.floor((pokemon.hpMax*255*4)/(pokemon.hp * bC))


def ballShake(pokemon: pokemon, ball_type: BALL_TYPES) -> int:
    bS: int = bShake(ball_type)
    d: int = math.floor((pokemon.catchRate*100)/bS)
    if(d >= 256):
        return 3
    else:
        f: int = F(pokemon, ball_type)
        s: int = S(pokemon)
        x: int = math.floor((d*f)/255) + s
        if(x < 10):
            return 0
        elif(x < 30):
            return 1
        elif(x < 70):
            return 2
        else:
            return 3


def statusThreshold(pokemon: pokemon) -> int:
    return 25 if(u.isFrozenOrAsleep(pokemon)) else 12


def printQuote(x):
    print(QUOTES[x])


def printShakeAndQuote(pokemon: pokemon, ball_type: BALL_TYPES):
    u.printShake(ballShake(pokemon, ball_type))
    printQuote(ballShake(pokemon, ball_type))


def throw(ball_type: BALL_TYPES, pokemon: pokemon) -> bool:
    print(type(ball_type))
    if(ball_type == BALL_TYPES.MASTERBALL):
        return True
    else:
        n: int = N(ball_type)
        if(u.hasNegativeStatus(pokemon) and n < statusThreshold(pokemon)):
            return True
        elif(n - statusThreshold(pokemon) > pokemon.catchRate):
            printShakeAndQuote(pokemon, ball_type)
            return False
        else:
            m = u.newRandomNewSeed(0, 255)
            f: int = F(pokemon, ball_type)
            if(f >= m):
                return True
            else:
                printShakeAndQuote(pokemon, ball_type)
                return False
