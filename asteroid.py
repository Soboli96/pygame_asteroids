import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

        def __init__(self, x, y, radius):
            super().__init__(x, y, radius)
        
        def split(self):
            if self.radius > ASTEROID_MIN_RADIUS:
                    new_radius = self.radius - ASTEROID_MIN_RADIUS
                    for _ in range(2):
                        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                        new_velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2
                        new_asteroid.velocity = new_velocity
                    self.kill()
            else:
                self.kill()