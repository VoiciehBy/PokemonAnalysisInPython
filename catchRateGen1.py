import ball
import enums as e
import random
import pokemon
import math
import utils as u
import quotes as q


def N(ball) -> int:
    random.seed()

    if(ball.type == e.BALLS.POKEBALL):
        return random.randint(0, 255)
    elif(ball.type == e.BALLS.GREATBALL):
        return random.randint(0, 200)
    elif(ball.type in {e.BALLS.SAFARIBALL, e.BALLS.ULTRABALL}):
        return random.randint(0, 150)
    else:
        return -1


def bShake(ball) -> int:
    if(ball.type == e.BALLS.POKEBALL):
        return 255
    elif(ball.type == e.BALLS.GREATBALL):
        return 200
    else:
        return 150


def S(pokemon) -> int:
    if(u.isFrozenOrAsleep(pokemon)):
        return 10
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 5
    else:
        return 0


def F(pokemon, ball) -> int:
    bC: int = 8 if(ball.type == e.BALLS.GREATBALL) else 12
    return math.floor((pokemon.hpMax*255*4)/(pokemon.hp * bC))


def ballShake(pokemon, ball) -> int:
    bS: int = bShake(ball)
    d: int = math.floor((pokemon.catchRate*100)/bS)
    if(d >= 256):
        return 3
    else:
        f: int = F(pokemon, ball)
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


def statusThreshold(pokemon) -> int:
    return 25 if(u.isFrozenOrAsleep(pokemon)) else 12


def printQuote(x):
    print(q.QUOTES[x])


def printShakeAndQuote(pokemon, ball):
    u.printShake(ballShake(pokemon, ball))
    printQuote(ballShake(pokemon, ball))


def throw(ball, pokemon) -> bool:
    if(ball.type == e.BALLS.MASTERBALL):
        return True
    else:
        n: int = N(ball)
        if(u.hasNegativeStatus(pokemon) and n < statusThreshold(pokemon)):
            return True
        elif(n - statusThreshold(pokemon) > pokemon.catchRate):
            printShakeAndQuote(pokemon, ball)
            return False
        else:
            m = u.newRandomNewSeed(0, 255)
            f : int = F(pokemon, ball)
            if(f >= m):
                return True
            else:
                printShakeAndQuote(pokemon, ball)
                return False
