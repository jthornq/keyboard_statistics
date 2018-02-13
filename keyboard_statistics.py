
import pygame

import settings


pygame.init()
ai_settings = settings.Settings()
stats = settings.Stats()

BLACK = (0, 0, 0)
WHITE = (255, 255, 25)
RED = (255, 0, 0)
CYAN = (65, 202, 217)
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Keylogger")




done = False
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key_list.append(event.__dict__['unicode'])
            
            if event.key == pygame.K_BACKSPACE:
                del key_list[-1]
                # to avoid prog crash, second key removal from list happens only if list has 1 or more characters in it.
                if len(key_list) > 0:
                    del key_list[-1]
            if event.key == pygame.K_SPACE:
                if refined_word == word_list['word']:
                    del word_list['word']
                    del key_list[:]
                    stats.score += 1
                # else != word_list  point deduction?
                del key_list[:]
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, CYAN, [0, 0, 250, 1200])
    pygame.draw.rect(screen, BLACK, [250, 0, 5, 1200])

    # If the dictionary holding the word is empty, create a new word.
    if len(word_list) < 3:
        append_word()

    # Blit the word to screen.
    draw_word()
    sb.show_score()
    # Move the word upwards on screen.
    word_list['y'] = word_list['y'] - ai_settings.word_speed

    # Converting key_list into a string(refined_word).
    refined_word = ''.join(map(str, key_list))

    # delete blitted word if it reaches the top of the screen.
    new_word()
    print(refined_word)
    print(key_list)
    typed_word()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()