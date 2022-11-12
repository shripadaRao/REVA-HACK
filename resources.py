import pygame

tiles = {}

tiles['road'] = pygame.image.load('assets/black-tile.jpg')
tiles['street'] = pygame.image.load('assets/white-tile.jpg')
tiles['start'] = pygame.image.load('assets/gray-tile.jpg')
tiles['end'] = pygame.image.load('assets/gray-tile.jpg')

def change_tile_size(new_tile_size):
  for key in tiles:
    tiles[key] = pygame.transform.scale(tiles[key], (new_tile_size, new_tile_size))