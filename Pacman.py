import Busquedas_pacman
import turtle

wn = turtle.Screen()
wn.title("Pacman")
wn.bgcolor("black")
wn.setup(width = 700, height = 700)

class Laber(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Pacman(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)


class Objeto(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)

class Camino(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)

ambiente = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X   XX         X  X     X",
"X   XX         X  X     X",
"X              X  X     X",
"X        XXXX  X  XXXXX X",
"X        X        X     X",
"XXXXXXXXXX        X     X",
"X        X    P   X     X",
"X        X  XXXX  XX XXXX",
"X        X  X        X  X",
"X   XXXXXX  X        X  X",
"X                    X  X",
"X                       X",
"X            XX  XX     X",
"X            XX  XX     X",
"X            X    X   X X",
"X            X    X   X X",
"XXXXXXXXXXXXXX    XXXXX X",
"X   X                   X",
"X   X          X        X",
"XT           XXX        X",
"XXXXX        XXXXXX     X",
"X   X        XXX     XX X",
"X       XX     X     XX X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):
            letra = nivel[fila][columna]
            n_x = -288 + (columna * 24)
            n_y = 288 - (fila * 24)

            if letra == "X":
                laber.goto(n_x,n_y)
                laber.stamp()
                paredes.append((n_x,n_y))

            if letra == "P":
                pacman.goto(n_x,n_y)

            if letra == "T":
                obj.goto(n_x,n_y)

laber = Laber()
pacman = Pacman()
obj = Objeto()
cam = Camino()

paredes = []

iniciar_lab(ambiente)

estadoInicial = (48,120)
goalTest = (-264,-192)

#solucion = Busquedas_pacman.BEST_FIRST_SEARCH(estadoInicial,goalTest, paredes)

#solucion = Busquedas_pacman.DEPTH_FIRST_SEARCH(estadoInicial,goalTest, paredes)

solucion = Busquedas_pacman.GREEDY_BEST_FIRST_SEARCH(estadoInicial,goalTest, paredes)

for sol in solucion:
    if (sol[0],sol[1]) != estadoInicial:
        cam.goto(sol[0], sol[1])
        cam.stamp()

wn.tracer(0)

while True:
    wn.update()


turtle.done()

