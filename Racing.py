#Se importan las librerias necesarias
import pygame, sys, time
import os.path
import Menu as Menu_inicio
import random
from pygame.locals import *
from itertools import groupby
import pickle


class CarRacing:
    def __init__(self):
        
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()

    def initialize(self):

        self.crashed = False

        self.carImg = pygame.image.load('img/car.png')
        self.car_x_coordinate = (self.display_width * 0.45)
        self.car_y_coordinate = (self.display_height * 0.8)
        self.car_width = 49

        # obras
        self.enemy_car = pygame.image.load('img/obras.png')
        self.enemy_car_startx = random.randrange(310, 460)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 49
        self.enemy_car_height = 100
        
        # huecos
        self.enemy_car2 = pygame.image.load('img/hueco.png')
        self.enemy_car2_startx = random.randrange(310, 460)
        self.enemy_car2_starty = -600
        self.enemy_car2_speed = 5
        self.enemy_car2_width = 49
        self.enemy_car2_height = 100

        # Fondo
        self.bgImg = pygame.image.load('img/fondo.jpg')
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Dodge')
        self.run_car()

    def run_car(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    if event.key == K_ESCAPE:
                        Menu_inicio.main()                    
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 50

                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 50

            self.gameDisplay.fill(self.black)
            self.back_ground_raod()
            if (self.count <= 1100):
                self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
                self.enemy_car_starty += self.enemy_car_speed

                if self.enemy_car_starty > self.display_height:
                    self.enemy_car_starty = 0 - self.enemy_car_height
                    self.enemy_car_startx = random.randrange(310, 460)

                self.car(self.car_x_coordinate, self.car_y_coordinate)
                self.highscore(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.enemy_car_speed += 0.5
                    self.bg_speed += 0.5
                    
            if (2500>=self.count >1100):
                self.run_enemy_car2(self.enemy_car2_startx, self.enemy_car2_starty)
                self.enemy_car2_starty += self.enemy_car2_speed

                if self.enemy_car2_starty > self.display_height:
                    self.enemy_car2_starty = 0 - self.enemy_car2_height
                    self.enemy_car2_startx = random.randrange(310, 460)

                self.car(self.car_x_coordinate, self.car_y_coordinate)
                self.highscore(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.enemy_car2_speed += 1
                    self.bg_speed += 0.5
            if (self.count >2500):

                numbers= list(range(310, 460))                
                self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
                self.enemy_car_starty += self.enemy_car_speed

                if self.enemy_car_starty > self.display_height:
                    self.enemy_car_starty = 0 - self.enemy_car_height
                    self.enemy_car_startx = random.choice(numbers)

                self.car(self.car_x_coordinate, self.car_y_coordinate)
                self.highscore(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.enemy_car_speed += 1
                    self.bg_speed += 0.5
                ###################################################################
                self.run_enemy_car2(self.enemy_car2_startx, self.enemy_car2_starty)
                self.enemy_car2_starty += self.enemy_car2_speed

                if self.enemy_car2_starty > self.display_height:
                    self.enemy_car2_starty = 0 - self.enemy_car2_height
                    numbers.remove(self.enemy_car_startx)
                    self.enemy_car2_startx = random.choice(numbers)

                self.car(self.car_x_coordinate, self.car_y_coordinate)
                self.highscore(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.enemy_car2_speed += 1
                    self.bg_speed += 0.5
                

            

            if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or self.car_x_coordinate + self.car_width > self.enemy_car_startx and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                    ###Guardado###
                    matrix = []
                    if(os.path.exists("Historial_CRacing.txt")):
                        archivo=open("Historial_CRacing.txt","rb")
                        linea=pickle.load(archivo)
                        matrix=linea
                        archivo.close()
                    matrix.append([self.count])

                    matrix.sort(reverse=True)
                    
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    
                    archivo=open("Historial_CRacing.txt","wb")
                    pickle.dump(matrix,archivo)
                    archivo.close()             
                                      
                    self.display_message("Game Over !!!")
            if self.car_y_coordinate < self.enemy_car2_starty + self.enemy_car2_height:
                if self.car_x_coordinate > self.enemy_car2_startx and self.car_x_coordinate < self.enemy_car2_startx + self.enemy_car2_width or self.car_x_coordinate + self.car_width > self.enemy_car2_startx and self.car_x_coordinate + self.car_width < self.enemy_car2_startx + self.enemy_car2_width:
                    ###Guardado###
                    matrix = []
                    if(os.path.exists("Historial_CRacing.txt")):
                        archivo=open("Historial_CRacing.txt","rb")
                        linea=pickle.load(archivo)
                        matrix=linea
                        archivo.close()
                    matrix.append([self.count])
 
                    matrix.sort(reverse=True)
                    
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    
                    archivo=open("Historial_CRacing.txt","wb")
                    pickle.dump(matrix,archivo)
                    archivo.close() 
                    
                    self.display_message("Game Over !!!")

            if self.car_x_coordinate < 310 or self.car_x_coordinate > 460:
                self.crashed = True
                
                self.display_message("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        
        pygame.display.update()
        self.clock.tick(60)
        time.sleep(1)
        car_racing = CarRacing()
        car_racing.initialize()
        car_racing.racing_window()

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))
    def run_enemy_car2(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car2, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

def main():
    car_racing = CarRacing()
    car_racing.racing_window()
