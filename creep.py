import random
import pygame
from pygame.math import Vector2


class Creep:

    def __init__(self, largeur=800, hauteur=450):
        self.taille = 5
        self.position = Vector2(random.randint(0+self.taille, largeur-self.taille), random.randint(0+self.taille, hauteur-self.taille))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.masse = 10

    def show(self, screen):
        pygame.draw.circle(screen, self.couleur, [int(self.position.x), int(self.position.y)], self.taille)

    def edge(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        if self.position.x > fenetre[1]:
            self.position.x = 0