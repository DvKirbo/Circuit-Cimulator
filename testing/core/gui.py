from tki import *
import pygame
from pygame.locals import *
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Simulador de Circuitos")
reloj = pygame.time.Clock()
COLOR_FONDO = (255, 255, 255)
COLOR_NODO = (0, 0, 0)
TAMANO_NODO = 20
GROSOR_LINEA = 2
simulador = SimuladorCircuitos()
fuente_voltaje = None
def dibujar_nodos():
    for nodo in simulador.nodos.values():
        if isinstance(nodo, Resistencia):
            pygame.draw.circle(pantalla, COLOR_NODO, nodo.posicion, TAMANO_NODO)
        elif isinstance(nodo, Capacitor):
            pygame.draw.polygon(pantalla, COLOR_NODO, [nodo.posicion, (nodo.posicion[0] - TAMANO_NODO, nodo.posicion[1] + TAMANO_NODO), (nodo.posicion[0] + TAMANO_NODO, nodo.posicion[1] + TAMANO_NODO)])
        elif isinstance(nodo, FuenteVoltaje):
            pygame.draw.rect(pantalla, COLOR_NODO, (nodo.posicion[0] - TAMANO_NODO, nodo.posicion[1] - TAMANO_NODO, TAMANO_NODO * 2, TAMANO_NODO * 2))

def dibujar_conexiones():
    for nodo in simulador.nodos.values():
        for conexion in nodo.conexiones:
            pygame.draw.line(pantalla, COLOR_NODO, nodo.posicion, conexion.posicion, GROSOR_LINEA)

def actualizar_pantalla():
    pantalla.fill(COLOR_FONDO)
    dibujar_nodos()
    dibujar_conexiones()
    pygame.display.flip()
def main():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                return

            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botón izquierdo del mouse
                    x, y = evento.pos
                    nombre = f"Nodo_{len(simulador.nodos)}"
                    nodo = simulador.crear_nodo(nombre, voltaje=5.0)  # Crea un nodo de voltaje
                    nodo.posicion = (x, y)
                    
                    if len(simulador.nodos) == 1:
                        global fuente_voltaje
                        fuente_voltaje = nodo

            if evento.type == KEYDOWN:
                if evento.key == K_RETURN:  # Presiona la tecla Enter para cerrar el circuito
                    if fuente_voltaje:
                        fuente_voltaje.conectar(fuente_voltaje)  # Conecta el nodo de la fuente de voltaje consigo mismo
                        actualizar_pantalla()
                        return

        actualizar_pantalla()
        reloj.tick(60)

if __name__ == "__main__":
    main()
