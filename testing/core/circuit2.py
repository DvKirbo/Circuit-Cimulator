import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Circuitos")

# Lista para almacenar los componentes del circuito
components = []

# Clase Componente
class Component:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected = False

    def draw(self):
        pass

    def is_clicked(self, mouse_pos):
        pass

# Clase Resistencia
class Resistor(Component):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.value = 100  # Valor en ohmios

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 50, 20))

    def is_clicked(self, mouse_pos):
        return self.x < mouse_pos[0] < self.x + 50 and self.y < mouse_pos[1] < self.y + 20

# Clase Fuente de Alimentación
class PowerSupply(Component):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.voltage = 5  # Voltaje en voltios
        self.connected_resistor = None

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 20, 50))

    def is_clicked(self, mouse_pos):
        return self.x < mouse_pos[0] < self.x + 20 and self.y < mouse_pos[1] < self.y + 50

# Clase Bombilla
class Bulb(Component):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.on = False

    def draw(self):
        color = RED if self.on else BLACK
        pygame.draw.circle(screen, color, (self.x, self.y), 10)

    def is_clicked(self, mouse_pos):
        return self.x - 10 < mouse_pos[0] < self.x + 10 and self.y - 10 < mouse_pos[1] < self.y + 10

# Función para dibujar los componentes en pantalla
def draw_components():
    for component in components:
        component.draw()

# Función principal del simulador
def run_simulator():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for component in components:
                        if component.is_clicked(mouse_pos):
                            if isinstance(component, PowerSupply):
                                if not component.connected_resistor:
                                    component.connected_resistor = Resistor(mouse_pos[0], mouse_pos[1])
                                    components.append(component.connected_resistor)
                                    component.connected = True
                            elif isinstance(component, Bulb):
                                if component.connected:
                                    component.on = not component.on

        screen.fill(WHITE)
        draw_components()
        pygame.display.update()

run_simulator()
