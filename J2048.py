#Se importan las librerias necesarias
#Libreria sys se utiliza para poder relaizar los exit al oprimir la "x" de la esquina superior #
import pygame, sys
import os.path #Libreria para el manjeo de .txt #
import Menu as Menu_inicio # Libreria para el manejo del menú principal y sub menú #
import random #Libreria para generar aleatoridad, que va a ser utilizada para la funcion placeRandomTitle #
from colours import * # Libreria para el manejo de los colores deseados para los bloques #
from random import * # Libreria para generar numeros aleatoreos #
from pygame.locals import *# Pygame #
from itertools import groupby #Libreria para el manejo basico de vectores. #
import pickle #Libreria para guaradar archivos txt como binarios. #

# Variables iniciales #
TOTAL_POINTS = 0 #Como no se ha realiza ningun movimiento y solo existe un 2 que se genero por iniciar el juego el score se toma como 0 aunque se tenga un 2 en el tablero. #
DEFAULT_SCORE = 2 #Score minimo nada mas al iniciar el juego ya que siempre se realiza un placeRandomTitle al iniciar el juego. #

# Inicializacion de pygame. #
pygame.init()
# Estandarizacion del tamaño de la ventana del juego. #
SURFACE = pygame.display.set_mode((500, 500), 0, 32)
# Estiqueta del nombre de la ventana del juego. #
pygame.display.set_caption("2048")

myfont = pygame.font.SysFont("monospace", 25)
scorefont = pygame.font.SysFont("monospace", 50)
# Matriz para el manejo de movimientos. #
Matrizpre = []
#_________________________________________________________________________________________#
# Funcion principal del modulo 2048. #
def main(fromLoaded = False, tamano = 4):
	# Variables globales #
	global Tamano 
	global tileMatrix
	# Variable receptora por parametrizacion el tamaño de la cuadricula, en el caso de un reset se coloca en 4 ya que el juego original se establece 4x4. #
	Tamano = tamano
	# Reescritura de las dimensiones para  solucion de los cambios entre pantallas. #
	SURFACE = pygame.display.set_mode((500, 500), 0, 32)
	# Creacion de la matriz vacía #
	tileMatrix = createEmptyMatrix()
	# Creacion de los primeros dos bloques para jugar. #
	if not fromLoaded:
		placeRandomTile()
		placeRandomTile()
	# Mostrado en pantalla de todo lo creado anteriormente. #
	printMatrix()
	# Ciclo para el recorrido del juego. #
	while True:
		# Eventos del juego generales. #
		for event in pygame.event.get():
			if event.type == QUIT:
				# Si se marca la casilla equis de la ventana se sale de todo el juego. #
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					# Si se preciona el boton fisico "esc" de la ventana se limpia la matriz y se devuelve al sub menú de tamaños. #
					restablecer()
					Menu_inicio.J_2048()
			# Condiciones en las que el juego está perdido u pueden proseguir jugando, ya que si no se cumple setGameOverCondicion() == True se va a la pantalla de gameover. #
			if setGameOverCondicion() == True:
				if event.type == KEYDOWN:
					if pushKey(event.key):
						rotations = getRotations(event.key)

						Fmatrizpre()

						for i in range(0, rotations):
							MovMatriz()

						if canMove():
							moveTiles()
							sumTiles()
							placeRandomTile()

						for j in range(0, (4 - rotations) % 4):
							MovMatriz()

						printMatrix()
			else:
				printGameOver()
			# Eventos del juego. #
			if event.type == KEYDOWN:
				
				if event.key == pygame.K_r:
					# Si se presiona el boton fisico "r"  se limpia la matriz y se vuelve al menú principal. #
					restablecer()
					main()

				if 50 < event.key and 56 > event.key:
					# Limpia la matriz. #
					Tamano = event.key - 48
					restablecer()
        
		pygame.display.update()
       
		
