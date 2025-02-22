# Třída hráče

import pygame

from settings import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32)) # Placeholder (32x32)
        self.image.fill((255, 0, 0)) # Zelená barva
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2.5
        
    def update(self, keys):
        # Dočasné proměnné pro nový pohyb
        new_x, new_y = self.rect.x, self.rect.y

        # Zkontrolujeme, zda je stisknutý Shift
        speed_multiplier = 2 if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) else 1

        if keys[pygame.K_w]:  # Pohyb nahoru
            new_y -= self.speed * speed_multiplier
        if keys[pygame.K_s]:  # Pohyb dolů
            new_y += self.speed * speed_multiplier
        if keys[pygame.K_a]:  # Pohyb doleva
            new_x -= self.speed * speed_multiplier
        if keys[pygame.K_d]:  # Pohyb doprava
            new_x += self.speed * speed_multiplier

        # Omezíme pohyb na hranice okna
        screen_width, screen_height = WIDTH, HEIGHT
        self.rect.x = max(0, min(new_x, screen_width - self.rect.width))
        self.rect.y = max(0, min(new_y, screen_height - self.rect.height))
