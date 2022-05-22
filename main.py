import catchRateGen1 as g1
import catchRateGen2 as g2
import catchRateGen3or4 as g3g4
import enums as e
import pokemon
import ball


def main():
    rattata = pokemon.pokemon("rattata", e.STATUS.ASLEEP, 264, 264/264, 255)
    raichu = pokemon.pokemon("raichu", e.STATUS.NONE, 324, 324, 75)
    mewtwo = pokemon.pokemon("mewtwo", e.STATUS.NONE, 416, 416, 3)

    poke = ball.ball(e.BALLS.POKEBALL)
    great = ball.ball(e.BALLS.GREATBALL)
    ultra = ball.ball(e.BALLS.ULTRABALL)
    master = ball.ball(e.BALLS.MASTERBALL)

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

main()
