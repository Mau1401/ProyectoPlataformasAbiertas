# Colores a utilizar, formato RGB #
WHITE = (255 , 255 , 255)
BLACK = (0, 0, 0)
RED = (201, 5, 5)
PINK = (255, 74, 165)
PURPLE = (155, 0, 155)
DEEP_PURPLE = (91, 0, 91)
BLUE = (0, 0, 170)
TEAL = (80, 80, 160)
L_GREEN = (94, 168, 72)
GREEN = (0, 113, 0)
ORANGE = (210, 105, 0)
DEEP_ORANGE = (248, 98, 33)
BROWN = (119, 32, 6)
# Guardado de los colores y su asignacion a los numeros#
colour_dict = { 0:BLACK, 2:RED, 4:PINK, 8:PURPLE, 16:DEEP_PURPLE, 32:BLUE, 64:TEAL, 128:L_GREEN, 256:GREEN, 512:ORANGE, 1024: DEEP_ORANGE, 2048:BROWN}
# Funcion para el envio de los colres por vector #
def getColour(i):
	return colour_dict[i]
