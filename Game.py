import pygame
from Player import Player

pygame.init()
pygame.font.init()

pygame.display.set_caption('Rainfun Platformer')
#pygame.display.set_icon(pygame.image.load(r'Resources\Enemies\ship\idle.png'))

clock = pygame.time.Clock()
myfont = pygame.font.SysFont('freesans', 30)
running = True
sW = 1024
sH = 768
screen = pygame.display.set_mode((sW, sH))

BLACK = (0, 0, 0)
background = pygame.Surface(screen.get_size())
player = Player(50, 50, 'Resources/Player.png', sW, sH)



def start():
    loop()
    cleanUp()

def loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update()
        render()
        clock.tick(30)

def render():
    screen.fill(BLACK)
    player.render(screen)
    pygame.display.flip()



def cleanUp():
    pygame.quit()


start()
