import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Game")

run = True
mouse = {
    "down": False,
    "pressed": False,
    "released": False,
    "x": 0,
    "y": 0
}
key = {
    "down": [],
    "pressed": [],
    "released": []
}
clk = pygame.time.Clock()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            key.pressed.append(e.key)
            key.down.append(e.key)
        if e.type == pygame.KEYUP:
            key.released.append(e.key)
            key.down.remove(e.key)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
