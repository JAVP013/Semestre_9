import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

TM = 600  # Tamaño de la ventana en píxeles
TC = 10   # Tamaño del sistema de coordenadas en unidades

class Figura:
    def __init__(self):
        # Define los vértices de la figura en forma de corazón
        self.vertices_figura = [
            [-2, 2],  # a
            [-1, 2],  # b
            [-1, 1],  # c
            [0, 1],   # d (el punto que queremos en el origen)
            [0, 0],   # e
            [2, 0],   # f
            [2, -2],  # g
            [-2, -2]  # h
        ]

    def trazar(self):
        # Dibujar la figura completa usando GL_LINE_LOOP
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices_figura:
            glVertex2fv(vertice)
        glEnd()

    def transformar(self, M):
        # Aplica una transformación homogénea a los vértices
        for i in range(len(self.vertices_figura)):
            P = np.array([[self.vertices_figura[i][0]],
                          [self.vertices_figura[i][1]],
                          [1]], dtype=np.float32)
            Pp = np.dot(M, P)
            self.vertices_figura[i][0] = Pp[0, 0]
            self.vertices_figura[i][1] = Pp[1, 0]

    def trasladar(self, tx, ty):
        # Genera y aplica una matriz de traslación
        T = np.array([[1, 0, tx],
                      [0, 1, ty],
                      [0, 0, 1]], dtype=np.float32)
        self.transformar(T)

    def rotar(self, theta):
        # Genera y aplica una matriz de rotación
        t = np.radians(theta)
        R = np.array([[np.cos(t), -np.sin(t), 0],
                      [np.sin(t), np.cos(t), 0],
                      [0, 0, 1]], dtype=np.float32)
        self.transformar(R)

    def escalado(self, sx, sy):
        # Genera y aplica una matriz de escalado
        S = np.array([[sx, 0, 0],
                      [0, sy, 0],
                      [0, 0, 1]], dtype=np.float32)
        self.transformar(S)

    def vertices(self):
        # Devuelve los vértices actuales
        return self.vertices_figura

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(TM, TM, "Transformaciones con matrices", None, None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-TC, TC, -TC, TC)

    # Crear la figura
    obj = Figura()

        # Matriz de traslación T1: mover los puntos en (0, -1)
    T1 = np.array([[1, 0, 0],
                    [0, 1, -1],
                    [0, 0, 1]], dtype=np.float32)
        
        # Ángulo de rotación en grados y conversión a radianes
    theta = 45
    t = np.radians(theta)
        
        # Matriz de rotación R de 45 grados
    R = np.array([[np.cos(t), -np.sin(t), 0],
                    [np.sin(t), np.cos(t), 0],
                    [0, 0, 1]], dtype=np.float32)
        
        # Composición de las transformaciones
    M = np.dot(R, T1)
    # Paso 3: Aplicar la transformación
    obj.transformar(M)

    # Imprimir los vértices transformados
    print("Vértices transformados:")
    for vertice in obj.vertices():
        print(vertice)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar los ejes
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        glVertex2f(-TC, 0)
        glVertex2f(TC, 0)
        glVertex2f(0, -TC)
        glVertex2f(0, TC)
        glEnd()

        # Dibujar la figura transformada
        glColor(1, 0, 0)
        obj.trazar()

        glfw.swap_buffers(ventana)

    glfw.terminate()


if __name__ == "__main__":
    main()
