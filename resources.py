import pygame

tiles = {}

tiles['street'] = pygame.image.load('assets/white-tile.jpg')
tiles['start'] = pygame.image.load('assets/gray-tile.jpg')
tiles['end'] = pygame.image.load('assets/gray-tile.jpg')

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

def change_tile_size(new_tile_size):
  for key in tiles:
    tiles[key] = pygame.transform.scale(tiles[key], (new_tile_size, new_tile_size))

def get_road_img(city, j,i):

  if city[i-1][j]=='ROAD' and city[i][j-1]=='ROAD' and city[i+1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-LURB']
  if city[i][j-1]=='ROAD' and city[i+1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-URB']
  if city[i-1][j]=='ROAD' and city[i][j-1]=='ROAD' and city[i+1][j]=='ROAD':
    return tiles['road-LUR']
  if city[i-1][j]=='ROAD' and city[i][j-1]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-LUB']
  if city[i-1][j]=='ROAD' and city[i+1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-LRB']
  
  if city[i-1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-LB']
  if city[i-1][j]=="ROAD" and city[i+1][j]=='ROAD':
    return tiles['road-LR']
  if city[i-1][j]=='ROAD' and city[i][j-1]=='ROAD':
    return tiles['road-LU']
  if city[i+1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-RB']
  if city[i][j+1]=='ROAD' and city[i][j-1]=='ROAD':
    return tiles['road-UB']
  if city[i][j+1] =='ROAD' and city[i+1][j]=='ROAD':
    return tiles['road-UR']
  if city[i-1][j]=='ROAD' and city[i][j+1]=='ROAD':
    return tiles['road-LB']
  
  if city[i][j+1]=="ROAD":
    return tiles['road-B']
  if city[i][j-1]=="ROAD":
    return tiles['road-U']
  if city[i+1][j]=="ROAD":
    return tiles['road-R']
  if city[i-1][j]=="ROAD":
    return tiles['road-L']

