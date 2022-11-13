import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import pygame_widgets
from pygame_widgets.button import Button
# from main import view_size

VIEW_SIZE = (600, 700)
TEXT_FONT_COLOR = (0,125,200)
SUBMIT_BUTTON_COLOR = (3, 86, 252)

pygame.init()
win = pygame.display.set_mode(VIEW_SIZE)

font = pygame.font.Font('freesansbold.ttf', VIEW_SIZE[0]//15)
text = font.render('safety score', True, TEXT_FONT_COLOR)
 
textRect = text.get_rect()
textRect.center = (VIEW_SIZE[0]//2, VIEW_SIZE[1]*0.1)

slider = Slider(win, VIEW_SIZE[0]//6, VIEW_SIZE[1]//2, VIEW_SIZE[0]//1.5, VIEW_SIZE[1]//25, min=0, max=10, step=1)
output = TextBox(win, VIEW_SIZE[0]//2.5, VIEW_SIZE[1]//3, VIEW_SIZE[0]//6, VIEW_SIZE[1]//12, fontSize=VIEW_SIZE[0]//15)

def getValue():    
    print(slider.getValue())
    return slider.getValue()

button = Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    VIEW_SIZE[0]//2.5,  # X-coordinate of top left corner
    VIEW_SIZE[1]//1.3,  # Y-coordinate of top left corner
    VIEW_SIZE[0]//5,  # Width
    VIEW_SIZE[1]//15,  # Height

    # Optional Parameters
    text='submit',  # Text to display
    fontSize=VIEW_SIZE[0]//12,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=SUBMIT_BUTTON_COLOR,  # Colour of button when not being interacted with
    hoverColour=(144, 3, 252),  # Colour of button when being hovered over
    pressedColour=SUBMIT_BUTTON_COLOR,  # Colour of button when being clicked
    # radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: getValue()  # Function to call when clicked on
)


run  = True
while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        win.fill((255,255,255))
        win.blit(text,textRect)

        output.setText(slider.getValue())
        # print(slider.getValue())
        pygame_widgets.update(events)
        pygame.display.update()

def paint_feedback():
    font = pygame.font.Font('freesansbold.ttf', VIEW_SIZE[0]//15)
    text = font.render('safety score', True, TEXT_FONT_COLOR)
    
    textRect = text.get_rect()
    textRect.center = (VIEW_SIZE[0]//2, VIEW_SIZE[1]*0.1)

    slider = Slider(win, VIEW_SIZE[0]//6, VIEW_SIZE[1]//2, VIEW_SIZE[0]//1.5, VIEW_SIZE[1]//25, min=0, max=10, step=1)
    output = TextBox(win, VIEW_SIZE[0]//2.5, VIEW_SIZE[1]//3, VIEW_SIZE[0]//6, VIEW_SIZE[1]//12, fontSize=VIEW_SIZE[0]//15)

    button = Button(
    # Mandatory Parameters
    win,  # Surface to place button on
    VIEW_SIZE[0]//2.5,  # X-coordinate of top left corner
    VIEW_SIZE[1]//1.3,  # Y-coordinate of top left corner
    VIEW_SIZE[0]//5,  # Width
    VIEW_SIZE[1]//15,  # Height

    # Optional Parameters
    text='submit',  # Text to display
    fontSize=VIEW_SIZE[0]//12,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    inactiveColour=SUBMIT_BUTTON_COLOR,  # Colour of button when not being interacted with
    hoverColour=(144, 3, 252),  # Colour of button when being hovered over
    pressedColour=SUBMIT_BUTTON_COLOR,  # Colour of button when being clicked
    # radius=20,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: getValue()  # Function to call when clicked on
)