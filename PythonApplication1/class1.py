import math
class class1:
    """description of class"""


def Yravnenie(a, b, c):
    error = ''
    answer = []
    if a == 0:
	    if b == 0:
		    if c == 0:
			    error = 'R'
			    answer = []
		    else:
			    error = 'Нет корней'
			    answer = []
	    else:
		    answer = [ -c / b ]
    else:
	    discr = b ** 2 - 4 * a * c
	    if discr > 0:
		    answer = [ (-b + math.sqrt(discr)) / (2 * a), (-b - math.sqrt(discr)) / (2 * a) ]
	    elif discr == 0:
		    answer = [ -b / (2 * a) ]
	    else:
		    error = 'Нет корней'
		    answer = []
    return error, answer
