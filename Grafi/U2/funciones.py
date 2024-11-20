import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

TM = 800 #pixeles
TC = 15 #unidades

class Grafica:
    def __init__(self, f):
        self.vertices = [[x,f(x)] for x in np.linspace(-TC,TC,50*TC//2)]
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
        glEnd()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(TM,TM,"20400734",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    glClearColor(0,0,0,0)#RGB
    gluOrtho2D(-TC,TC,-TC,TC)
   
    f1 = Grafica(lambda x: x*np.sin(x))
    f2 = Grafica(lambda x: x**2-2*x-3)
    f3 = Grafica(lambda x: 3*x + np.cos(x) - np.exp(x))
   
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
        f1.trazar()
        glColor(0,1,0)
        f2.trazar()
        glColor(0,0,1)
        f3.trazar()
        

        # grafica_funcion()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()