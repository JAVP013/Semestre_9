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
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32)


class Circunferencia_de_circunferencia():
    def __init__(self, R,r,n):
        self.circunferencia=[Circunferencia(r) for i in range(n)]
        print(len(self.circunferencia))
        i =0
        for theta in np.arange(0,2*np.pi,2*np.pi/n):
            self.circunferencia[i].trasladar(R*np.cos(theta),R*np.sin(theta))
            i+=1
    def trazar(self):
        for circunferencia in self.circunferencia:
            circunferencia.trazar()
    def temp(self,tx,ty):
        
        tx,ty =0,0
        for circunferencia in self.circunferencia:
            circunferencia.trasladar(tx,ty)

    

           


    
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
    
    obj1= Circunferencia_de_circunferencia(12,.5,100)
    

   
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
        
       
        
        
      
        # grafica_funcion()

        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()