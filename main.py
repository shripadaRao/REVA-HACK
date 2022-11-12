### imports
import pygame
import resources
from city_generation import generate_city


# tile info
tile_size = 50
resources.change_tile_size(tile_size)
TILE_STREET = 'STREET'
TILE_ROAD = 'ROAD'
TILE_START = 'START'
TILE_END = 'END'

# view related info
view_topleft = [0, 0]
view_size = [10 * tile_size, 10 * tile_size]
movement_distance = 1 * tile_size

# screen dimensions
screen_width = view_size[0]
screen_height = view_size[1]

# states info
states = ['SELECTING START', 'SELECTING END', 'SELECTED']
current_state = 0


city_height = int(input('City Height: '))
city_width = int(input('City Width: '))
city = generate_city(city_height, city_width)


### functions

def paint_view(screen):

  for j in range(view_topleft[1]//tile_size, (view_topleft[1]+view_size[1])//tile_size):
    for i in range(view_topleft[0]//tile_size, (view_topleft[0]+view_size[0])//tile_size):

      x = i * tile_size - view_topleft[0]
      y = j * tile_size - view_topleft[1]

      if (city[j][i] == TILE_ROAD):
        screen.blit(resources.get_road_img(city, j, i), (x, y))

      elif (city[j][i] == TILE_STREET):
        screen.blit(resources.tiles['street'], (x, y))
      elif (city[j][i] == TILE_START):
        screen.blit(resources.tiles['start'], (x, y))
      elif (city[j][i] == TILE_END):
        screen.blit(resources.tiles['end'], (x, y))
      
  pygame.display.flip()

def main():
  screen = pygame.display.set_mode((screen_width, screen_height))
  
  running = True
  while running:

    paint_view(screen)

    events = pygame.event.get()

    for event in events:
      
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          if not view_topleft[0] - movement_distance < 0:
            view_topleft[0] -= movement_distance
        elif event.key == pygame.K_UP:
          if not view_topleft[1] - movement_distance < 0:
            view_topleft[1] -= movement_distance
        elif event.key == pygame.K_RIGHT:
          if not view_topleft[0] + view_size[0] - 1 + movement_distance >= city_width * tile_size:
            view_topleft[0] += movement_distance
        elif event.key == pygame.K_DOWN:
          if not view_topleft[1] + view_size[1] - 1 + movement_distance >= city_width * tile_size:
            view_topleft[1] += movement_distance
      
      if event.type == pygame.MOUSEBUTTONUP:
        x, y = pygame.mouse.get_pos()
        city_x, city_y = x + view_topleft[0], y + view_topleft[1]
        i, j = city_x//tile_size, city_y//tile_size

        global current_state
        if city[j][i] == TILE_ROAD:
          if states[current_state] == 'SELECTING START':
            city[j][i] = TILE_START
            current_state += 1
            print('start selected')
          elif states[current_state] == 'SELECTING END':
            city[j][i] = TILE_END
            current_state += 1
            print('end selected')

if __name__ == '__main__':
  main()