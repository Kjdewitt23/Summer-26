import pygame
from pygame import mixer
import random
from shapes import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#.....Enemies..........
enemies = []

#.....Functions..........
def spawn_square():
    length = random.randint(20, 125)
    side = random.randint(0,3)

    if side == 0:
        x = random.randint(0, SCREEN_WIDTH)
        y = -length
    elif side == 1:
        x = random.randint(0, SCREEN_WIDTH)
        y = SCREEN_HEIGHT + length
    elif side == 2:
        x = -length
        y = random.randint(0, SCREEN_HEIGHT)
    else:
        x = SCREEN_WIDTH + length
        y = random.randint(0, SCREEN_HEIGHT)

    enemies.append(Square(x, y, length))

def spawn_circle():
    radius = random.randint(20, 120)
    side = random.randint(0,3)

    if side == 0:
        x = random.randint(0, SCREEN_WIDTH)
        y = -radius
    elif side == 1:
        x = random.randint(0, SCREEN_WIDTH)
        y = SCREEN_HEIGHT + radius
    elif side == 2:
        x = -radius
        y = random.randint(0, SCREEN_HEIGHT)
    else:
        x = SCREEN_WIDTH + radius
        y = random.randint(0, SCREEN_HEIGHT)

    enemies.append(Circle(x, y, radius))

def spawn_triangle():
    length = random.randint(20, 120)
    side = random.randint(0,3)

    if side == 0:
        x = random.randint(0, SCREEN_WIDTH)
        y = -length
    elif side == 1:
        x = random.randint(0, SCREEN_WIDTH)
        y = SCREEN_HEIGHT + length
    elif side == 2:
        x = -length
        y = random.randint(0, SCREEN_HEIGHT)
    else:
        x = SCREEN_WIDTH + length
        y = random.randint(0, SCREEN_HEIGHT)

    enemies.append(Triangle(x, y, length))


#.....Game loop..........

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()
elapsed_time = (current_time - start_time) / 1000
font = pygame.font.Font(None, 18)

last_square_spawn = 0.0
last_circle_spawn = 0.0
last_triangle_spawn = 0.0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000

#.....Spawn Enemies..........
    if elapsed_time - last_square_spawn >= 2:
        last_square_spawn = elapsed_time
        for _ in range(5):
            spawn_square()

    if elapsed_time - last_circle_spawn >= 7:
        last_circle_spawn = elapsed_time
        for _ in range(5):
            spawn_circle()

    if elapsed_time - last_triangle_spawn >= 12:
        last_triangle_spawn = elapsed_time
        for _ in range(2):
            spawn_triangle()

    for enemy in enemies:
        enemy.update(elapsed_time)

#.....Update Enemies.........
    enemies = [
        enemy
        for enemy in enemies
        if not enemy.reached_center()
    ]

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for enemy in enemies:
        if enemy.hit_player(mouse_x, mouse_y):
            survival_time = elapsed_time
            running = False
            break

    screen.fill((0, 0, 0))
#.....Draw Enemies..........
    for enemy in enemies:
        enemy.draw(screen)

#.....Draw Mouse Circle..........
    pygame.draw.circle(
        screen,
        "white",
        (mouse_x, mouse_y),
        4
    )

#.....Draw Timer..........
    timer_text = font.render(
        f"Time: {elapsed_time:.1f}s",
        True,
        "white"
    )

    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

    survival_time = elapsed_time
    font = pygame.font.Font(None, 60)

    text = font.render(
        f"You survived {survival_time:.1f} seconds!",
        True,
        "white"
    )
#.....Game Over State to display time..........
game_over = True

while game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    screen.fill((0, 0, 0))

    screen.blit(text, (150, 250))

    pygame.display.flip()

pygame.quit()