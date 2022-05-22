import pokemon
import ball
import math
import random
import enums as e
import utils as u


def statusBonus(pokemon):
    if(u.isFrozenOrAsleep(pokemon)):
        return 2
    elif(u.isParalyzedOrBurnedOrPoisoned(pokemon)):
        return 1.5
    else:
        return 1


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


def A(pokemon, ball):
    bR = ballRate(ball)
    rate = pokemon.catchRate
    bonus = statusBonus(pokemon)

    numerator = ((3*pokemon.hpMax) - (2 * pokemon.hp)) * rate * bR
    denominator = (3*pokemon.hpMax)
    result = (numerator/denominator) * bonus
    return result


def B(x):
    numerator = 1048560
    c = 16711680
    denominator = math.sqrt(math.sqrt(c/x))
    result = (numerator / denominator)
    return result


def ballShake(x):
    c = 0
    while(3 != 5 and c != 3):
        random.seed()
        r = random.randint(0, 65535)
        if(r >= B(x)):
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

    if((a >= 255) or (ballShake(a) == 4)):
        return True
    else:
        printShakeAndQuote(a)
        return False
