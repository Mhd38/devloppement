import core
from proie import Proies


def setup():
    print("setup----start")
    core.WINDOW_SIZE = [400, 400]
    core.fps = 30

    core.memory("proies", [])
    core.memory("predateur", [])

    core.memory("nbrProies", 100)
    core.memory("nbrPredateur", 10)

    for i in range(0, core.memory("nbrProies")):
        core.memory("proies").append(Proies())


def run():
    core.cleanScreen()
    for p in core.memory("proies"):
        p.show()

    for p in core.memory("proies"):
        p.move()
        p.edge(core.WINDOW_SIZE)

    for p in core.memory("predateur"):
        p.move()
        p.edge(core.WINDOW_SIZE)

    for p in core.memory("predateur"):
        p.manger(core.memory("proies"))


core.main(setup, run)