# Funcion que imprime la matriz en el surface creado. #
def printMatrix():
	# Se pinta el fondo negro guardado en la libreria colours. #
	SURFACE.fill(BLACK)
	# Variable global para el manejo de los puntos. #
	global TOTAL_POINTS
	# Ciclo para el manejo de la impresion mediante pygame. #
	for i in range(0, Tamano):
		for j in range(0, Tamano):
			pygame.draw.rect(SURFACE, getColour(tileMatrix[i][j]), (i*(400/Tamano), j*(400/Tamano) + 100, 400/Tamano, 400/Tamano))
			
			label = myfont.render(str(tileMatrix[i][j]), 1, (255,255,255))
			label2 = scorefont.render("Score:" + str(TOTAL_POINTS), 1, (255, 255, 255))

			SURFACE.blit(label, (i*(400/Tamano) + 30, j*(400/Tamano) + 130))
			SURFACE.blit(label2, (10, 20))
    
def printGameOver():
	#Guardado en el txt tras perder, se guarda en un txt binario para asegurar que no se editen facilmente los datos. # 
	# Se realiza una doble apertura del archivo txt esto debido a que se debe primero buscar valores ya guardados en partidas anteriores. #
	matrix = []
	# Con la libreria os se garatinza la existencia de Historial_2048.txt en la carpeta. #
	if(os.path.exists("Historial_2048.txt")):
		# Apertura del txt en modo binario. #
		archivo=open("Historial_2048.txt","rb")
		# Lectura y cargado en variable de las lineas del archivo. #
		linea=pickle.load(archivo)
		# Guardado de la matriz encontrada para en la matriz matrix para su uso. #
		matrix=linea
		# Cerrado del txt. #
		archivo.close()
	# se agrega a la matriz encontrada el valor de la partida actual. #
	matrix.append([TOTAL_POINTS])
	# se acomoda la matriz de mayor a menor. #
	matrix.sort(reverse=True)
	# Se eliminan duplicados. #
	matrix = list(lista for lista, _ in groupby(matrix))
	# Apertura del txt en modo binario. #
	archivo=open("Historial_2048.txt","wb")
	# Escritura de lo cargado en variable para las lineas del archivo. #
	pickle.dump(matrix,archivo)
	# Cerrado del txt. #
	archivo.close() 

	#Se crea la pantalla de Game Over y los textos que son: Texto de Game Over,texto del score donde se le agrega el string que lleva los puntos totales y la intsruccion para poder realizar un restart. #

	SURFACE.fill(BLACK)
	
	label = scorefont.render("Game Over!", 1, (255,255,255))
	label2 = scorefont.render("Score:" + str(TOTAL_POINTS), 1, (255,255,255))
	label3 = myfont.render("Press r to restart", 1, (255,255,255))
	label4 = myfont.render("o la tecla esc para salir", 1, (255,255,255))
	#Se colocan en la pantalla las etiquetas (textos)  creadas anteriormente para quedar lista nuestra pantalla de Game Over. #
	SURFACE.blit(label, (50, 100))
	SURFACE.blit(label2, (50, 200))
	SURFACE.blit(label3, (100, 300))
	SURFACE.blit(label4, (50, 350))

#Funion que coloca una Tile en una posicion random de la matriz. Esta funcion se utiliza nada mas iniicar el juego y cada vez que se realiz un movimiento. #
def placeRandomTile():
	count = 0

	for i in range(0, Tamano):
		for j in range(0, Tamano):
			if tileMatrix[i][j] == 0:
				count += 1

	k = Mod(random() * Tamano * Tamano)

	while tileMatrix[Mod(k / Tamano)][k % Tamano] != 0:
		k = Mod(random() * Tamano * Tamano)

	tileMatrix[Mod(k / Tamano)][k % Tamano] = 2

#Funcion que crea la matriz vacia, dependiendo del BOAR_SIZE que se seleccione asi va a ser el tamano de la matriz. #
def createEmptyMatrix():
	return [[0 for i in range(0, Tamano)] for j in range(0, Tamano)]

#Funcion que calcula el modulo de un numero, para el determinado espacion de las teclas. # 
def Mod(n):
	return int(n - (n % 1))

