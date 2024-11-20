import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 #pixeles
TC = 15 #unidades



class Rectangulo:
    def __init__(self, base,altura):
        # Definir los vértices como una lista de listas o tuplas
        self.vertices = np.array([
            [-base/2, altura/2],
            [base/2, altura/2],
            [base/2, -altura/2],
            [-base/2, -altura/2]
        ],dtype=np.float32)
    
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)  # Se pasa cada vértice
        glEnd()   
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32)   
    def rotar(self,theta):
        t = np.radians(theta)
        i = 0
        while i<len(self.vertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x*np.cos(t) - y*np.sin(t)
            self.vertices[i][1] = x*np.sin(t) + y*np.cos(t)
            i+=1


class Triangulo_Equilatero:
    def __init__(self, lado,tx=0,ty=0):
        # Definir los vértices como una lista de listas o tuplas
        ap = np.sqrt(3)*lado/6
        h = 3*ap
        self.vertices = np.array([
            [-lado/2+tx, -ap+ty],
            [lado/2+tx, -ap+ty],
            [0+tx, h-ap+ty]
        ],dtype=np.float32)

    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)  # Se pasa cada vértice
        glEnd()
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32) 
    def rotar(self,theta):
        t = np.radians(theta)
        i = 0
        while i<len(self.vertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x*np.cos(t) - y*np.sin(t)
            self.vertices[i][1] = x*np.sin(t) + y*np.cos(t)
            i+=1
class Med_elipse:
    def __init__(self, r_x, r_y, v=100):
        # r_x es el radio a lo largo del eje x y r_y a lo largo del eje y
        self.vertices = np.array([[x, np.sqrt(r_y**2 - (r_y/r_x)**2 * x**2)] for x in np.linspace(-r_x, r_x, v)], dtype=np.float32)
    
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
        glEnd()

    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        i = 0
        while i < len(self.vertices):
            x, y = self.vertices[i]
            self.vertices[i][0] = x * np.cos(t) - y * np.sin(t)
            self.vertices[i][1] = x * np.sin(t) + y * np.cos(t)
            i += 1


class modelo:
    def __init__(self,base,altura):
        ap = np.sqrt(3)*base/6
        self.rec = Rectangulo(base,altura)
        self.tri = Triangulo_Equilatero(base)
        self.cir = Med_elipse(base/2,np.sqrt(altura)/3)
        self.tri.trasladar(0,altura/2+ap)
        self.cir.rotar(180)
        self.cir.trasladar(0,-(altura/2))
    def trazar(self):
        self.rec.trazar()
        self.tri.trazar()
        self.cir.trazar()
    def rotar(self,theta):
        self.rec.rotar(theta)
        self.tri.rotar(theta)
        self.cir.rotar(theta)
    def trasladar(self,tx,ty):
        self.rec.trasladar(tx,ty)
        self.tri.trasladar(tx,ty)
        self.cir.trasladar(tx,ty)
    
def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(TM,TM,"20400833",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    glClearColor(0,0,0,0)#RGB
    gluOrtho2D(-TC,TC,-TC,TC)
   
    mod1 = modelo(2,19)
   


    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
    
        #ejes
        glColor(1,1,1)#RGB  
        glBegin(GL_LINES)
        glVertex2f(-TC,0)
        glVertex2f(TC,0)
        glVertex2f(0,-TC)
        glVertex2f(0,TC)
        glEnd()
        
        glColor(1,0,0)
       
        mod1.trazar()
       
     
       
       

        glfw.swap_buffers(ventana)


    glfw.terminate()

if __name__ == "__main__":
    main()