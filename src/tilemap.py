# Základní dlaždice a načítání mapy

import pygame

from settings import TILE_SIZE

# Barvy dlaždic (dočasně, než budeme mít obrázky)
TILE_COLORS = {
    "G": (34, 177, 76),  # Grass - Zelená
    "P": (200, 200, 0),  # Path - Cesta
    "W": (0, 162, 232)   # Water - Voda (neprůchozí)
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(TILE_COLORS[tile_type]) # Vybarvíme dlaždici
        self.rect = self.image.get_rect(topleft=(x, y))
        self.tile_type = tile_type
        
        # Voda je neprůchozí
        self.walkable = tile_type != "W"
        
def load_map(map_data):
    """Načte mapu ze seznamu řetězců."""
    tiles = pygame.sprite.Group()
    for row_idx, row in enumerate(map_data):
        for col_idx, tile_type in enumerate(row):
            tile = Tile(col_idx * TILE_SIZE, row_idx * TILE_SIZE, tile_type)
            tiles.add(tile)
    return tiles