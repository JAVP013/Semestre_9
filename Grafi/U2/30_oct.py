import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 # pixeles
TC = 15  # unidades


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

           
class Cuadrado:
    def __init__(self, lado=1):
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
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]
    def escalar(self, sx, sy):
        self.vertices *= np.array([sx, sy], dtype=np.float32)




class Circunferencia:
    def __init__(self, r=1,v=50):
        self.vertices =np.array([[r*np.cos(t),r*np.sin(t)] for t in np.linspace(0,np.pi,v)],dtype=np.float32)

        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
        glEnd()
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32)

    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]
    def escalar(self, sx, sy):
        self.vertices *= np.array([sx, sy], dtype=np.float32)
   


class lapiz:
    def __init__(self, l=10):
       
        self.cua = Cuadrado()
        self.cua.escalar(0.1*l,0.8*l)
        
        self.tri = Triangulo_Equilatero(0.1*l)
        ap = np.sqrt(3) * 0.1*l / 6
        h = 3 * ap
        self.tri.trasladar(0,ap)
        self.tri.escalar(1,0.1*l/h)
        self.tri.trasladar(0, 0.8*l /2)


        self.cir = Circunferencia(0.1*l/2)
        self.cir.rotar(180)
        self.cir.escalar(1,2)
        self.cir.trasladar(0,-(0.8*l / 2))
    
    def trazar(self):
        self.cua.trazar()
        self.tri.trazar()
        self.cir.trazar()
    
    def rotar(self, theta):
        self.cua.rotar(theta)
        self.tri.rotar(theta)
        self.cir.rotar(theta)
    
    def trasladar(self, tx, ty):
        self.cua.trasladar(tx, ty)
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
   
    
    obj = lapiz()

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
        
        obj.trazar()

        glColor(0,1,0)
        glBegin(GL_LINES)
        glVertex2f(-10,5)
        glVertex2f(10,5)
        glVertex2f(-10,4)
        glVertex2f(10,4)
        glVertex2f(-10,-4)
        glVertex2f(10,-4)
        glVertex2f(-10,-5)
        glVertex2f(10,-5)
        glEnd()
       


        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
