import pygame
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.rotation = 0

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def check_collision(self, other):
        # Check if the distance between the two circles is less than the sum of their radii
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True