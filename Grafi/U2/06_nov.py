import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 600 # pixeles
TC = 10  # unidades

class Cruz:
    def __init__(self):
        self.vertices = np.array([
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
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]
    def escalar(self, sx, sy):
            self.vertices *= np.array([sx, sy], dtype=np.float32)
    def vertices(self):
        return self.vertices
    def reflexion_y(self):
        self.vertices *= np.array([-1, 1], dtype=np.float32)
    def reflexion_xy(self):
        self.vertices *= np.array([-1, -1], dtype=np.float32)


      


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
    obj.reflexion_xy()
    
    
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
