import pygame

from settings import WIDTH, HEIGHT, FPS
from player import Player
from tilemap import load_map
from map_data import MAP_DATA

pygame.init()

# Vytvoření okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyRPG")

clock = pygame.time.Clock()

# Načtení mapy
tiles = load_map(MAP_DATA)

# Vytvoření hráče
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(tiles, player)  # Přidáme hráče i dlaždice do skupiny

# Hlavní smyčka hry
running = True
while running:
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Aktualizace hráče
    player.update(keys)

    # Kreslení
    screen.fill((0, 0, 0))  # Vyčištění obrazovky
    tiles.draw(screen)  # Vykreslíme dlaždice
    all_sprites.draw(screen)  # Vykreslíme hráče
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()