import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 600 # pixeles
TC = 10  # unidades

class Cruz:
    def __init__(self):
        self.vertices = np.array([[0.5,1.5],
                                  [0.5,0.5],
                                  [1.5,0.5],
                                  [1.5,-0.5],
                                  [0.5,-0.5],
                                  [0.5,-2.5],
                                  [-0.5,-2.5],
                                  [-0.5,-0.5],
                                  [-1.5,-0.5],
                                  [-1.5,0.5],
                                  [-0.5,0.5],
                                  [-0.5,1.5]],dtype=np.float32)
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    def transformar(self,M):
        i = 0
        while i<len(self.vertices):
            P = np.matrix([[self.vertices[i][0]],
                          [self.vertices[i][1]],
                          [1]],dtype=np.float32)
            Pp = np.dot(M,P)
            self.vertices[i][0] = Pp[0]
            self.vertices[i][1] = Pp[1]
            i+=1
    def trasladar(self,tx,ty):
        T = np.array([[1,0,tx],
                      [0,1,ty],
                      [0,0,1]],dtype=np.float32)
        self.transformar(T)
    def escalar(self,sx,sy):
        S = np.array([[sx,0,0],
                      [0,sy,0],
                      [0,0,1]],dtype=np.float32)
        self.transformar(S)
    def rotar(self,theta):
        t = np.radians(theta)
        R = np.array([[np.cos(t),-np.sin(t),0],
                      [np.sin(t),np.cos(t),0],
                      [0,0,1]],dtype=np.float32)
        self.transformar(R)


      


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
   
    obj=Cruz()
    obj.transformar(np.array([[2,0,4],
                              [0,2,4],
                              [0,0,1]],dtype=np.float32))
    
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

       
        
        
        



        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
