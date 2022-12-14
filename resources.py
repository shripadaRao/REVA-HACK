import pygame

tiles = {}

def load_assets(tile_size):
  global tiles

  # road images
  tiles['road-B'] = pygame.image.load('assets/roads/B.png')
  tiles['road-L'] = pygame.image.load('assets/roads/L.png')
  tiles['road-R'] = pygame.image.load('assets/roads/R.png')
  tiles['road-U'] = pygame.image.load('assets/roads/U.png')
  tiles['road-LB'] = pygame.image.load('assets/roads/LB.png')
  tiles['road-LR'] = pygame.image.load('assets/roads/LR.png')
  tiles['road-LRB'] = pygame.image.load('assets/roads/LRB.png')
  tiles['road-LU'] = pygame.image.load('assets/roads/LU.png')
  tiles['road-LUB'] = pygame.image.load('assets/roads/LUB.png')
  tiles['road-LUR'] = pygame.image.load('assets/roads/LUR.png')
  tiles['road-LURB'] = pygame.image.load('assets/roads/LURB.png')
  tiles['road-RB'] = pygame.image.load('assets/roads/RB.png')
  tiles['road-UB'] = pygame.image.load('assets/roads/UB.png')
  tiles['road-UR'] = pygame.image.load('assets/roads/UR.png')
  tiles['road-URB'] = pygame.image.load('assets/roads/URB.png')

  tiles['pin'] = pygame.image.load("assets/pin.png").convert_alpha()

  tiles['street'] = pygame.image.load('assets/green-tile.jpg')

  tiles['highlight'] = pygame.Surface((100, 100))
  tiles['highlight'].set_alpha(128)
  tiles['highlight'].fill((255, 234, 0))

  change_tile_size(tile_size)

def change_tile_size(new_tile_size):
  for key in tiles:
    tiles[key] = pygame.transform.scale(tiles[key], (new_tile_size, new_tile_size))

def get_road_img(city, j, i):
  city_height = len(city)
  city_width = 0 if not city else len(city[0])

  road = ['ROAD', 'START', 'END']

  if city[j][i-1] in road and city[j-1][i] in road and city[j][i+1] in road and city[j+1][i] in road:
    return tiles['road-LURB']
  if city[j-1][i] in road and city[j][i+1] in road and city[j+1][i] in road:
    return tiles['road-URB']
  if city[j][i-1] in road and city[j-1][i] in road and city[j][i+1] in road:
    return tiles['road-LUR']
  if city[j][i-1] in road and city[j-1][i] in road and city[j+1][i] in road:
    return tiles['road-LUB']
  if city[j][i-1] in road and city[j][i+1] in road and city[j+1][i] in road:
    return tiles['road-LRB']
  
  if city[j][i-1] in road and city[j+1][i] in road:
    return tiles['road-LB']
  if city[j][i-1] in road and city[j][i+1] in road:
    return tiles['road-LR']
  if city[j][i-1] in road and city[j-1][i] in road:
    return tiles['road-LU']
  if city[j][i+1] in road and city[j+1][i] in road:
    return tiles['road-RB']
  if city[j-1][i] in road and city[j+1][i] in road:
    return tiles['road-UB']
  if city[j-1][i] in road and city[j][i+1] in road:
    return tiles['road-UR']
  if city[j][i-1] in road and city[j+1][i] in road:
    return tiles['road-LB']
  
  if city[j+1][i] in road:
    return tiles['road-B']
  if city[j-1][i] in road:
    return tiles['road-U']
  if city[j][i+1] in road:
    return tiles['road-R']
  if city[j][i-1] in road:
    return tiles['road-L']