#Funcion que mueve las tiles del juego. #
def moveTiles():
	#Queremos trabajar columna por columna desplazando cada elemento a su vez. #
	for i in range(0, Tamano): # Trabaja a través de nuestras 4 columnas. #
		for j in range(0, Tamano - 1): # Ahora considere cambiar cada elemento marcando los 3 elementos principales si 0. #
			while tileMatrix[i][j] == 0 and sum(tileMatrix[i][j:]) > 0: # Si algún elemento es 0 y hay un número para cambiar, queremos mover los elementos de abajo. #
				for k in range(j, Tamano - 1): # Se mueven los elementos a continuación. #
					tileMatrix[i][k] = tileMatrix[i][k + 1] # Se mueven los elemento uno por uno. #
				tileMatrix[i][Tamano - 1] = 0

#Funcion que suma titles que son iguales y agrega puntos al score. #
def sumTiles():
	global TOTAL_POINTS #Varibale global que va a ser modificada. #

	for i in range(0, Tamano):
		for k in range(0, Tamano - 1):
				if tileMatrix[i][k] == tileMatrix[i][k + 1] and tileMatrix[i][k] != 0:
					tileMatrix[i][k] = tileMatrix[i][k] * 2
					tileMatrix[i][k + 1] = 0
					TOTAL_POINTS += tileMatrix[i][k]
					moveTiles() #Se mueven todas las tiles porque se realizo un movimiento. #

#Funcion que establece condicion de game over. #
def setGameOverCondicion():
	for i in range(0, Tamano ** 2):
		if tileMatrix[Mod(i / Tamano)][i % Tamano] == 0:
			return True

	for i in range(0, Tamano):
		for j in range(0, Tamano - 1):
			if tileMatrix[i][j] == tileMatrix[i][j + 1]:
				return True
			elif tileMatrix[j][i] == tileMatrix[j + 1][i]:
				return True
	return False

#Funcion que restablece la matriz y el score. #
def restablecer():
	global TOTAL_POINTS #Varibale global que va a ser modificada. #
	global tileMatrix #Varibale global que va a ser modificada. #

	TOTAL_POINTS = 0
	SURFACE.fill(BLACK)
	tileMatrix = createEmptyMatrix() #Si se realiza un restablecer presionando la tecla 'r' se estabalece una nueva matriz con tamano predeterminado 4x4. #

# Determinado de la cantidad maxima de bloques en la matriz y revision de si se puede crear otro nuevo para más movimientos. # 
def canMove():
	for i in range(0, Tamano):
		for j in range(1, Tamano):
			if tileMatrix[i][j-1] == 0 and tileMatrix[i][j] > 0:
				return True
			elif (tileMatrix[i][j-1] == tileMatrix[i][j]) and tileMatrix[i][j-1] != 0:
				return True

	return False

# Funcion principal de movimientos y ajustado de las teclas en la matriz. #
def MovMatriz():
	for i in range(0, int(Tamano/2)):
		for k in range(i, Tamano- i - 1):
			temp1 = tileMatrix[i][k]
			temp2 = tileMatrix[Tamano - 1 - k][i]
			temp3 = tileMatrix[Tamano - 1 - i][Tamano - 1 - k]
			temp4 = tileMatrix[k][Tamano - 1 - i]
			tileMatrix[Tamano - 1 - k][i] = temp1
			tileMatrix[Tamano - 1 - i][Tamano - 1 - k] = temp2
			tileMatrix[k][Tamano - 1 - i] = temp3
			tileMatrix[i][k] = temp4

#Funcion auxiliar que ayuda con la revicion de los eventos por cada vez que se preciona un tecla. #
def pushKey(k):
	return(k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)

#Funcion auxiliar que ayuda con la revicion de los eventos por cada vez que se preciona un tecla. #
def getRotations(k):
	if k == pygame.K_UP:
		return 0
	elif k == pygame.K_DOWN:
		return 2
	elif k == pygame.K_LEFT:
		return 1
	elif k == pygame.K_RIGHT:
		return 3

# Modificacion de la matriz mediante una temporal. #	
def convertToLinearMatrix():
	temp = []
	for i in range(0, Tamano ** 2):
		temp.append(tileMatrix[Mod(i / Tamano)][i % Tamano])
	temp.append(TOTAL_POINTS)

	return temp

# Llenado de la matriz para el manejo de movimientos. #
def Fmatrizpre():
	Matrizpre.append(convertToLinearMatrix())


