
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

with open('statistics.txt', 'r') as file:
    data = file.readlines()
print(data)
while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:  # to find which key is being presse
            letter = event.__dict__['unicode'] # save pressed key to variable
            line_in_file = ord(letter) - 97  # letter into number, a = 1, b = 2 etc
            line_before_added = data[int(line_in_file)]  # grab information in corresponding line.
            line_before_added += 1  # somehow increment number in line
            # save line to variable with list of key presses (letter)
            print(line_before_added)


    screen.fill(WHITE)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()