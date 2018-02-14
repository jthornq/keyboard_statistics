
import pygame


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 25)
RED = (255, 0, 0)
CYAN = (65, 202, 217)
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Keylogger")


key_list = []
statistics = open("statistics.txt", "r+")

done = False
clock = pygame.time.Clock()

with open('statistics.txt,', 'r') as file:
    data = file.readlines()

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            letter = event.__dict__['unicode']

    data[ord(letter) - 64] += 1




    screen.fill(WHITE)
    pygame.draw.rect(screen, CYAN, [0, 0, 250, 1200])
    pygame.draw.rect(screen, BLACK, [250, 0, 5, 1200])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()