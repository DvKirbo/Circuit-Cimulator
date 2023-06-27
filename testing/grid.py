import pygame

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Dimensiones de la cuadrícula
GRID_SIZE = 50
CELL_SIZE = 60

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_grid():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cuadrícula")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Dibuja las líneas horizontales
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

        # Dibuja las líneas verticales
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))

        pygame.display.flip()

    pygame.quit()

draw_grid()
