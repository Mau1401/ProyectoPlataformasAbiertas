# Importacion de librerias #
import pygame, sys, time
import os.path
import pickle
from pygame.locals import *
from colours import *
from random import *
import J2048 as Juego2048
import Racing as Racing
# Variables para determianr el color de los textos y fondo #
FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)
# Variable para el manejo del tamaño de la pantalla principal del menú #
dimensiones = [600, 460]

# Inicializacion de pygame #
pygame.init()
# Variables en las cuales se almacena las dimenciones, imagenes necesarias para cada uno de los botones y fondos, además de el tipo de letras a usar con su respectivo tamaño. #
pantalla = pygame.display.set_mode(dimensiones)
imagen_panel = pygame.image.load("img/panel.png")
imagen_boton = pygame.image.load("img/button.png")
imagen_boton_pressed = pygame.image.load("img/buttonPressed.png")
fuente = pygame.font.SysFont('Courier', 15)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)


#_________________________________________________________________________________________#
def main():
    # Establece el Tiempo en la variable clock #
    clock = pygame.time.Clock()
    # Creacion de los botones del menú principal #
    button_1 = imagen_boton.get_rect()
    button_2 = imagen_boton.get_rect()
    button_3 = imagen_boton.get_rect()
    button_4 = imagen_boton.get_rect()
    button_5 = imagen_boton.get_rect()
    # En la variable botones se van guardando cada uno de los botones con sus propiedades #
    botones = []

    # Posicion exacta del pintado  de los botones#
    button_1.topleft = [200, 70]
    # Asignado del texto e imagen de cada uno de los botones#
    botones.append({'texto': "  2048  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_1, 'on_click': False})
    
    button_2.topleft = [200, 140]    
    botones.append({'texto': "  CR Racing  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_2, 'on_click': False})

    button_3.topleft = [200, 210]
    botones.append({'texto': "Historial 2048", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_3, 'on_click': False})

    button_4.topleft = [200, 280]
    botones.append({'texto': "Historial CR Rancing", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_4, 'on_click': False})

    button_5.topleft = [200, 350]
    botones.append({'texto': "Creditos", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_5, 'on_click': False})
    # Se asigna el click false ya que inicialmente no debe estar presionado el boton fisicamente #
    click = False
    # While finito para el uso del menu y pintado de los elementos de la interfaz #
    while True:
        #For para su repectiva actualicion de los eventos#
        for event in pygame.event.get():
            if event.type == QUIT:
                # Caso en el que se presiona la cruz de la ventana, da un cierre de pygame y la salida del programa #
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Caso en el que se presiona el boton fisico "esc", da un cierre de pygame y la salida del programa #
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # Caso en el que el boton de mouse(raton) se envian los parametros del mouse para dar las posiciones donde se hizo el click#
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                #Caso en el que el boton de mouse(raton) no se presiona se reitera el click como false#
                for boton in botones:
                    boton['on_click'] = False
      
        
        # Manejo de la matriz de botos#
        if botones[0]['on_click'] and click:
            #Seleccion de la posicion 0 donde llama a la funcion J_2048 #
            J_2048()
            click = False
        if botones[1]['on_click'] and click:
            #Seleccion de la posicion 1 donde llama a la funcion CR_Racing #
            CR_Racing()
            click = False
        
        if botones[2]['on_click'] and click:
            #Seleccion de la posicion 4 donde llama a la funcion Historial_2048 #
            Historial_2048()
            click = False
        if botones[3]['on_click'] and click:
            #Seleccion de la posicion 4 donde llama a la funcion Historial_CR_Racing #
            Historial_CR_Racing()
            click = False
        if botones[4]['on_click'] and click:
            #Seleccion de la posicion 4 donde llama a la funcion Creditos #
            Creditos()
            click = False
        # Al existir el problema de la salida de la ventana a una diferente de su tamaño se tiene la solucion de reiterar con su tamaño para que se asigne el necesario #
        dimensiones = [600, 460]
        # Set de las dimensiones de la pantalla del menú principal #
        pantalla = pygame.display.set_mode(dimensiones)
        #Se le asigma el nombre a la venta de la aplicacion cuando está en el menú#
        pygame.display.set_caption("Programación Bajo Plataformas Abiertas")
        #Se rellena el fondo con el color designado para dar el efecto de destruido con un negro un poco claro #
        pantalla.fill(FONDO)
        #Se dibujan los botones con la función dibujar_botones_iniciales#
        dibujar_botones_iniciales(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
#_________________________________________________________________________________________#
# Pintado de los textos en fondo negro #
def Pintar_Texto_en_fondo_negro(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#_________________________________________________________________________________________#
# Pintado de los textos en fondo personalizado #
def Pintar_Texto_en_fondo(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])
#_________________________________________________________________________________________#
# Pintado de los botones #
def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [560, 420])
    pantalla.blit(panel, [20, 20])
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        Pintar_Texto_en_fondo(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)
#_________________________________________________________________________________________#
# Funcion para el manejo del sub menú para la seleccion de los tamaño de las matriz del juego 2048 #
# No se comenta ya que posee los mismos funcionamientos del menú principal solo que cambian las debidas etiquetas de los elemento #
def J_2048():
    
    clock = pygame.time.Clock()
    button_1 = imagen_boton.get_rect()
    button_2 = imagen_boton.get_rect()
    button_3 = imagen_boton.get_rect()
    
    botones = []
    button_1.topleft = [200, 100]
    botones.append({'texto': "  3X3  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_1, 'on_click': False})

    button_2.topleft = [200, 200]    
    botones.append({'texto': "  4X4  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_2, 'on_click': False})

    button_3.topleft = [200, 300]
    botones.append({'texto': "  5X5  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_3, 'on_click': False})
    click = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
      
        
        if botones[0]['on_click'] and click:

            tamano3x3()
            click = False
            
        if botones[1]['on_click'] and click:

            tamano4x4()
            click = False
        
        if botones[2]['on_click'] and click:
            tamano5x5()
            click = False
        dimensiones = [600, 460]
        pantalla = pygame.display.set_mode(dimensiones)
        pygame.display.set_caption("2048")
        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
#_________________________________________________________________________________________#

# Funcion para mandar el tamaño 3x3 al juego 2048 #
def tamano3x3():
    Juego2048.main(tamano = 3)
#_________________________________________________________________________________________#
# Funcion para mandar el tamaño 4x4 al juego 2048 #
def tamano4x4():
    Juego2048.main(tamano = 4)
#_________________________________________________________________________________________#
# Funcion para mandar el tamaño 5x5 al juego 2048 #   
def tamano5x5():
    Juego2048.main(tamano = 5)
#_________________________________________________________________________________________# 
# Llamado al juego CR Racing #
def CR_Racing():
    Racing.main()
#_________________________________________________________________________________________#
# Funcion para la impresion del historial para el juego CR Racing #      
def Historial_CR_Racing():
    
    while True:
          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Historial CR Racing")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        # Variable para el manejo la matriz guardada en el .txt binario #
        matrix = []
        contador=2
        # Con la libreria os se garatinza la existencia de Historial_CRacing.txt en la carpeta #
        if(os.path.exists("Historial_CRacing.txt")): # Apertura del txt en modo binario #
            archivo=open("Historial_CRacing.txt","rb") # Lectura y cargado en variable de las lineas del archivo #
            linea=pickle.load(archivo)
            matrix=linea # Guardado de la matriz encontrada para en la matriz matrix para su uso #
            archivo.close() # Cerrado del txt #
        # Se crean dos condiciones de impresión si hay una cantidad mayor a 20 de jugadas o menor a 20 #
        # Y con la ayuda de Pintar_Texto_en_fondo_negro y un recorrido por la matriz se hace la impresión #
        
        if(len(matrix)>=20):

            for i in range(0,20):
                Pintar_Texto_en_fondo_negro("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
                contador= contador+1
        if(len(matrix)<20):
            
            for i in range(len(matrix)):
                Pintar_Texto_en_fondo_negro("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
                contador= contador+1      
        # Eventos de salida de la ventana de impresión #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
        
        pygame.display.update()
        mainClock.tick(60)

#_________________________________________________________________________________________#
# Funcion para la impresion del historial para el juego 2048 #
# Posee un funcionamiento igual al de Historial_CR_Racing pero con el txt Historial_2048.txt #
def Historial_2048():
    
    while True:
          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Historial 2048")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        
        matrix = []
        contador=2
        if(os.path.exists("Historial_2048.txt")):
            archivo=open("Historial_2048.txt","rb")
            linea=pickle.load(archivo)
            matrix=linea
            archivo.close()
            
        
        if(len(matrix)>=20):
            for i in range(0,20):
                Pintar_Texto_en_fondo_negro("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
                contador= contador+1
        if(len(matrix)<20):
            for i in range(len(matrix)):
                Pintar_Texto_en_fondo_negro("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
                contador= contador+1 
         
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
        
        pygame.display.update()
        mainClock.tick(60)
#_________________________________________________________________________________________# 
# La funcion Creditos fue creada para la impresion mediante la funcion Pintar_Texto_en_fondo_negro y un while para su actualizacion #     
def Creditos():
    movimiento=-291
    while True:          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Creditos")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        Pintar_Texto_en_fondo_negro('Creditos', font, (255, 255, 255), screen, 270, movimiento-80)         
        Pintar_Texto_en_fondo_negro('Universidad de Costa Rica', font, (255, 255, 255), screen, 215, movimiento-40)
        Pintar_Texto_en_fondo_negro('Escuela de ingeniería eléctrica', font, (255, 255, 255), screen, 205, movimiento-10)               
        Pintar_Texto_en_fondo_negro('Programación Bajo Plataformas Abiertas', font, (255, 255, 255), screen, 170, movimiento+20)
        Pintar_Texto_en_fondo_negro('IE-0117', font, (255, 255, 255), screen, 270, movimiento+50)
        Pintar_Texto_en_fondo_negro('II ciclo 2020', font, (255, 255, 255), screen, 260, movimiento+80)
        Pintar_Texto_en_fondo_negro('Profesor', font, (255, 255, 255), screen, 270, movimiento+110)
        Pintar_Texto_en_fondo_negro('Andrés Mora Zúñiga', font, (255, 255, 255), screen, 235, movimiento+140)        
        Pintar_Texto_en_fondo_negro('Estudiantes', font, (255, 255, 255), screen, 260, movimiento+170)
        Pintar_Texto_en_fondo_negro('José Antonio Franchi B32687', font, (255, 255, 255), screen, 200, movimiento+200)
        Pintar_Texto_en_fondo_negro('Mauricio Rodríguez B96694', font, (255, 255, 255), screen, 205, movimiento+230)
        Pintar_Texto_en_fondo_negro('Ronald Rivera Morales B5565', font, (255, 255, 255), screen, 200, movimiento+260)
        Pintar_Texto_en_fondo_negro('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 180, movimiento+290)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
        
        pygame.display.update()
        mainClock.tick(60)
        movimiento=movimiento+1
        time.sleep(0.01)
        if movimiento >=500:
            movimiento=-291
#_________________________________________________________________________________________#
# Llamado inicial para el arranque de del main o menú principal
if __name__ == '__main__':
    main()
#_________________________________________________________________________________________#