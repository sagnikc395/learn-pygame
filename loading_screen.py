import pygame 

from constants import * 

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Loading Screen Example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font("assets/Pixeltype.ttf",50)

def show_loading_screen():
    screen.fill(BLACK)
    loading_text = FONT.render("Loading...", True, WHITE)
    text_rect = loading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(loading_text, text_rect)
    pygame.display.flip()

def load_game_assets():
    # Simulate a long loading process
    import time
    time.sleep(3) 
    # In a real game, this is where you would load images, sounds, etc.
    print("Assets loaded!")
