import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

monkeyImg = pygame.image.load("monkey.png")

monkeyRect = monkeyImg.get_rect()
monkeyRect.left = 20
monkeyRect.top = 480

monkeyX_pos = float(monkeyRect.x)
monkX_change = 0.15

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    monkeyX_pos += monkX_change
    monkeyRect.x = int(monkeyX_pos) # This took a little finagling to get to work without the monkey bouncing back and forth insanely fast

    if monkeyRect.left <= 0 or monkeyRect.right >= 800:
        monkX_change = -monkX_change

    screen.blit(monkeyImg, monkeyRect)

    pygame.display.update()