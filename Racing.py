#Se importan las librerias necesarias
import pygame, sys, time
import os.path
import Menu as Menu_inicio #Libreria para el manejo del menú principal y sub menú
import random               #Libreria para importar pseudoaleatoriedad en el juego
from pygame.locals import * #Libreria Pygame para el manejo de vectores
from itertools import groupby
import pickle #Libreria para poder guardar archivos.txt como binarios

"""
Se crea la clase CR_Racing
"""
class CR_Racing: 
    def __init__(self): 
        """
        __init__ es el metodo constructor Python se ejecuta despues de crea un nuevo objeto
        Se usa para para cuando se crea un objecto de la clase para inicializar los atributos de la clase
        
        @param self: convencionalmente es el primer parametro de todos los metodos.
        self es necesario para acceder a los atributos y metodos del objecto
        """
       
        pygame.init()       #Se inicializa el modulo de pygame
        #Se le dan los atributos al modulo display para seleccionar como se visualizara el juego
        self.display_width = 800    #Ancho de display en pantalla
        self.display_height = 600   #Altura de display en pantalla
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.inicializar()

    def inicializar(self):
        """
        Funcion para inicializar el juego
        donde a cada objeto se le asignan unas condiciones iniciales
        """

        """
        car es nuevo objeto principal, nuestro automovil
        """
        #Los atributos de car

        self.crashed = False #Atributo de se choco, se inicializa con falso para indicar que no ha chocado

        self.carImg = pygame.image.load('img/car.png') #Se importa la imagen del carro 
        self.car_x_coordenada = (self.display_width * 0.45) #Se definen la pos inic en x
        self.car_y_coordenada = (self.display_height * 0.8)  #Se definen la pos inic en y
        self.car_width = 49 #La dimension de ancho del carro
        
        
        """
        Hueco como obstaculo en la carretera
        """
        #Los atributos del hueco
        self.hueco = pygame.image.load('img/hueco.png') #Se importa la imagen para el hueco
        #La aleatoriedad del obstaculo se puso unicamente en el x, 
        # ya que al moverse de arriba hacia abajo no es convieniente variar la posicion inicial en el eje y
        # debido a que la jugabilidad se vendria a menos
        self.hueco_startx = random.randrange(310, 460)   #Posicion horizontal aleatoria en donde puede aparecer el obstaculo
        self.hueco_starty = -4500         #Posicion inicial en y
        self.hueco_speed = 3             #Velocidad inicial
        self.hueco_width = 49           #Ancho del obstaculo
        self.hueco_height = 49          #Largo del obstaculo

        
        """
        Obras o trabajos como obstaculo en la carretera
        """
        #Los atributos de obras
        self.obras = pygame.image.load('img/obras.png') ##Se importa la imagen para la obra de construccion
        #La aleatoriedad del obstaculo se puso unicamente en el x, 
        # ya que al moverse de arriba hacia abajo no es convieniente variar la posicion inicial en el eje y
        # debido a que la jugabilidad se vendria a menos
        self.obras_startx = random.randrange(310, 460) #Posicion horizontal aleatoria en donde puede aparecer el obstaculo
        self.obras_starty = -4500    #Posicion inicial en y
        self.obras_speed = 3        #Velocidad inicial
        self.obras_width = 49       #Ancho del obstaculo
        self.obras_height = 49      #Largo del obstaculo


        """
        Cono como obstaculo en la carretera 
        """
        #Los atributos de cono
        self.cono = pygame.image.load('img/cono.png') ##Se importa la imagen para la obra de construccion
        #La aleatoriedad del obstaculo se puso unicamente en el x, 
        # ya que al moverse de arriba hacia abajo no es convieniente variar la posicion inicial en el eje y
        # debido a que la jugabilidad se vendria a menos
        self.cono_startx = random.randrange(310, 460) #Posicion horizontal aleatoria en donde puede aparecer el obstaculo
        self.cono_starty = -4500    #Posicion inicial en y
        self.cono_speed = 3        #Velocidad inicial
        self.cono_width = 49       #Ancho del obstaculo
        self.cono_height = 49      #Largo del obstaculo
        
        """
        Vaca como obstaculo en la carretera 
        """
        #Los atributos de vaca
        self.vaca = pygame.image.load('img/vaca.png') ##Se importa la imagen para la obra de construccion
        #La aleatoriedad del obstaculo se puso unicamente en el x, 
        # ya que al moverse de arriba hacia abajo no es convieniente variar la posicion inicial en el eje y
        # debido a que la jugabilidad se vendria a menos
        self.vaca_startx = random.randrange(310, 460) #Posicion horizontal aleatoria en donde puede aparecer el obstaculo
        self.vaca_starty = -4500    #Posicion inicial en y
        self.vaca_speed = 3        #Velocidad inicial
        self.vaca_width = 49       #Ancho del obstaculo
        self.vaca_height = 49      #Largo del obstaculo

       
        """
        Fondo consiste en la carretera en la viaja el carro
        se utiliza el acronimo bg de background
        """
        #Los atributos de fondo
        self.bgImg = pygame.image.load('img/fondo.jpg')
        self.bg_x1 = (self.display_width / 2) - (360 / 2) #Los rangos en que se muestra la carretera
        self.bg_x2 = (self.display_width / 2) - (360 / 2) 
        self.bg_y1 = 0
        self.bg_y2 = -4500
        self.bg_speed = 2 #Esta es la velocidad relativa del auto en la direccion opuesta
        self.count = 0

        #Imagen cuando el jugador pierde en el juego.
        self.multa = pygame.image.load('img/multa.jpg')



    def car(self, car_x_coordenada, car_y_coordenada):
        """
        funcion car

        @param self: la instancia de la clase
        @param car_x_coordenada:  la posicion en el eje x-horizontal
        @param car_y_coordenada:  la posicion en el eje y-vertical        
        """
        #gameDisplay.blit dibuja la imagen del auto en la pantalla
        self.gameDisplay.blit(self.carImg, (car_x_coordenada, car_y_coordenada))


    def racing_pantalla(self):
        """
        Esta funcion crea una ventana (display) del juego
        
        @param self: la instancia de la clase
        """
        #Inicializa la ventana en pantalla a mostrar
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('CR-Racing')
        self.run_car()


           


    def run_car(self):
        """
        Esta funcion que crea la dinamica de juego para el carro

        @param self: la instancia de la clase
        """
        #Condicion de juego mientras no haya chocado
        while not self.crashed:  
            
            #Ciclo para registrar todos los eventos que ocurren durante el juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Si se termina juego
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.KEYDOWN):
                    if event.key == K_ESCAPE:           #Para regresar el menu principal
                        Menu_inicio.main()                    
                    if (event.key == pygame.K_LEFT):    #Cambio de posicion de carro a la izquierda
                        self.car_x_coordenada -= 50
                       
                    if (event.key == pygame.K_RIGHT):   #Cambio de posicion de carro a la izquierda  
                        self.car_x_coordenada += 50
                        

            self.gameDisplay.fill(self.black)       
            self.fondo_carretera()
            
            """
            Condicion de la dificultad asociado con la puntuacion: Nivel 1
            Aparece de obstaculos obras 
            """
            if (self.count <= 1100):
                self.run_obras(self.obras_startx, self.obras_starty)
                self.obras_starty += self.obras_speed

                if self.obras_starty > self.display_height:
                    self.obras_starty = 0 - self.obras_height
                    self.obras_startx = random.randrange(310, 460)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.obras_speed += 0.5
                    self.bg_speed += 0.5
            
            """
            Condicion de la dificultad asociado con la puntuacion: Nivel 2
            Aparece de obstaculos huecos 
            """        
            if (3500>=self.count >2500):
                self.run_hueco(self.hueco_startx, self.hueco_starty)
                self.hueco_starty += self.hueco_speed

                if self.hueco_starty > self.display_height:
                    self.hueco_starty = 0 - self.hueco_height
                    self.hueco_startx = random.randrange(310, 460)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.hueco_speed += 1
                    self.bg_speed += 0.5
            
            """
            Condicion de la dificultad asociado con la puntuacion: Nivel 3
            Aparece de obstaculos huecos  y obras
            """
            
            if (2500>=self.count >1100):

                numbers= list(range(310, 460))                
                self.run_obras(self.obras_startx, self.obras_starty)
                self.obras_starty += self.obras_speed

                if self.obras_starty > self.display_height:
                    self.obras_starty = 0 - self.obras_height
                    self.obras_startx = random.choice(numbers)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.obras_speed += 1
                    self.bg_speed += 0.5
                ###################################################################
                self.run_hueco(self.hueco_startx, self.hueco_starty)
                self.hueco_starty += self.hueco_speed

                if self.hueco_starty > self.display_height:
                    self.hueco_starty = 0 - self.hueco_height
                    numbers.remove(self.obras_startx)
                    self.hueco_startx = random.choice(numbers)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.hueco_speed += 1
                    self.bg_speed += 0.5
            
            """
            Condicion de la dificultad asociado con la puntuacion: Nivel 4
            Aparece de obstaculos vaca  y cono
            """
            
            if (self.count >3500):

                numbers= list(range(310, 460))                
                self.run_vaca(self.vaca_startx, self.vaca_starty)
                self.vaca_starty += self.vaca_speed

                if self.vaca_starty > self.display_height:
                    self.vaca_starty = 0 - self.vaca_height
                    self.vaca_startx = random.choice(numbers)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.vaca_speed += 1
                    self.bg_speed += 0.5
                ###################################################################
                self.run_cono(self.cono_startx, self.cono_starty)
                self.cono_starty += self.cono_speed

                if self.cono_starty > self.display_height:
                    self.cono_starty = 0 - self.cono_height
                    numbers.remove(self.obras_startx)
                    self.cono_startx = random.choice(numbers)

                self.car(self.car_x_coordenada, self.car_y_coordenada)
                self.puntaje(self.count)
                self.count += 1
                if (self.count % 100 == 0):
                    self.cono_speed += 1
                    self.bg_speed += 0.5         

            """
            Para de que termina y para guardar el puntaje cuando choque con un objeto 'obras' en un archivo .txt
    
            """
            if self.car_y_coordenada < self.obras_starty + self.obras_height:
                if self.car_x_coordenada > self.obras_startx and self.car_x_coordenada < self.obras_startx + self.obras_width or self.car_x_coordenada + self.car_width > self.obras_startx and self.car_x_coordenada + self.car_width < self.obras_startx + self.obras_width:
                    
                    #Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores
                    matrix = []
                    # Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta #
                    if(os.path.exists("Historial_CRacing.txt")):
                        #Apertura del txt en modo binario 
                        archivo=open("Historial_CRacing.txt","rb") #Se abre el archivo txt
                        #Lectura y cargado en variable de las lineas del archivo
                        linea=pickle.load(archivo)
                        #Guardado de la matriz encontrada para en la matriz matrix para su uso
                        matrix=linea
                        #Cerrado del txt
                        archivo.close()
                    #Se agrega a la matriz encontrada el valor de la partida actual #
                    matrix.append([self.count])

                    #Se acomoda la matriz de mayor a menor
                    matrix.sort(reverse=True)
                    #Se eliminan duplicados
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    #Apertura del txt en modo binario
                    archivo=open("Historial_CRacing.txt","wb")
                    #Escritura de lo cargado en variable para las lineas del archivo 
                    pickle.dump(matrix,archivo)
                    #Cerrado del txt 
                    archivo.close()             
                                    
                    self.display_message()
            
            """
            Para de que termina y para guardar el puntaje cuando choque con un objeto 'hueco' en un archivo .txt
    
            """
            if self.car_y_coordenada < self.hueco_starty + self.hueco_height:
                if self.car_x_coordenada > self.hueco_startx and self.car_x_coordenada < self.hueco_startx + self.hueco_width or self.car_x_coordenada + self.car_width > self.hueco_startx and self.car_x_coordenada + self.car_width < self.hueco_startx + self.hueco_width:
                    
                    #Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores
                    matrix = []
                    # Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta #
                    if(os.path.exists("Historial_CRacing.txt")):
                        #Apertura del txt en modo binario 
                        archivo=open("Historial_CRacing.txt","rb") #Se abre el archivo txt
                        #Lectura y cargado en variable de las lineas del archivo
                        linea=pickle.load(archivo)
                        #Guardado de la matriz encontrada para en la matriz matrix para su uso
                        matrix=linea
                        #Cerrado del txt
                        archivo.close()
                    #Se agrega a la matriz encontrada el valor de la partida actual #
                    matrix.append([self.count])

                    #Se acomoda la matriz de mayor a menor
                    matrix.sort(reverse=True)
                    #Se eliminan duplicados
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    #Apertura del txt en modo binario
                    archivo=open("Historial_CRacing.txt","wb")
                    #Escritura de lo cargado en variable para las lineas del archivo 
                    pickle.dump(matrix,archivo)
                    #Cerrado del txt 
                    archivo.close()             
                                    
                    self.display_message()

            """
            Para de que termina y para guardar el puntaje cuando choque con un objeto 'vaca' en un archivo .txt
    
            """
            if self.car_y_coordenada < self.vaca_starty + self.vaca_height:
                if self.car_x_coordenada > self.vaca_startx and self.car_x_coordenada < self.vaca_startx + self.vaca_width or self.car_x_coordenada + self.car_width > self.vaca_startx and self.car_x_coordenada + self.car_width < self.vaca_startx + self.vaca_width:
                    
                    #Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores
                    matrix = []
                    # Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta #
                    if(os.path.exists("Historial_CRacing.txt")):
                        #Apertura del txt en modo binario 
                        archivo=open("Historial_CRacing.txt","rb") #Se abre el archivo txt
                        #Lectura y cargado en variable de las lineas del archivo
                        linea=pickle.load(archivo)
                        #Guardado de la matriz encontrada para en la matriz matrix para su uso
                        matrix=linea
                        #Cerrado del txt
                        archivo.close()
                    #Se agrega a la matriz encontrada el valor de la partida actual #
                    matrix.append([self.count])

                    #Se acomoda la matriz de mayor a menor
                    matrix.sort(reverse=True)
                    #Se eliminan duplicados
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    #Apertura del txt en modo binario
                    archivo=open("Historial_CRacing.txt","wb")
                    #Escritura de lo cargado en variable para las lineas del archivo 
                    pickle.dump(matrix,archivo)
                    #Cerrado del txt 
                    archivo.close()             
                                    
                    self.display_message()
            
            """
            Para de que termina y para guardar el puntaje cuando choque con un objeto 'cono' en un archivo .txt

            """
            if self.car_y_coordenada < self.cono_starty + self.cono_height:
                if self.car_x_coordenada > self.cono_startx and self.car_x_coordenada < self.cono_startx + self.cono_width or self.car_x_coordenada + self.car_width > self.cono_startx and self.car_x_coordenada + self.car_width < self.cono_startx + self.cono_width:
                    
                    #Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores
                    matrix = []
                    # Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta #
                    if(os.path.exists("Historial_CRacing.txt")):
                        #Apertura del txt en modo binario 
                        archivo=open("Historial_CRacing.txt","rb") #Se abre el archivo txt
                        #Lectura y cargado en variable de las lineas del archivo
                        linea=pickle.load(archivo)
                        #Guardado de la matriz encontrada para en la matriz matrix para su uso
                        matrix=linea
                        #Cerrado del txt
                        archivo.close()
                    #Se agrega a la matriz encontrada el valor de la partida actual #
                    matrix.append([self.count])

                    #Se acomoda la matriz de mayor a menor
                    matrix.sort(reverse=True)
                    #Se eliminan duplicados
                    matrix = list(lista for lista, _ in groupby(matrix))
                     
                    #Apertura del txt en modo binario
                    archivo=open("Historial_CRacing.txt","wb")
                    #Escritura de lo cargado en variable para las lineas del archivo 
                    pickle.dump(matrix,archivo)
                    #Cerrado del txt 
                    archivo.close()             
                                    
                    self.display_message()

            """
            Para de que termina si se sale de la carretera y para guardar el puntaje en un archivo .txt

            """
            if self.car_x_coordenada < 310 or self.car_x_coordenada > 460:
                self.crashed = True
                
                #Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores
                matrix = []
                # Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta #
                if(os.path.exists("Historial_CRacing.txt")):
                        #Apertura del txt en modo binario 
                        archivo=open("Historial_CRacing.txt","rb") #Se abre el archivo txt
                        #Lectura y cargado en variable de las lineas del archivo
                        linea=pickle.load(archivo)
                        #Guardado de la matriz encontrada para en la matriz matrix para su uso
                        matrix=linea
                        #Cerrado del txt
                        archivo.close()
                #Se agrega a la matriz encontrada el valor de la partida actual #
                matrix.append([self.count])

                #Se acomoda la matriz de mayor a menor
                matrix.sort(reverse=True)
                #Se eliminan duplicados
                matrix = list(lista for lista, _ in groupby(matrix))
                     
                #Apertura del txt en modo binario
                archivo=open("Historial_CRacing.txt","wb")
                #Escritura de lo cargado en variable para las lineas del archivo 
                pickle.dump(matrix,archivo)
                #Cerrado del txt 
                archivo.close()


                self.display_message()

            pygame.display.update()
            self.clock.tick(60)


    def display_message(self):
        """
        Esta funcion para mostrar el mensaje una vez que haya finalizado la partida

        @param self: la instancia de la clase
        
        """
        
        self.gameDisplay.blit( self.multa, (0,100)) #Llama a la imagen que 'multa.png'
        pygame.display.update()
        self.clock.tick(60)
        time.sleep(1)
        car_racing = CR_Racing()
        car_racing.inicializar()
        car_racing.racing_pantalla()


    def fondo_carretera(self):
        """
        Esta funcion le da movimiento al fondo (movimiento relativo del carro)
        y la vuelve a iniciar en loop para dar sentimiento de continuidad
        @param self: la instancia de la clase
        """

        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed         #Velocidad de la carretera
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:       #Condicion para que una vez finalizada la carretera comience de nuevo
            self.bg_y1 = -4500

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -4500



    def run_hueco(self, pos_x, pos_y):
        """
        Esta funcion para mostrar en pantalla al objeto "hueco"

        @param self: la instancia de la clase
        @param pos_x: valor asociado con la posicion en x del objeto
        @param pos_y: valor asociado con la posicion en y del objeto
        """
        self.gameDisplay.blit(self.hueco, (pos_x, pos_y))


    def run_obras(self, pos_x, pos_y):
        """
         Esta funcion para mostrar en pantalla al objeto "obras" 

        @param self: la instancia de la clase
        @param pos_x: valor asociado con la posicion en x del objeto
        @param pos_y: valor asociado con la posicion en y del objeto
        """
        self.gameDisplay.blit(self.obras, (pos_x, pos_y))



    def run_vaca(self, pos_x, pos_y):
        """
         Esta funcion para mostrar en pantalla al objeto "vaca" 

        @param self: la instancia de la clase
        @param pos_x: valor asociado con la posicion en x del objeto
        @param pos_y: valor asociado con la posicion en y del objeto
        """
        self.gameDisplay.blit(self.vaca, (pos_x, pos_y))

    def run_cono(self, pos_x, pos_y):
        """
        Esta funcion para mostrar en pantalla al objeto "vaca"  

        @param self: la instancia de la clase
       @param pos_x: valor asociado con la posicion en x del objeto
        @param pos_y: valor asociado con la posicion en y del objeto
        """
        self.gameDisplay.blit(self.cono, (pos_x, pos_y))

    def puntaje(self, count):
        """
        Esta funcion para mostrar el puntuaje actual en la pantalla (display)

        @param self: la instancia de la clase
        @param count: el contador del puntaje
        """
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))


def main():
    """
    Funcion principal en donde se llama a la clase CR_Rancing()
    y la funcion que crea la pantalla del juego
    """
    car_racing = CR_Racing()
    car_racing.racing_pantalla()
