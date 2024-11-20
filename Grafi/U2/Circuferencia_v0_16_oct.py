import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

TM = 800 #pixeles
TC = 15 #unidades

class Circunferenciav0:
    def __init__(self, r,v=100):
        self.vertices =np.array([[x,np.sqrt(r**2-x**2)] for x in np.linspace(-r,r,v)],dtype=np.float32)
        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
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
   
    f1 = Circunferenciav0(5)
    f1.rotar(180)
   
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
        
        
        # grafica_funcion()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()