import pygame

pygame.init()
screen = pygame.display.set_mode((1290, 720))
clock = pygame.time.Clock()
running = True
dt = 0
x_midline_start = 600
x_midline_end = 600
y_midline_start = 100
y_midline_end = 150
gap = 40

player1_posy = 100
player2_posy = 100

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")

    pygame.draw.rect(screen, "blue", pygame.Rect(30, 30, 1240, 650), 2)

    x_midline_start = 600
    x_midline_end = 600
    y_midline_start = 80
    y_midline_end = 160

    for i in range(5):
        pygame.draw.line(screen, "blue", (x_midline_start, y_midline_start), (x_midline_end, y_midline_end))
        y_midline_start = y_midline_end + gap
        y_midline_end = y_midline_start + gap * 2

    pygame.draw.line(screen, "blue", (215, player1_posy), (215, player1_posy + 100))
    pygame.draw.line(screen, "red", (1075, player2_posy), (1075, player2_posy +100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player1_posy -= 300 * dt
    if keys[pygame.K_s]:
        player1_posy += 300 * dt

    if keys[pygame.K_UP]:
        player2_posy -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_posy += 300 * dt

    pygame.display.flip()

    clock.tick(60)

    dt = clock.tick(60) / 1000

pygame.quit()
