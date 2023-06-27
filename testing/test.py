import pygame

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Dimensiones de la cuadrícula
GRID_SIZE = 300
CELL_SIZE = 60

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_grid():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cuadrícula")

    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]  # Matriz para almacenar el estado de la cuadrícula
    drawing = False  # Variable para indicar si se está dibujando una línea

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False

        screen.fill(BLACK)

        # Dibuja las líneas horizontales
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

        # Dibuja las líneas verticales
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))

        # Actualiza el estado de la cuadrícula según la posición del ratón
        if drawing:
            mouse_pos = pygame.mouse.get_pos()
            cell_x = mouse_pos[0] // CELL_SIZE
            cell_y = mouse_pos[1] // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                grid[cell_y][cell_x] = 1

        # Dibuja la línea en la cuadrícula
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if grid[y][x] == 1:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, (255,0,0), rect, 9)

        pygame.display.flip()

    pygame.quit()

draw_grid()
