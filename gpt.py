import pygame 
import time 

import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Establecer el ancho y alto de la pantalla
ANCHO = 800
ALTO = 600

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dibujar una línea")

# Estado del dibujo
dibujando = False
posicion_anterior = None

# Bucle principal del programa
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
            #cerrar la ventana

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botón izquierdo del ratón
                dibujando = True
                posicion_anterior = pygame.mouse.get_pos()
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:  # Botón izquierdo del ratón
                dibujando = False
        elif evento.type == pygame.MOUSEMOTION:
            if dibujando:
                posicion_actual = pygame.mouse.get_pos()
                if posicion_anterior:
                    pygame.draw.line(pantalla, BLANCO, posicion_anterior, posicion_actual, 2)
                posicion_anterior = posicion_actual

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()


#pygame drawline(panta;;a, color, posicion inicial, poisicion final)