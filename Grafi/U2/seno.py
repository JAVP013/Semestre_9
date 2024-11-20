import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

TAM_VENTANA = 800 #pixeles
TAM_CUADRANTE = 15 #unidades

class Grafica:
    def __init__(self, funcion):
        self.f = funcion
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in np.linspace(-TAM_CUADRANTE,TAM_CUADRANTE,50*TAM_CUADRANTE//2):
            glVertex2f(x,self.f(x))
            
        glEnd()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(TAM_VENTANA,TAM_VENTANA,"20400734",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    
    glClearColor(0,0,0,0)#RGB
    gluOrtho2D(-TAM_CUADRANTE,TAM_CUADRANTE,-TAM_CUADRANTE,TAM_CUADRANTE)
   
    f1 = Grafica(lambda x: np.sin(x))
    f2 = Grafica(lambda x: 3*x+np.cos(x)-np.exp(x))
    f3 = Grafica(lambda x: x*np.sin(x))
   
    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
    
        #ejes
        glColor(1,1,1)#RGB  
        glBegin(GL_LINES)
        glVertex2f(-TAM_CUADRANTE,0)
        glVertex2f(TAM_CUADRANTE,0)
        glVertex2f(0,-TAM_CUADRANTE)
        glVertex2f(0,TAM_CUADRANTE)
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