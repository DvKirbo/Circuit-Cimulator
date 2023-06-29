import core2 as core
import pygame
import math
import time


nodos = []#arrays de los nodos creados
Nombre_nodos= []#array de los nombres de los nodos q vamos a utilizar
array_coliders = []#array de los coliders asociados al circulo
posiciones = []

LETRAS = 65 #letras desde la A hasta la Z #65 // 91
CIRCLE_SIZE = 15,15
RADIO = 5
cont = 0

#COLORES
BLANCO = 255,255,255
ROJO=255,0,0

def drawNodo (mouse_position):
    #Crear un rectángulo que envuelve al círculo
    a,b=mouse_position
    #procedemos a guardar todo
    if len(posiciones)>=1:
        x1, y1 = posiciones[cont-1]
        if(abs(x1 - a) > abs(y1 - b)):
            if(x1 > a):
                posiciones.append([x1-100,y1])
            else:
                posiciones.append([x1+100,y1])
        elif(abs(x1 - a) < abs(y1 - b)):
            if(y1 > a):
                posiciones.append([x1,y1-100])
            else:
                posiciones.append([x1,y1+100])
    else:
        posiciones.append([a,b])
    pygame.draw.circle(screen,BLANCO,posiciones[cont],5)
    #esta linea es la q jode todo mrd                   
    
def drawlines ():
    for i in range (len(nodos)-1):
        pygame.draw.line(screen,BLANCO,start_pos=(posiciones[i]),end_pos=(posiciones[i+1]),width=5)

def drawresistanceright ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    
    
    # Draw the resistor
    pygame.draw.line(screen, BLANCO, posiciones[cont-1], (x1+30, y1), 5)  # Node 1 connection
    #pygame.draw.line(screen, BLANCO, (x1+30, y1), (x2-30, y2), 5)  # Body of the resistor
    pygame.draw.line(screen, BLANCO, (x2-30, y2), posiciones[cont], 5)  # Node 2 connection

    # Draw the wavy lines
    pygame.draw.line(screen, BLANCO, (x1+30, y1), (x1 + 40, y1+20), 5)
    for x in range(x1 + 40, x2-50,20):
        pygame.draw.line(screen, BLANCO, (x, y1+20), (x+10, y1-20), 5)
        pygame.draw.line(screen, BLANCO, (x+10, y1 - 20), (x+20, y1 + 20), 5)
    pygame.draw.line(screen, BLANCO, (x2-37, y1+20), (x2-30, y1), 5)


def reactCircle (mouse_position , i):
    #calculando la distancia entre el mouse y el nodo
    # Calcular la distancia entre el centro del círculo y el mouse
    a, b=mouse_position
    distance = math.sqrt((a - posiciones[i][0]) ** 2 + (b-posiciones[i][1]) ** 2)
    if distance <= RADIO:
        pygame.draw.circle(screen, ROJO,posiciones[i],RADIO)
        time.sleep(0.2)
    else:    
        pygame.draw.circle(screen,BLANCO,posiciones[i], RADIO)
    

def estado_normal(i):    
    pygame.draw.circle(screen,BLANCO,posiciones[i][0], posiciones[i][1], RADIO)


pygame.init ()
width, height = 650, 1000 #tama no de la ventana
screen = pygame.display.set_mode((height, width))
bg = 25,25,25 #rgb colors
screen.fill(bg)#llenamos o pintamos de ese color

#creando la malla
nxC, nyC = 20,20
dimxC= width/nxC
dimyC= height/nyC
#dimensiones
#colores rgb (255,255,255)

#puntos de poligono

#posicion del mouse


run=True#ejecutar//booleano

while run:#logica que se ejecutara durante todo el simulador
    mouse_position = pygame.mouse.get_pos()#no estoy tomando la posicion del mous
    #creamos colider para el puntero
    
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
    #pygame.draw.circle(screen,BLANCO,(200,200),10 )#pantalla, color,posicion, radio
    #pygame.draw.line(screen,BLANCO,start_pos=(200,200),end_pos=(100,100),width=1)
    pygame.display.flip()
    #ya dibujamos
    for event in pygame.event.get():#obtenemos todos los eventos
      
        if event.type == pygame.QUIT:
            run =False
            #si presiona cerrar se rompe el bucle y cierra el programa
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
                #usar array de nodo para guardar las variables
                nodos.append(core.Nodo(LETRAS))#añadimos a la lista el objeto nodo
                Nombre_nodos.append(chr(LETRAS))#guardamos tmbn su nombre la ptmre
                print(f"Nodo: {chr(LETRAS)} creado")

                drawNodo(mouse_position)
                if pygame.mouse.get_pressed()[0]:
                    if len(nodos)>1:
                        drawlines()
                elif pygame.mouse.get_pressed()[2]:
                    if len(nodos)>1:
                        drawresistanceright()
                a,b=mouse_position
                colider = pygame.Rect(a -RADIO, b -RADIO, RADIO * 2, RADIO * 2)
                array_coliders.append(colider)
    
                LETRAS=LETRAS+1
                cont=cont+1
                pass
            #print(event)
        
        elif len(nodos)>0:
            i=0
            for nodo in nodos:
                reactCircle(mouse_position, i)
                i+=1 
        

    pygame.display.update()

pygame.quit()
