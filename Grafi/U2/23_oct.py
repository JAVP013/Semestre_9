import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 #pixeles
TC = 15 #unidades



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
   
    lado =6 
    cua = Cuadrado(lado)
    cua.rotar(45)
    cua.trasladar(lado/np.sqrt(2),lado/np.sqrt(2))


    tri = Triangulo_Equilatero(lado)
    tri.trasladar(lado/2,np.sqrt(3)*lado/6)
    tri.rotar(-45) #2
    tri.trasladar(np.sqrt(2)*lado/2,lado*np.sqrt(2)) #3



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
       
      
        cua.trazar()
        tri.trazar()
    

        glfw.swap_buffers(ventana)


    glfw.terminate()

if __name__ == "__main__":
    main()