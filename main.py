import pygame
from constants import *
from player import *

def main():
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    

    while True:
        # Olayları kontrol et
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # FPS sınırlayıcı ve zaman ölçüm
        dt = clock.tick(60) / 1000

        # Oyuncuyu güncelle (input'a göre döndür)
        player.update(dt)

        # Ekranı temizle
        screen.fill((0, 0, 0))

        # Oyuncuyu çiz
        player.draw(screen)

        # Ekranı güncelle
        pygame.display.flip()

        

if __name__ == "__main__":
    main()
