import pokebase

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Pokemon Analysis")
window.geometry("100x400")

windowFrame = ttk.Frame(window)

images = []
labels = []


def destroyEveryLabelAndClear():
    for i in label:
        i.destroy()
    labels.clear()


def addPokemonImage(pokemon):
    images.append(PhotoImage(data=pokemon.sprite))


def drawGUI():
    windowFrame.grid()
    for i in images:
        labels.append(ttk.Label(image=i))
    for l in labels:
        l.grid()
    window.mainloop()
