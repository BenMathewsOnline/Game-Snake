import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and food settings
SNAKE_SIZE = 20
SNAKE_SPEED = 20
FOOD_SIZE = 20

clock = pygame.time.Clock()

snake_pos = [[100, 100], [120, 100], [140, 100]]
snake_speed = [SNAKE_SPEED, 0]

food_pos = [random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE, random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE]
food_spawn = True

def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()

        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                snake_speed = [0, -SNAKE_SPEED]
            if keys[pygame.K_DOWN]:
                snake_speed = [0, SNAKE_SPEED]
            if keys[pygame.K_LEFT]:
                snake_speed = [-SNAKE_SPEED, 0]
            if keys[pygame.K_RIGHT]:
                snake_speed = [SNAKE_SPEED, 0]

    snake_pos.insert(0, list(snake_pos[0]))

    if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE, random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE]
    food_spawn = True

    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    # Game Over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT:
        game_over()

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    # Draw everything
    WIN.fill(WHITE)

    for pos in snake_pos:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))

    pygame.display.flip()

    clock.tick(15)
