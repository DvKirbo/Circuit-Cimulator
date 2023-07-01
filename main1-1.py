import core2 as core
import pygame
import keyboard
import heapq
import sys
import math
import time


nodos = []#arrays de los nodos creados
Nombre_nodos= []#array de los nombres de los nodos q vamos a utilizar
posiciones = []

LETRAS = 65 #letras desde la A hasta la Z #65 // 91
CIRCLE_SIZE = 15,15
RADIO = 5
cont = 0

##componentes
tipocomponente = "cable"

#COLORES
BLANCO = 255,255,255
ROJO=255,0,0

def nodo_existente(posicion):
    for node in posiciones:
        if node == posicion:
            return True
    return False

def drawNodo (mouse_position):
    a,b=mouse_position
    #procedemos a cambiar la posición
    if len(posiciones)>=1:
        # Encuentra el nodo más cercano a la posición del mouse
        closest_node = min(posiciones, key=lambda node: abs(mouse_position[0] - node[0]) + abs(mouse_position[1] - node[1]))

        #Redirecciona la posición del mouse en una escala de 100 pixeles
        x1, y1 = posiciones[cont-1]
        if(round((a-x1)/100) != 0):
            a = round((a-x1)/100)*100+x1
        elif round((a-x1)/100) == 0:
            a = x1

        if(round((b-y1)/100) != 0):
            b = round((b-y1)/100)*100+y1
        elif round((b-y1)/100) == 0:
            b = y1
        posiciones.append([a,b])

        if(tipocomponente != "RESISTENCIA" or tipocomponente != "VOLTAJE"):
            # Dibuja una línea horizontal o vertical desde el nodo seleccionado
            if abs(mouse_position[0] - closest_node[0]) < abs(mouse_position[1] - closest_node[1]):
                draw_line(closest_node)
            else:
                draw_line(closest_node)
    else:
        posiciones.append([a,b])
    pygame.draw.circle(screen,BLANCO,posiciones[cont],5)                       
                    

#Resistores, tanto en horizontal como en vertical
def drawresistanceright ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(x1 > x2):
        c = x1
        x1 = x2
        x2 = c
        
    # Lineas que conectan con el circuito
    pygame.draw.line(screen, BLANCO, (x1,y1), (x1+30, y1), 5)  # Node 1 connection
    pygame.draw.line(screen, BLANCO, (x2-30, y2), (x2,y2), 5)  # Node 2 connection

    # Dibuja los picos de la resistencia
    pygame.draw.line(screen, BLANCO, (x1+30, y1), (x1 + 40, y1+20), 5)
    for x in range(x1 + 40, x2-50,20):
        pygame.draw.line(screen, BLANCO, (x, y1+20), (x+10, y1-20), 5)
        pygame.draw.line(screen, BLANCO, (x+10, y1 - 20), (x+20, y1 + 20), 5)
    pygame.draw.line(screen, BLANCO, (x2-37, y1+20), (x2-30, y1), 5)

def drawresistancedown ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(y1 > y2):
        c = y1
        y1 = y2
        y2 = c
        
    pygame.draw.line(screen, BLANCO, (x1,y1), (x1, y1+30), 5)  # Node 1 connection
    pygame.draw.line(screen, BLANCO, (x2, y2-30), (x2,y2), 5)  # Node 2 connection

    pygame.draw.line(screen, BLANCO, (x1, y1+30), (x1+20, y1+40), 5)
    for y in range(y1 + 40, y2-50,20):
        pygame.draw.line(screen, BLANCO, (x1+20, y), (x1-20, y+10), 5)
        pygame.draw.line(screen, BLANCO, (x1- 20, y+10), (x1+ 20, y+20), 5)
    pygame.draw.line(screen, BLANCO, (x2+20, y2-37), (x2, y2-30), 5)

