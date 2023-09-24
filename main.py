import pokemon
import enums as e
import utils as u
import catchRateGen1 as g1
import catchRateGen2 as g2
import catchRateGen3or4 as g3g4

from gui import *


def main():
    rattata = pokemon.pokemon(
        "rattata", e.GENDERS.MALE, 100, e.STATUS.ASLEEP, 1)
    raichu = pokemon.pokemon("raichu", e.GENDERS.MALE, 100, e.STATUS.NONE, 1)
    mewtwo = pokemon.pokemon(
        "mewtwo", e.GENDERS.UNKNOWN, 100, e.STATUS.NONE, 1)
    karpador = pokemon.pokemon(
        "magikarp", e.GENDERS.MALE, 100, e.STATUS.NONE, 50)

    #pokemons = [rattata, raichu, mewtwo, karpador]
    pokemons = [rattata]

    poke = e.BALL_TYPES.POKEBALL
    great = e.BALL_TYPES.GREATBALL
    ultra = e.BALL_TYPES.ULTRABALL
    master = e.BALL_TYPES.MASTERBALL

    n : int = 1

    print("GENERATION I:")
    for i in range(n):
        no = i + 1
        for p in pokemons:
            print(p.name + " #" + str(no) + ":")
            u.printCaughtGen1(g1.throw(poke, p), p.name)

    print("GENERATION II:")
    for i in range(n):
        no = i + 1
        for p in pokemons:
            print(p.name + " #" + str(no) + ":")
            u.printCaught(g2.throw(poke, p), p.name)

    print("GENERATION III or IV:")
    for i in range(n):
        no = i + 1
        for p in pokemons:
            print(p.name + " #" + str(no) + ":")
            u.printCaught(g3g4.throw(poke, p), p.name)

    for p in pokemons:
        addPokemonImage(p)
    drawGUI()


main()
