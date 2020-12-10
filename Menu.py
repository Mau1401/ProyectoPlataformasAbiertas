import pygame, sys, time
import os.path
import pickle
from pygame.locals import *
from colours import *
from random import *
import J2048 as J2048
import Racing as Racing

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

pygame.init()
dimensiones = [600, 460]
pantalla = pygame.display.set_mode(dimensiones)
imagen_panel = pygame.image.load("img/panel.png")
imagen_boton = pygame.image.load("img/button.png")
imagen_boton_pressed = pygame.image.load("img/buttonPressed.png")
imagen_text = pygame.image.load("img/panelInset_brown.png")
fuente = pygame.font.SysFont('Courier', 15)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)

Juego2048=J2048

def main():
    clock = pygame.time.Clock()


    button_1 = imagen_boton.get_rect()
    button_2 = imagen_boton.get_rect()
    button_3 = imagen_boton.get_rect()
    button_4 = imagen_boton.get_rect()
    button_5 = imagen_boton.get_rect()
    

    botones = []
    button_1.topleft = [200, 70]
    botones.append({'texto': "  2048  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_1, 'on_click': False})
    
    button_2.topleft = [200, 140]    
    botones.append({'texto': "  CR Racing  ", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_2, 'on_click': False})

    button_3.topleft = [200, 210]
    botones.append({'texto': "Historial 2048", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_3, 'on_click': False})

    button_4.topleft = [200, 280]
    botones.append({'texto': "Historial CR Rancing", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_4, 'on_click': False})

    button_5.topleft = [200, 350]
    botones.append({'texto': "Creditos", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': button_5, 'on_click': False})

    #dibujar_botones_iniciales(botones)
    click = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
      
        
        if botones[0]['on_click'] and click:
            J_2048()
            click = False

        if botones[1]['on_click'] and click:
            CR_Racing()
            click = False
        
        if botones[2]['on_click'] and click:
            Historial_2048()
            click = False
            
        if botones[3]['on_click'] and click:
            Historial_CR_Racing()
            click = False
        if botones[4]['on_click'] and click:
            Creditos()
            click = False
            
        dimensiones = [600, 460]
        pantalla = pygame.display.set_mode(dimensiones)
        pygame.display.set_caption("Programación Bajo Plataformas Abiertas")
        
        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
#_________________________________________________________________________________________#

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])


def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [560, 420])
    pantalla.blit(panel, [20, 20])
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)


def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)

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

    #dibujar_botones_iniciales(botones)
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
        pygame.display.set_caption("Mini menú 2048")
        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



def tamano3x3():
    Juego2048.main(board_size = 3)

def tamano4x4():
    Juego2048.main(board_size = 4)
    
def tamano5x5():
    Juego2048.main(board_size = 5)
    
def CR_Racing():
    mainClock = pygame.time.Clock()
    Racing.main()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)


def Historial_2048():
    
    while True:
          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Historial 2048")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        
        matrix = []
        if(os.path.exists("Historial_2048.txt")):
            archivo=open("Historial_2048.txt","rb")
            linea=pickle.load(archivo)
            matrix=linea
            archivo.close()
            
        contador=2
        for i in range(len(matrix)):
            draw_text("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
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
        
def Historial_CR_Racing():
    
    while True:
          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Historial CR Racing")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        
        matrix = []
        if(os.path.exists("Historial_CRacing.txt")):
            archivo=open("Historial_CRacing.txt","rb")
            linea=pickle.load(archivo)
            matrix=linea
            archivo.close()
            
        contador=2
        for i in range(len(matrix)):
            draw_text("Posicion "+str(i+1)+" # "+str(matrix[i][0]), font, (255, 255, 255), screen, 200, contador*20)
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
        
def Creditos():
    movimiento=-291
    while True:
          
        mainClock = pygame.time.Clock()
        screen = pygame.display.set_mode((600, 460),0,32)
        pygame.display.set_caption("Creditos")
        font = pygame.font.SysFont(None, 20)
        screen.fill((0,0,0))
        draw_text('Creditos', font, (255, 255, 255), screen, 270, movimiento-80)         
        draw_text('Universidad de Costa Rica', font, (255, 255, 255), screen, 215, movimiento-40)
        draw_text('Escuela de ingeniería eléctrica', font, (255, 255, 255), screen, 205, movimiento-10)               
        draw_text('Programación Bajo Plataformas Abiertas', font, (255, 255, 255), screen, 170, movimiento+20)
        draw_text('IE-0117', font, (255, 255, 255), screen, 270, movimiento+50)
        draw_text('II ciclo 2020', font, (255, 255, 255), screen, 260, movimiento+80)
        draw_text('Profesor', font, (255, 255, 255), screen, 270, movimiento+110)
        draw_text('Andrés Mora Zúñiga', font, (255, 255, 255), screen, 235, movimiento+140)        
        draw_text('Estudiantes', font, (255, 255, 255), screen, 260, movimiento+170)
        draw_text('José Antonio Franchi B32687', font, (255, 255, 255), screen, 200, movimiento+200)
        draw_text('Mauricio Rodríguez B96694', font, (255, 255, 255), screen, 205, movimiento+230)
        draw_text('Ronald Rivera Morales B5565', font, (255, 255, 255), screen, 200, movimiento+260)
        draw_text('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 180, movimiento+290)
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

if __name__ == '__main__':
    main()
