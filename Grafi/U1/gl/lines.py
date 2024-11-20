import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Pixeles de la ventana
TAM_VENTANA = 500
TAM_CUADRANTE = 20

class Cuadrado:
    def __init__(self, lado, h = 0, k = 0):
        self.lado = lado
        self.h = h
        self.k = k
        
    def Trazar(self):
        glBegin(GL_LINE_LOOP)
        glVertex2f(-self.lado/2 + self.h, self.lado/2 + self.k)
        glVertex2f(self.lado/2 + self.h, self.lado/2 + self.k)
        glVertex2f(self.lado/2 + self.h, -self.lado/2 + self.k)
        glVertex2f(-self.lado/2 + self.h, -self.lado/2 + self.k)
        glEnd()
    
def main():
    if not glfw.init():
        return

    ventanas = glfw.create_window(TAM_VENTANA, TAM_VENTANA, "20400734", None, None)

    if not ventanas:
        glfw.terminate()
        return

    glfw.make_context_current(ventanas)

    # Color de la ventana, negro
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-TAM_CUADRANTE, TAM_CUADRANTE, -TAM_CUADRANTE, TAM_CUADRANTE)

    obj = Cuadrado(12.5, 4,5)
    while not glfw.window_should_close(ventanas):
        glfw.poll_events()

        # Establecemos el color de las lineas a rojo
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        
        glVertex2f(-TAM_CUADRANTE,0) #V1
        glVertex2f(TAM_CUADRANTE,0) #V2
        glVertex2f(0, TAM_CUADRANTE) #V3
        glVertex2f(0, -TAM_CUADRANTE) #V4
        glEnd()
        
        glColor(1,0,0)
        obj.Trazar()

        # Establecemos el color de la recta y la circunferencia a color gris~
        glfw.swap_buffers(ventanas)

    glfw.terminate()


if __name__ == "__main__":
    main()
