import catchRateGen1 as g1
import catchRateGen2 as g2
import catchRateGen3or4 as g3g4
import enums as e
import pokemon
import ball
import DVGen1 as dv
import numpy
import time
start = time.time()

def main():
    rattata = pokemon.pokemon("rattata",100, e.STATUS.ASLEEP,1)
    raichu = pokemon.pokemon("raichu",100, e.STATUS.NONE, 1)
    mewtwo = pokemon.pokemon("mewtwo",100, e.STATUS.NONE,1)
    karpador = pokemon.pokemon("magikarp",100,e.STATUS.NONE,50)

    poke = ball.ball(e.BALLS.POKEBALL)
    great = ball.ball(e.BALLS.GREATBALL)
    ultra = ball.ball(e.BALLS.ULTRABALL)
    master = ball.ball(e.BALLS.MASTERBALL)
    """
    for i in range(2):
        no = i + 1
        print(rattata.name + " #" + str(no) + ":")
        g1.printCaught(g1.throw(poke, rattata), rattata.name)
        print(raichu.name + " #" + str(no) + ":")
        g1.printCaught(g1.throw(poke, raichu), raichu.name)
        print(mewtwo.name + " #" + str(no) + ":")
        g1.printCaught(g1.throw(poke, mewtwo), mewtwo.name)

    for i in range(1):
        no = i + 1
        print(rattata.name + " #" + str(no) + ":")
        g2.printCaught(g2.throw(poke, rattata), rattata.name)
        print(raichu.name + " #" + str(no) + ":")
        g2.printCaught(g2.throw(ultra, raichu), raichu.name)
        print(mewtwo.name + " #" + str(no) + ":")
        g2.printCaught(g2.throw(master, mewtwo), mewtwo.name)

    for i in range(1):
        no = i + 1
        print(rattata.name + " #" + str(no) + ":")
        g3g4.printCaught(g3g4.throw(poke, rattata), rattata.name)
        print(raichu.name + " #" + str(no) + ":")
        g3g4.printCaught(g3g4.throw(ultra, raichu), raichu.name)
        print(mewtwo.name + " #" + str(no) + ":")
        g3g4.printCaught(g3g4.throw(master, mewtwo), mewtwo.name)
    """
    print(karpador.stats.attack.current)
    print(karpador.stats.attack.ev)
    print(karpador.stats.attack.iv)
main()
print("--- %s seconds ---" % (time.time() - start))