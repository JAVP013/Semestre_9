#Nombre
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

tam_ventana = 500 #pixels
tam_cuadrante = 20 #unidades

class Cuadrado:
    def __init__(self,lado):
        self.l = lado
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        glVertex2f(-self.l/2,self.l/2)
        glVertex2f(self.l/2,self.l/2)
        glVertex2f(self.l/2,-self.l/2)
        glVertex2f(-self.l/2,-self.l/2)
        glEnd()

def main():
    if not glfw.init():
        return

    ventana = glfw.create_window(tam_ventana,tam_ventana,"91400481",None,None)
    if not ventana:
        glfw.terminate()
        return

    glfw.make_context_current(ventana)
    glClearColor(0,0,0,0)#RGB
    gluOrtho2D(-tam_cuadrante,tam_cuadrante,-tam_cuadrante,tam_cuadrante)

    obj = Cuadrado(7.8)

    while not glfw.window_should_close(ventana):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
        #Ejes
        glColor(1,1,1)#RGB
        glBegin(GL_LINES)
        glVertex2f(-tam_cuadrante,0)
        glVertex2f(tam_cuadrante,0)
        glVertex2f(0,-tam_cuadrante)
        glVertex2f(0,tam_cuadrante)
        glEnd()

        glColor(1,0,0)
        obj.trazar()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
    