#Voltaje
def drawvoltageY ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(y1 > y2):
        c = y1
        y1 = y2
        y2 = c
    
    pygame.draw.line(screen, BLANCO, (x1,y1), (x1, ((y1+y2)/2)-5), 5)  # Node 1 connection
    pygame.draw.line(screen, BLANCO, (x2, ((y1+y2)/2)+5), (x2,y2), 5)  # Node 2 connection
    pygame.draw.line(screen, BLANCO, (x1-20,((y1+y2)/2)-5), (x1+20, ((y1+y2)/2)-5), 5)  
    pygame.draw.line(screen, BLANCO, (x2-10, ((y1+y2)/2)+5), (x2+10,((y1+y2)/2)+5), 5)

def drawvoltageX ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(x1 > x2):
        c = x1
        x1 = x2
        x2 = c
    
    pygame.draw.line(screen, BLANCO, (x1,y1), (((x1+x2)/2)-5, y1), 5)  # Node 1 connection
    pygame.draw.line(screen, BLANCO, (((x1+x2)/2)+5, y2), (x2,y2), 5)  # Node 2 connection
    pygame.draw.line(screen, BLANCO, (((x1+x2)/2)-5,y1+20), (((x1+x2)/2)-5, y1-20), 5)  
    pygame.draw.line(screen, BLANCO, (((x1+x2)/2)+5, y2+10), (((x1+x2)/2)+5,y2-10), 5)    

#################PRUEBA#################
def draw_line(start_pos):
    pygame.draw.line(screen, (255, 255, 255), start_pos, posiciones[cont], 5)

pygame.init ()
width, height = 1200, 600 #tama no de la ventana
screen = pygame.display.set_mode((width, height))
bg = 25,25,25 #rgb colors
screen.fill(bg)#llenamos o pintamos de ese color

imagen1 = pygame.image.load("daimakura gawr gura.jpg")
screen.blit(imagen1,(900,00))

#creando la malla
nxC, nyC = 30,20
dimxC= (width-300)/nxC
dimyC= height/nyC

run=True#ejecutar//booleano

while run:#logica que se ejecutara durante todo el simulador
    mouse_position = pygame.mouse.get_pos()
    
    for y in range (0,nyC):
        for x in range (0,nxC):
            poly =[
                ((x)*dimxC,y*dimyC),
                ((x+1)*dimxC, y*dimyC),
                ((x+1)*dimxC,(y+1)*dimyC),#multiplicamos por las dimensiones del cubo
                ((x)*dimxC, (y+1)*dimyC)

            ]
            pygame.draw.polygon(screen, (128,128,128), poly,1)#ultimo argumento es para el grosos sino se pinta todo
    pygame.display.flip()
    #ya dibujamos
    for event in pygame.event.get():#obtenemos todos los eventos
      
        if event.type == pygame.QUIT:
            run =False
            #si presiona cerrar se rompe el bucle y cierra el programa
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
                #usar array de nodo para guardar las variables
                nodos.append(core.Nodo(LETRAS))#añadimos a la lista el objeto nodo
                Nombre_nodos.append(chr(LETRAS))#guardamos tmbn su nombre
                print(f"Nodo: {chr(LETRAS)} creado")
                
                drawNodo(mouse_position)
                
                if keyboard.is_pressed("a"):
                    tipocomponente = "RESISTENCIA"
                elif keyboard.is_pressed("b"):
                    tipocomponente = "VOLTAJE"
                
                if(len(posiciones) > 1):
                    if pygame.mouse.get_pressed()[0]:
                        pass
                        #if len(nodos)>1:
                            #drawlines()

                if pygame.mouse.get_pressed()[2]:
                    if(tipocomponente == "RESISTENCIA"):
                        if len(nodos)>1:
                            x,y = mouse_position
                            x1, y1 = posiciones[cont-1]
                            if(abs(x1 - x) > abs(y1 - y)):
                                drawresistanceright()
                            else:
                                drawresistancedown()
                    elif(tipocomponente == "VOLTAJE"):
                        if len(nodos)>1:
                            x,y = mouse_position
                            x1, y1 = posiciones[cont-1]
                            if(abs(x1 - x) > abs(y1 - y)):
                                drawvoltageX()
                            else:
                                drawvoltageY()
    
                LETRAS=LETRAS+1
                cont = cont + 1
                pass
            #print(event) 
        
    pygame.display.update()

pygame.quit()
