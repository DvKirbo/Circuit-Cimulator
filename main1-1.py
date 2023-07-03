import core2 as core
import pygame
import keyboard
import pygame_gui
import sys
import math
import time

posiciones = []
posicionesImportantes = []

resistencias = []
pos_resistencias_inicial = []
pos_resistencias_final = []
voltajes = []
pos_voltajes_inicial = []
pos_voltajes_final = []

cont = 0
cantImportante = 0

CIRCLE_SIZE = 15,15
RADIO = 3

##componentes
tipocomponente = "cable"

#NODOS
def drawNodo (mouse_position):
    a,b=mouse_position
    #procedemos a cambiar la posición
    if len(posiciones)%2 != 0 and len(posiciones)>=1:
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

        if(tipocomponente != "RESISTENCIA" and tipocomponente != "VOLTAJE"):
            # Dibuja una línea horizontal o vertical desde el nodo seleccionado
            draw_line(posiciones[cont-1])
        elif(tipocomponente == "RESISTENCIA"):
            x,y = mouse_position
            x1, y1 = posiciones[cont-1]
            if(abs(x1 - x) > abs(y1 - y)):
                drawresistanceright()
            else:
                drawresistancedown()
            resistencias.append(100)
            pos_resistencias_inicial.append((x1,y1))
            pos_resistencias_final.append((a,b))
        elif(tipocomponente == "VOLTAJE"):
            x,y = mouse_position
            x1, y1 = posiciones[cont-1]
            if(abs(x1 - x) > abs(y1 - y)):
                drawvoltageX()
            else:
                drawvoltageY()
            voltajes.append(10)
            pos_voltajes_inicial.append((x1,y1))
            pos_voltajes_final.append((a,b))
            
    else:
        if(len(posiciones)>=1):
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
        else:
            posiciones.append([a,b])
    #pygame.draw.circle(screen,BLANCO,posiciones[cont],5)                       
                    
def drawimportantnodo(mouse_position):
    a,b=mouse_position
    if(len(posiciones)>=1):
        x1, y1 = posiciones[cont-1]
        if(round((a-x1)/100) != 0):
            a = round((a-x1)/100)*100+x1
        elif round((a-x1)/100) == 0:
            a = x1

        if(round((b-y1)/100) != 0):
            b = round((b-y1)/100)*100+y1
        elif round((b-y1)/100) == 0:
            b = y1
        posicionesImportantes.append([a,b])
    else:
        posicionesImportantes.append([a,b])
    pygame.draw.circle(screen,(255,0,0),posicionesImportantes[cantImportante],3) 

#RESISTORES
def drawresistanceright ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(x1 > x2):
        c = x1
        x1 = x2
        x2 = c
        
    # Lineas que conectan con el circuito
    pygame.draw.line(screen, (255, 165, 0), (x1,y1), (x1+30, y1), 3)  # Node 1 connection
    pygame.draw.line(screen, (255, 165, 0), (x2-30, y2), (x2,y2),3)  # Node 2 connection

    # Dibuja los picos de la resistencia
    pygame.draw.line(screen, (255, 165, 0), (x1+30, y1), (x1 + 40, y1+10), 3)
    for x in range(x1 + 40, x2-50,20):
        pygame.draw.line(screen, (255, 165, 0), (x, y1+10), (x+10, y1-10), 3)
        pygame.draw.line(screen, (255, 165, 0), (x+10, y1 - 10), (x+20, y1 + 10), 3)
    pygame.draw.line(screen, (255, 165, 0), (x2-37, y1+10), (x2-30, y1), 3)

def drawresistancedown ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(y1 > y2):
        c = y1
        y1 = y2
        y2 = c
        
    pygame.draw.line(screen, (255, 165, 0), (x1,y1), (x1, y1+30), 3)  # Node 1 connection
    pygame.draw.line(screen, (255, 165, 0), (x2, y2-30), (x2,y2), 3)  # Node 2 connection

    pygame.draw.line(screen, (255, 165, 0), (x1, y1+30), (x1+10, y1+40), 3)
    for y in range(y1 + 40, y2-50,20):
        pygame.draw.line(screen, (255, 165, 0), (x1+10, y), (x1-10, y+10), 3)
        pygame.draw.line(screen, (255, 165, 0), (x1- 10, y+10), (x1+ 10, y+20), 3)
    pygame.draw.line(screen, (255, 165, 0), (x2+10, y2-37), (x2, y2-30), 3)

#FUENTES DE VOLTAJE
def drawvoltageY ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]

    if (y1 > y2):
        pygame.draw.line(screen, (0, 255, 0), (x1,y1), (x1, ((y1+y2)/2)+5), 3)  # Node 1 connection
        pygame.draw.line(screen, (0, 255, 0), (x2, ((y1+y2)/2)-5), (x2,y2), 3)  # Node 2 connection
        pygame.draw.line(screen, (0, 255, 0), (x1-20,((y1+y2)/2)-5), (x1+20, ((y1+y2)/2)-5), 3)  
        pygame.draw.line(screen, (0, 255, 0), (x2-10, ((y1+y2)/2)+5), (x2+10,((y1+y2)/2)+5), 3)
    elif (y2 > y1):
        pygame.draw.line(screen, (0, 255, 0), (x1,y1), (x1, ((y1+y2)/2)-5), 3)  # Node 1 connection
        pygame.draw.line(screen, (0, 255, 0), (x2, ((y1+y2)/2)+5), (x2,y2), 3)  # Node 2 connection
        pygame.draw.line(screen, (0, 255, 0), (x1-10,((y1+y2)/2)-5), (x1+10, ((y1+y2)/2)-5), 3)  
        pygame.draw.line(screen, (0, 255, 0), (x2-20, ((y1+y2)/2)+5), (x2+20,((y1+y2)/2)+5), 3)

