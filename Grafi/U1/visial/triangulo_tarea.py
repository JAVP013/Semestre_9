import glfw
import math
from OpenGL.GL import *
from OpenGL.GLU import *


class Recta:
    def __init__(self, xi, xf, yi, yf):
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf

    def trazar(self):
        dx = self.xf - self.xi
        dy = self.yf - self.yi

        if abs(dx) >= abs(dy):
            pasos = abs(dx)
        else:
            pasos = abs(dy)

        inc_x = dx/pasos
        inc_y = dy/pasos

        x = self.xi
        y = self.yi

        i = 0

        glBegin(GL_POINTS)
        while i <= pasos:
            glVertex2i(round(x), round(y))

            x += inc_x
            y += inc_y
            i += 1

        glEnd()


class Triangulo:
    def __init__(self, lado, h=0, k=0):
        altura = math.sqrt(3) * lado / 2
        apotema = math.sqrt(3) * lado / 6

        self.recta1 = Recta(-lado//2, -round(apotema),
                            lado//2, -round(apotema))
        self.recta2 = Recta(-lado//2, -round(apotema),
                            0, round(altura - apotema))
        self.recta3 = Recta(0, round(altura - apotema),
                            lado//2, -round(apotema))

    def trazar(self):
        self.recta1.trazar()
        self.recta2.trazar()
        self.recta3.trazar()


def main():
    if not glfw.init():
        return

    ventanas = glfw.create_window(501, 501, "20400734", None, None)

    if not ventanas:
        glfw.terminate()
        return

    glfw.make_context_current(ventanas)

    triangulo1 = Triangulo(100)

    # Color de la ventana, negro
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-250, 250, -250, 250)

    while not glfw.window_should_close(ventanas):
        glfw.poll_events()

        # Establecemos el color de las lineas a rojo
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 0, 0, 0)
        glBegin(GL_POINTS)

        #  Dibujamos las lineas centrales del plano cartesiano
        for i in range(-250, 250):
            glVertex2i(i, 0)

        for j in range(-250, 250):
            glVertex2i(0, j)

        glEnd()

        # Establecemos el color de la recta y la circunferencia a color gris~
        glColor(235, 120, 23, 0)
        glColor(0, 1, 0, 0)
        triangulo1.trazar()

        glfw.swap_buffers(ventanas)

    glfw.terminate()


if __name__ == "__main__":
    main()
