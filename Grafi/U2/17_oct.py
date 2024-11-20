import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 #pixeles
TC = 15 #unidades

class Circunferencia:
    def __init__(self, r,v=50):
        self.vertices =np.array([[r*np.cos(t),r*np.sin(t)] for t in np.linspace(0,2*np.pi,v)],dtype=np.float32)
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
        glEnd()

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
        i=0
        while i<len(self.vertices):
            self.vertices[i][0] += tx
            self.vertices[i][1] += ty
            i=i+1
    

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
   
    
    obj1= Triangulo_Equilatero(6)
    """ obj1.trasladar(3,np.sqrt(3)) """
    obj1.trasladar(-15,np.sqrt(3))
    

   
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
        obj1.trazar()


        time.sleep(.01)
        obj1.trasladar(.1,0)
    
        
        
        # grafica_funcion()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()