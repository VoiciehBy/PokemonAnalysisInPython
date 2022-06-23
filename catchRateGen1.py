import pokemon
import ball
import math
import random
import enums as e
import utils as u
import quotes as q


def N(ball):
    random.seed()

    if(ball.type == e.BALLS.POKEBALL):
        return random.randint(0, 255)
    elif(ball.type == e.BALLS.GREATBALL):
        return random.randint(0, 200)
    elif(ball.type == e.BALLS.SAFARIBALL or e.BALLS.ULTRABALL):
        return random.randint(0, 150)
    else:
        return -1


def bShake(ball):
    if(ball.type == e.BALLS.POKEBALL):
        return 255
    elif(ball.type == e.BALLS.GREATBALL):
        return 200
    else:
        return 150


def S(pokemon):
    if(u.isFrozenOrAsleep(pokemon)):
        return 10
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 5
    else:
        return 0


def bCatch(ball):
    if(ball.type == e.BALLS.GREATBALL):
        return 8
    else:
        return 12


def F(pokemon, ball):
    bC = bCatch(ball)
    return math.floor((pokemon.hpMax*255*4)/(pokemon.hp * bC))


def ballShake(pokemon, ball):
    bS = bShake(ball)
    d = math.floor((pokemon.catchRate*100)/bS)
    if(d >= 256):
        return 3
    else:
        f = F(pokemon, ball)
        s = S(pokemon)
        x = math.floor((d*f)/255) + s
        if(x < 10):
            return 0
        elif(x < 30):
            return 1
        elif(x < 70):
            return 2
        else:
            return 3


def statusThreshold(pokemon):
    if(u.isFrozenOrAsleep(pokemon)):
        return 25
    else:
        return 12


def printQuote(x):
    print(q.QUOTES[x])

def printShakeAndQuote(pokemon, ball):
    u.printShake(ballShake(pokemon, ball))
    printQuote(ballShake(pokemon, ball))


def printCaught(b, name):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("All right! " + name + " was caught!")


def throw(ball, pokemon):

    if(ball.type == e.BALLS.MASTERBALL):
        return True
    else:
        n = N(ball)
        if(u.hasNegativeStatus(pokemon) and n < statusThreshold(pokemon)):
            return True
        elif(n - statusThreshold(pokemon) > pokemon.catchRate):
            printShakeAndQuote(pokemon, ball)
            return False
        else:
            random.seed()
            m = random.randint(0, 255)
            f = F(pokemon, ball)
            if(f >= m):
                return True
            else:
                printShakeAndQuote(pokemon, ball)
                return False
