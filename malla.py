import pygame
import pyautogui as pt
import time

#robo 3t #para mongo sh#mac, linux, 

#dz31yRaYStnDqNN1

#COLORES
CIRCLE_SIZE = 30,30
BLANCO = 255,255,255



def drawCircle (mouse_position):
    pygame.draw.circle(screen,BLANCO,mouse_position,10 )
    pass


pygame.init ()
width, height = 600, 600 #tama no de la ventana
screen = pygame.display.set_mode((height, width))
bg = 25,25,25 #rgb colors
screen.fill(bg)#llenamos o pintamos de ese color

#creando la malla
nxC, nyC = 10,10
dimxC= width/nxC
dimyC= height/nyC
#dimensiones
#colores rgb (255,255,255)

#puntos de poligono

#posicion del mouse


run=True#ejecutar//booleano

while run:#logica que se ejecutara durante todo el simulador
    mouse_position = pygame.mouse.get_pos()#no estoy tomando la posicion del mous

    for y in range (0,nxC):
        for x in range (0,nyC):
            poly =[
                ((x)*dimxC,y*dimyC),
                ((x+1)*dimxC, y*dimyC),
                ((x+1)*dimxC,(y+1)*dimyC),#multiplicamos por las dimensiones del cubo
                ((x)*dimxC, (y+1)*dimyC)

            ]
            pygame.draw.polygon(screen, (128,128,128), poly,1)#ultimo argumento es para el grosos sino se pinta todo
        #pygame.display.flip()
    pygame.draw.circle(screen,BLANCO,(200,200),10 )#pantalla, color,posicion, radio
    pygame.display.flip()
    #ya dibujamos
    for event in pygame.event.get():#obtenemos todos los eventos
        print (mouse_position)
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawCircle(mouse_position)
            pass
        #print(event)

        elif event.type == pygame.QUIT:
            run =False
            #si presiona cerrar se rompe el bucle y cierra el programa

    pygame.display.update()

pygame.quit()


#para dibujar es con fill
#actualizae.update
    