from pygame.math import Vector2
import random
import core
from proie import Proies


class Predateur:
    def __init__(self):
        self.position = Vector2(random.randint(0, 400), random.randint(0, 400))
        self.vitesse = Vector2(0, 0)
        self.Acc = Vector2(0, 0)
        self.couleur = (255, 0, 0)
        self.taille = 10
        self.maxV = 6
        self.maxAcc = 4
        self.vision = 100

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.taille)

    def move(self, Proies):
        proiesDansvision = []
        cible = None
        distanceCible = 10000

        for p in Proies:
            if p.position.distance_to(self.position) < self.vision and p.vivante:
                proiesDansvision.append(p)
                if p.position.distance_to(self.position) < distanceCible:
                    cible = p
                    distanceCible = p.position.distance_to(self.position)

        if cible is not None:
            force = cible.position - self.position
            self.Acc = force
        else:
            self.Acc = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

            if self.Acc.length() > self.maxAcc:
                self.Acc.scale_to_length(self.maxAcc)

            self.vitesse = self.vitesse + self.Acc

        if self.vitesse.length() > self.maxV:
            self.vitesse.scale_to_length(self.maxV)

        self.position = self.position + self.vitesse

        self.Acc = Vector2(0, 0)

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0

    def manger(self, Proies):
        for p in Proies:
            if p.position.distance_to(self.position) < self.taille + p.taille:
                p.vivante = False
