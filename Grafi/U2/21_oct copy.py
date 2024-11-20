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
   
    ob1 = Cuadrado(5)
   
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
       
      
        ob1.trazar()
        ob1.rotar(1)
        # grafica_funcion()

        glfw.swap_buffers(ventana)


    glfw.terminate()

if __name__ == "__main__":
    main()