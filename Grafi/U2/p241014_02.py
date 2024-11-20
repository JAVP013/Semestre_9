import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np  # Asegúrate de importar numpy

tam_ventana = 500  # pixels
tam_cuadrante = 20  # unidades

class Cuadrado:
    def __init__(self, lado):
        # Definir los vértices como una lista de listas o tuplas
        self.vertices = np.array([
            [-lado/2, lado/2],
            [lado/2, lado/2],
            [lado/2, -lado/2],
            [-lado/2, -lado/2]
        ],dtype=np.float32)
    
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)  # Se pasa cada vértice
        glEnd()
class Triangulo_Equilatero:
    def __init__(self, lado):
        # Definir los vértices como una lista de listas o tuplas
        ap = np.sqrt(3)*lado/6
        h = 3*ap
        self.vertices = np.array([
            [-lado/2, ap],
            [lado/2, ap],
            [0, -h]
        ],dtype=np.float32)

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)  # Se pasa cada vértice
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

    obj = Cuadrado(20)
    obj2 = Triangulo_Equilatero(10)

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
        obj.trazar()
        glColor(0, 1, 0)  # Color del triángulo
        obj2.trazar()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
