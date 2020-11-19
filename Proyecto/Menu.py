# Setup Python ----------------------------------------------- #

import pygame, sys, time
from pygame.locals import *
from colours import *
from random import *

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Programación Bajo Plataformas Abiertas')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('Menú de juegos', font, (255, 255, 255), screen, 80, 20)
        draw_text('Use siempre la tecla "esc" para salir', font, (255, 255, 255), screen, 80, 470)

        mx, my = pygame.mouse.get_pos()       

        button_1 = pygame.Rect(90, 80, 200, 50)
        button_2 = pygame.Rect(90, 160, 200, 50)
        button_3 = pygame.Rect(90, 240, 200, 50)
        button_4 = pygame.Rect(90, 320, 200, 50)
        button_5 = pygame.Rect(90, 400, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                J_2048()
        if button_2.collidepoint((mx, my)):
            if click:
                CR_Racing()
        if button_3.collidepoint((mx, my)):
            if click:
                Historial_2048()
        if button_4.collidepoint((mx, my)):
            if click:
                Historial_CR_Racing()
        if button_5.collidepoint((mx, my)):
            if click:
                Creditos()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('2048', font, (255, 255, 255), screen, 100, 90)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('CR Rancing', font, (255, 255, 255), screen, 100, 170)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Historial 2048', font, (255, 255, 255), screen, 100, 250)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        draw_text('Historial CR Rancing', font, (255, 255, 255), screen, 100, 330)
        pygame.draw.rect(screen, (255, 0, 0), button_5)
        draw_text('Creditos', font, (255, 255, 255), screen, 100, 410)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def J_2048():
      
    running = True
    while running:
        screen.fill((0,0,0))        
        draw_text('Juego 2048', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def CR_Racing():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Juego CR Racing', font, (255, 255, 255), screen, 20, 20)
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
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Historial Juego 2048', font, (255, 255, 255), screen, 20, 20)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def Historial_CR_Racing():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Historial juego CR Racing', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def Creditos():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Creditos', font, (255, 255, 255), screen, 20, 20)
        draw_text('Programación Bajo Plataformas Abiertas', font, (255, 255, 255), screen, 20, 40)
        draw_text('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 20, 60)
        draw_text('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 20, 80)
        draw_text('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 20, 100)
        draw_text('Jonathan Barrantes Castillo B50891', font, (255, 255, 255), screen, 20, 100)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()
