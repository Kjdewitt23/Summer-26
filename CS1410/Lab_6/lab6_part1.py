import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

monkeyImg = pygame.image.load('monkey.png')
monkX = 20.0 # This is a float to make MyPy not throw an error of 'incompatible types on line 23'
monkY = 480.0
monkX_change = 0.15

def monkey(x, y):
    screen.blit(monkeyImg, (x, y))

running = True
while running:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    monkX += monkX_change
    
    if monkX <= 0 or monkX >= 736:
        monkX_change = -monkX_change

    monkey(monkX, monkY)
    pygame.display.update()