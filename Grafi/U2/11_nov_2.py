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
    
    def trasladar(self, tx, ty):
        self.vertices += np.array([tx, ty], dtype=np.float32)
    
    def rotar(self, theta,xr=0,yr=0):
      t = np.radians(theta)
      i = 0
      while i<len(self.vertices):
        x,y = self.vertices[i]
        self.vertices[i][0] = xr+(x-xr)*np.cos(t) - (y-yr)*np.sin(t)
        self.vertices[i][1] = yr+(x-xr)*np.sin(t) + (y-yr)*np.cos(t) 
        i+=1
    def escalar(self, sx, sy,xf=0,yf=0):
      i = 0
      while i<len(self.vertices):
        x,y = self.vertices[i]
        self.vertices[i][0] = x*sx + xf*(1-sx)
        self.vertices[i][1] = y*sy + yf*(1-sy)
        i+=1

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


    obj2=Cruz()
    
    
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

        glColor(0, 1, 0)

        obj2.trazar()

        time.sleep(0.1)
        obj.trasladar(-0.5,-0.5)
        obj



        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
