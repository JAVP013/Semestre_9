import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np  # Asegúrate de importar numpy

tam_ventana = 800  # pixels
tam_cuadrante = 15  # unidades

""" def grafica_funcion():
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-tam_cuadrante, tam_cuadrante, 50*tam_cuadrante//2):
        glVertex2f(x, x*np.cos(x))
    glEnd() """

class Grafica():
    def __init__(self,function):
       self.f = function
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        for x in np.linspace(-tam_cuadrante, tam_cuadrante, 50*tam_cuadrante//2):
            glVertex2f(x, self.f(x))
        glEnd()
    

def main():
    
    
    if not glfw.init():
        return

    ventana = glfw.create_window(tam_ventana, tam_ventana, "91400481", None, None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    glClearColor(0, 0, 0, 0)  # RGB
    gluOrtho2D(-tam_cuadrante, tam_cuadrante, -tam_cuadrante, tam_cuadrante)

 
    f1 = Grafica(lambda x: x**2-2*x-3)
    f2 = Grafica(lambda x: x*np.sin(x))
    f3 = Grafica(lambda x: 3*x + np.cos(x) + np.exp(x))

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        # Ejes
        glColor(1, 1, 1)  # RGB
        glBegin(GL_LINES)
        glVertex2f(-tam_cuadrante, 0)
        glVertex2f(tam_cuadrante, 0)
        glVertex2f(0, -tam_cuadrante)
        glVertex2f(0, tam_cuadrante)
        glEnd()

        glColor(1, 0, 0)  # Color del cuadrado
        f1.trazar()
        glColor(0, 1, 0)  # Color del cuadrado
        f2.trazar()
        glColor(1, 1, 0)  # Color del cuadrado
        f3.trazar()
        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