def drawvoltageX ():
    x1, y1 = posiciones[cont-1]
    x2, y2 = posiciones[cont]
    
    if(x1 > x2):  
        pygame.draw.line(screen, (0, 255, 0), (x1,y1), (((x1+x2)/2)+5, y1), 3)  # Node 1 connection
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)-5, y2), (x2,y2), 3)  # Node 2 connection
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)-5,y1+20), (((x1+x2)/2)-5, y1-20), 3)  
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)+5, y2+10), (((x1+x2)/2)+5,y2-10), 3)  
    else:
        pygame.draw.line(screen, (0, 255, 0), (x1,y1), (((x1+x2)/2)-5, y1), 3)  # Node 1 connection
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)+5, y2), (x2,y2), 3)  # Node 2 connection
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)-5,y1+10), (((x1+x2)/2)-5, y1-10), 3)  
        pygame.draw.line(screen, (0, 255, 0), (((x1+x2)/2)+5, y2+20), (((x1+x2)/2)+5,y2-20), 3) 

#CABLES
def draw_line(start_pos):
    pygame.draw.line(screen, (128,128,128), start_pos, posiciones[cont], 3)

#PANTALLA PRINCIPAL
pygame.init ()
width, height = 1200, 600 #tama no de la ventana
screen = pygame.display.set_mode((width, height))

bg = 0,0,0 #rgb colors
screen.fill(bg)#llenamos o pintamos de ese color
pygame.display.set_caption("Simulador de circuitos simples mediante análisis modal")
imagen1 = pygame.image.load("daimakura gawr gura.jpg")
screen.blit(imagen1,(900,00))

#TEXTO 
# Definir los colores
WHITE = (255, 255, 255)
ORANGE = (0, 0, 255)

font = pygame.font.Font(None, 24)

# Definir el texto inicial
text = "Valor: 0"

def update_text(i,value):
    global text
    text = f"Resistencia n° {i+1}: {value}"

def draw_surface():
    # Crear una superficie con fondo transparente
    surface = pygame.Surface((300, 200), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 128))  # Fondo semitransparente
    
    # Dibujar el borde de la superficie
    pygame.draw.rect(surface, ORANGE, surface.get_rect(), 2)
    
    # Renderizar el texto en la superficie
    text_surface = font.render(text, True, ORANGE)
    
    # Centrar el texto en la superficie
    text_rect = text_surface.get_rect(center=(100, 50))
    
    # Dibujar el texto en la superficie
    surface.blit(text_surface, text_rect)
    
    # Dibujar la superficie en la esquina superior izquierda de la ventana principal
    screen.blit(surface, (900, 400))

#creando la malla
nxC, nyC = 45,30
dimxC= (width-300)/nxC
dimyC= height/nyC

fps = 60
timer = pygame.time.Clock()
run=True

while run:#logica que se ejecutara durante todo el simulador
    timer.tick(fps)
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0, 0, 255), screen.get_rect(), 2)

    for event in pygame.event.get():#obtenemos todos los eventos
      
        if event.type == pygame.QUIT:
            run =False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if keyboard.is_pressed("a"):
                tipocomponente = "RESISTENCIA"
            elif keyboard.is_pressed("s"):
                tipocomponente = "VOLTAJE"
            elif keyboard.is_pressed("d"):
                tipocomponente = "CABLE"
                
            if pygame.mouse.get_pressed()[0]:
                drawNodo(mouse_position)
                cont = cont + 1
                    
            elif pygame.mouse.get_pressed()[2]:
                drawimportantnodo(mouse_position)
                cantImportante = cantImportante + 1
            

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for i in range(0,len(pos_resistencias_inicial),1):
        
        if(pos_resistencias_final[i] > pos_resistencias_inicial[i]):
            res_x1, res_y1 = pos_resistencias_inicial[i]
            res_x2, res_y2 = pos_resistencias_final[i]
        else:
            res_x1, res_y1 = pos_resistencias_final[i]
            res_x2, res_y2 = pos_resistencias_inicial[i]

        if res_x1 - 10 <= mouse_x <= res_x2 + 10 and res_y1 - 10<= mouse_y <= res_y2 + 10:
            # El mouse está cerca de la resistencia, cambiar su valor
            if event.type == pygame.KEYDOWN:
            # Cambiar el valor cuando se presione una tecla
                if event.key == pygame.K_UP:
                    new_value = 10
                    resistencias[i] = resistencias[i] + new_value
                    update_text(i,resistencias[i])
                elif event.key == pygame.K_DOWN:
                    new_value = -10
                    resistencias[i] = resistencias[i] + new_value
                    update_text(i,resistencias[i])
            update_text(i,resistencias[i])
            draw_surface()
        else:
            pass

    
    pygame.display.update()

pygame.quit()
