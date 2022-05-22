import pokemon
import ball
import math
import random
import enums as e
import utils as u
import shakeLookUpTable as sLT


def statusBonus(pokemon):
    if(u.isFrozenOrAsleep(pokemon)):
        return 10
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 5
    else:
        return 0

def A(pokemon, ball):
    bR = u.ballRate(ball)
    rate = pokemon.catchRate * bR
    bonus = statusBonus(pokemon)

    numerator = ((3*pokemon.hpMax) - (2 * pokemon.hp)) * rate
    denominator = (3*pokemon.hpMax)
    x = math.floor(numerator / denominator)
    result = max(x, 1) + bonus
    return result


def ballShake(x):
    c = 0
    while(3 != 5 and c != 3):
        random.seed()
        r = random.randint(0, 255)
        if(r >= sLT.B(x)):
            break
        else:
            c = c + 1
    return c


def printQuote(x):
    if(x == 0):
        print("Oh no! The POKEMON broke free!")
    elif(x == 1):
        print("Aww! It appeared to be caught!")
    elif(x == 2):
        print("Aargh! Almost had it!")
    elif(x == 3):
        print("Shoot! It was so close too!")

def printShakeAndQuote(x):
    shakeCount = ballShake(x)
    u.printShake(shakeCount)
    printQuote(shakeCount)


def printCaught(b, name):
    if(b):
        print("Shake...\nShake...\nShake and click...")
        print("Gotcha! " + name + " was caught!")


def throw(ball, pokemon):
    random.seed()
    r = random.randint(0, 255)
    a = A(pokemon, ball)
    if(r <= a):
        return True
    else:
        printShakeAndQuote(a)
        return False
