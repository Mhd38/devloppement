import random
import pygame
from pygame.math import Vector2

import core


class Avatar:

    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(940, 500)
        self.taille = 20
        self.masse = 10
        self.vitesse = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.k = 0.001
        self.tailleMax = 300
        self.vitessemin = 10
        self.vitessemax = 20
        self.AccMax = 0.5
        self.m = 0.5

    def move(self):
        '''Bilan des forces'''
        x = Vector2(core.getMouseLeftClick())
        v = Vector2((x - self.position))
        u = v.normalize()
        l = v.length()
        fr = Vector2(self.k * (l - self.m) * u)

        '''Vecteur Vitesse'''
        self.vitesse = self.vitesse + fr
        fr = Vector2(0, 0)

        '''deplacement'''
        self.position = self.position + self.vitesse

    def show(self):
        core.Draw.circle(self.color, [int(self.position.x), int(self.position.y)], self.taille)

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0