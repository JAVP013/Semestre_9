import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 # pixeles
TC = 15  # unidades

class Rectangulo:
    def __init__(self, base, altura):
        self.vertices = np.array([
            [-base/2, altura/2],
            [base/2, altura/2],
            [base/2, -altura/2],
            [-base/2, -altura/2]
        ], dtype=np.float32)
    
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]

class Triangulo_Equilatero:
    def __init__(self, lado, tx=0, ty=0):
        ap = np.sqrt(3) * lado / 6
        h = 3 * ap
        self.vertices = np.array([
            [-lado/2 + tx, -ap + ty],
            [lado/2 + tx, -ap + ty],
            [tx, h - ap + ty]
        ], dtype=np.float32)

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]
    def escalar(self, sx, sy):
            self.vertices *= np.array([sx, sy], dtype=np.float32)

           

class Parabola:
    def __init__(self, ancho, v=50):
        self.vertices = np.array([[x, x**2 - ancho * x] for x in np.linspace(0, ancho, v)], dtype=np.float32)
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        for x in self.vertices:
            glVertex2fv(x)
        glEnd()
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]

class Modelo:
    def __init__(self, base, altura):
        ap = np.sqrt(3) * base / 6
        self.rec = Rectangulo(base, altura)
        self.tri = Triangulo_Equilatero(base)
        self.tri.trasladar(0, altura / 2 + ap)
        self.cir = Parabola(base)
        self.cir.trasladar(0, -(altura / 2))
        self.cir.trasladar(-base / 2, 0)
    
    def trazar(self):
        self.rec.trazar()
        self.tri.trazar()
        self.cir.trazar()
    
    def rotar(self, theta):
        self.rec.rotar(theta)
        self.tri.rotar(theta)
        self.cir.rotar(theta)
    
    def trasladar(self, tx, ty):
        self.rec.trasladar(tx, ty)
        self.tri.trasladar(tx, ty)
        self.cir.trasladar(tx, ty)

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(TM, TM, "20400833", None, None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-TC, TC, -TC, TC)
   
    
    tri_eq = Triangulo_Equilatero(4)
   

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        glVertex2f(-TC, 0)
        glVertex2f(TC, 0)
        glVertex2f(0, -TC)
        glVertex2f(0, TC)
        glEnd()
        
        glColor(1, 0, 0)
        
        tri_eq.trazar()

        time.sleep(0.1)


        
    
        tri_eq.trasladar(.1, .1)
        
        tri_eq.escalar(0.95, 0.95)

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
