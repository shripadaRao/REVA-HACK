### imports
import pygame
import resources

### global variables

city = [['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['0','0','0','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0','0','0','0','0'],
      ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1','0'],
      ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','0','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
      ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

city_height = len(city)
city_width = len(city[0]) if city else 0

# screen dimensions
screen_width = 1000
screen_height = 1000

# tile info
tile_size = 100
TILE_STREET = '1'
TILE_ROAD = '0'

# view related info
view_topleft = [0, 0]
view_size = [10 * tile_size, 10 * tile_size]
movement_distance = 1 * tile_size

### functions

def paint_view(screen):

  for j in range(view_topleft[1]//tile_size, (view_topleft[1]+view_size[1])//tile_size):
    for i in range(view_topleft[0]//tile_size, (view_topleft[0]+view_size[0])//tile_size):

      x = i * tile_size - view_topleft[0]
      y = j * tile_size - view_topleft[1]

      if (city[j][i] == TILE_STREET):
        screen.blit(resources.street_img, (x, y))
      elif (city[j][i] == TILE_ROAD):
        screen.blit(resources.road_img, (x, y))
      
  pygame.display.flip()

def get_keyboard_interactions():
  return pygame.key.get_pressed()

def keyboard_interaction_legal(keys):
  if not pygame.KEYDOWN:
    return False
  if keys[pygame.K_LEFT]:
    if view_topleft[0] - movement_distance < 0:
      return False
    else: 
      return True
  elif keys[pygame.K_RIGHT]:
    if view_topleft[0] + view_size[0] + movement_distance >= city_width * tile_size:
      return False
    else:
      return True
  elif keys[pygame.K_UP]:
    if view_topleft[1] - movement_distance < 0:
      return False
    else:
      return True
  elif keys[pygame.K_DOWN]:
    if view_topleft[1] + view_size[1] + movement_distance >= city_height * tile_size:
      return False
    else:
      return True
  return False

def apply_keyboard_interactions(keys):

  if not keyboard_interaction_legal(keys):
    return view_topleft
  
  new_view_topleft = view_topleft
  
  if keys[pygame.K_LEFT]:
    new_view_topleft[0] -= movement_distance
  elif keys[pygame.K_RIGHT]:
    new_view_topleft[0] += movement_distance
  elif keys[pygame.K_UP]:
    new_view_topleft[1] -= movement_distance
  elif keys[pygame.K_DOWN]:
    new_view_topleft[1] += movement_distance
  
  return new_view_topleft

def main():
  screen = pygame.display.set_mode((screen_width, screen_height))
  
  running = True
  while running:

    paint_view(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      keyboard_interactions = get_keyboard_interactions()
      global view_topleft
      view_topleft = apply_keyboard_interactions(keyboard_interactions)

if __name__ == '__main__':
  main()