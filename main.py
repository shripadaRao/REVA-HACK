### imports
import pygame
import resources
from city_generation import generate_city


pygame.font.init()

# tile info
tile_size = 60
TILE_STREET = 'STREET'
TILE_ROAD = 'ROAD'
TILE_START = 'START'
TILE_END = 'END'

# view related info
view_topleft = (0, 0)
view_size = (10 * tile_size, 10 * tile_size)
movement_distance = 1 * tile_size
view_rect = pygame.Rect(view_topleft[0], view_topleft[1], view_size[0], view_size[1])

# screen dimensions
menu_height = 100
menu_rect = pygame.Rect(0, view_size[1], view_size[0], menu_height)
screen_width = view_size[0]
screen_height = view_size[1] + menu_height

# review btn
review_btn_size = (150, 50)
review_btn_rect = pygame.Rect((view_size[0]-review_btn_size[0])//2, view_size[1]+(menu_height-review_btn_size[1])//2, review_btn_size[0], review_btn_size[1])
font = pygame.font.SysFont('Corbel',35)
review_btn_txt = font.render("Finish Trip", 1, (255, 255, 255))
text_size = font.size("Finish Trip")

# states info
states = ['SELECTING START', 'SELECTING END', 'SELECTED', 'REVIEWING']
current_state = 0

highlight_coords = [(2, 2), (2, 3), (2, 4)]


city_height = int(input('City Height: '))
city_width = int(input('City Width: '))
city = generate_city(city_height, city_width)


### functions

def paint_view(screen):

  for j in range(view_topleft[1]//tile_size, (view_topleft[1]+view_size[1])//tile_size):
    for i in range(view_topleft[0]//tile_size, (view_topleft[0]+view_size[0])//tile_size):

      x = i * tile_size - view_topleft[0]
      y = j * tile_size - view_topleft[1]

      if (city[j][i] in [TILE_ROAD, TILE_START, TILE_END]):
        screen.blit(resources.get_road_img(city, j, i), (x, y))
      
      elif (city[j][i] == TILE_STREET):
        screen.blit(resources.tiles['street'], (x, y))

      if (city[j][i] in [TILE_START, TILE_END]):
        screen.blit(resources.tiles['pin'], (x, y))

def paint_menu(screen):
  pygame.draw.rect(screen, [255, 255, 255], menu_rect)

def paint_highlights(screen):
  if not states[current_state] == 'SELECTED':
    return
  
  for i, j in highlight_coords:

    x = i * tile_size
    y = j * tile_size

    if (x + tile_size - 1 < view_topleft[0] or y + tile_size - 1 < view_topleft[1] or 
      x >= view_topleft[0] + view_size[0] or  y >= view_topleft[1] + view_size[1]):
      return

    screen.blit(resources.tiles['highlight'], (x, y))

def paint_review_btn(screen):
  pygame.draw.rect(screen, (0, 0, 0), review_btn_rect)
  txt_x = review_btn_rect.x + (review_btn_rect.w - text_size[0])//2
  txt_y = review_btn_rect.y + (review_btn_rect.h - text_size[1])//2
  screen.blit(review_btn_txt, (txt_x, txt_y))

def paint_review(screen):
  pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))

def in_rect(x, y, rect):
  return (x >= rect.x and y >= rect.y and 
          x < rect.x + rect.w and y < rect.y + rect.height)


def main():
  global current_state

  screen = pygame.display.set_mode((screen_width, screen_height))
  resources.load_assets(tile_size)
  
  running = True
  while running:

    if states[current_state] in ['SELECTING START', 'SELECTING END', 'SELECTED']:
      paint_view(screen)
      paint_menu(screen)
      paint_highlights(screen)
      if states[current_state] == 'SELECTED':
        paint_review_btn(screen)
    elif states[current_state] == 'REVIEWING':
      paint_review(screen)
    pygame.display.flip()

    events = pygame.event.get()

    for event in events:
      
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:

        if states[current_state] in ['SELECTING START', 'SELECTING END', 'SELECTED']:
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

        if states[current_state] in ['SELECTING START', 'SELECTING END', 'SELECTED']:
          x, y = pygame.mouse.get_pos()

          if in_rect(x, y, view_rect):
            city_x, city_y = x + view_topleft[0], y + view_topleft[1]
            i, j = city_x//tile_size, city_y//tile_size

            if city[j][i] == TILE_ROAD:
              if states[current_state] == 'SELECTING START':
                city[j][i] = TILE_START
                current_state += 1
              elif states[current_state] == 'SELECTING END':
                city[j][i] = TILE_END
                current_state += 1
          
          elif in_rect(x, y, menu_rect):

            if in_rect(x, y, review_btn_rect):
              if states[current_state] == 'SELECTED':
                current_state += 1

if __name__ == '__main__':
  main()