import pygame
WIDTH = 1280
HEIGHT = 720
PADDING = 10
GRID = [(0+PADDING, 0+PADDING), (WIDTH-PADDING, 0+PADDING), (WIDTH-PADDING,
                                                             HEIGHT-PADDING), (0+PADDING, HEIGHT-PADDING)]
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rect = pygame.Rect(player_pos.x, player_pos.y, 40, 40)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for i in range(len(GRID)):
        pygame.draw.aaline(
            screen, "blue", GRID[i], GRID[(i + 1) % len(GRID)], 10)
    pygame.draw.aalines(screen, "black", True, [
                        (0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)])

    pygame.draw.rect(screen, "red", rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        rect.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        rect.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        rect.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        rect.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
