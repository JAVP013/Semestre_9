import glfw
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

class Cuadrado:
    def __init__(self, lado,h = 0, k = 0):
        mitad = lado//2
        self.r1 = Recta(-mitad+h,mitad+k,mitad+h,mitad+k)
        self.r2 = Recta(mitad+h,mitad+k,mitad+h,-mitad+k)
        self.r3 = Recta(mitad+h,-mitad+k,-mitad+h,-mitad+k)
        self.r4 = Recta(-mitad+h,-mitad+k,-mitad+h,mitad+k)
        
    def trazar(self):
        self.r1.trazar()
        self.r2.trazar()
        self.r3.trazar()
        self.r4.trazar()
    
class Objeto_raro:
    def __init__(self, tam, h = 0, k = 0):
        mitad = tam//2
        self.r = tam//2
        self.r4 = Recta(-mitad+h,-mitad+k,-mitad+h,mitad+k)
        self.r2 = Recta(mitad+h,mitad+k,mitad+h,-mitad+k)
    
    def trazar(self):
        self.r2.trazar()
        self.r4.trazar()
        
        x = 0
        y = self.r
        DPk = 3 - 2*self.r

        glBegin(GL_POINTS)
        while x <= y:
            glVertex2i(x , y- self.r)
            glVertex2i(-x, y- self.r)
            glVertex2i(x , -y+ self.r)
            glVertex2i(-x , -y+ self.r)

            glVertex2i(y, x- self.r)
            glVertex2i(-y, x- self.r)
            glVertex2i(y, -x+ self.r)
            glVertex2i(-y, -x+ self.r)
            
            
            if DPk >= 0:
                DPk += 4*(x-y)+10
                y -= 1
            else:
                DPk += 4*x+6
            x += 1
        glEnd()
        
class Circunferencia:
    def __init__(self, radio, h = 0, k = 0):
        self.r = radio
        self.h = h
        self.k = k

    def trazar(self):
        x = 0
        y = self.r
        DPk = 3 - 2*self.r

        glBegin(GL_POINTS)
        while x <= y:
            glVertex2i(x+ self.h , y+ self.k )
            glVertex2i(-x+ self.h , y+ self.k)
            glVertex2i(x+ self.h , -y+ self.k)
            glVertex2i(-x+ self.h , -y+ self.k)

            glVertex2i(y+ self.h , x+ self.k)
            glVertex2i(-y+ self.h , x+ self.k)
            glVertex2i(y+ self.h , -x+ self.k)
            glVertex2i(-y+ self.h , -x+ self.k)
            
            
            if DPk >= 0:
                DPk += 4*(x-y)+10
                y -= 1
            else:
                DPk += 4*x+6
            x += 1
        glEnd()


def main():
    if not glfw.init():
        return

    ventanas = glfw.create_window(501, 501, "Puntos", None, None)

    if not ventanas:
        glfw.terminate()
        return

    glfw.make_context_current(ventanas)

    # Color de la ventana, negro
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-250, 250, -250, 250)

    recta1 = Recta(-200, 124, -234, 135)
    circunferencia1 = Circunferencia(50)
    circunferencia2 = Circunferencia(27, 12, 45)
    cuadrado1 = Cuadrado(100)
    cuadrado2 = Cuadrado(100, 50,50)
    objeto_raro1 = Objeto_raro(200)

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
        #recta1.trazar()
        #circunferencia1.trazar()
        #circunferencia2.trazar()
        #cuadrado1.trazar()
        
        glColor(0,1,0,0)
        #cuadrado2.trazar()
        objeto_raro1.trazar()

        glfw.swap_buffers(ventanas)

    glfw.terminate()


if __name__ == "__main__":
    main()
