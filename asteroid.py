from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
        screen,      
        "white",       
        self.position, 
        self.radius,   
        2              
    )

    def update(self, dt):
        self.position += self.velocity * dt

    def split_ast(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = vel1

            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = vel2

            
        

