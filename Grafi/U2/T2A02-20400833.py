import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 600 # pixeles
TC = 10  # unidades



class figuras:
    def __init__(self):
        # Define los vértices de la figura en forma de corazón usando las coordenadas dadas
        self.vertices_figura = [
            [-2,2],#a
            [-1,2],#b
            [-1,1],#c
            [0,1],#d
            [0,0],#e
            [2,0],#f
            [2,-2],#g
            [-2,-2]#h
          
        ]

    def trazar(self):
        # Dibujar la figura completa usando GL_LINE_LOOP
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices_figura:
            glVertex2fv(vertice)
        glEnd()

    def rotar(self, theta):
        # Rotación de los vértices en torno al origen
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices_figura):
            self.vertices_figura[i] = [
                x * np.cos(t) - y * np.sin(t),
                x * np.sin(t) + y * np.cos(t)
            ]

    def trasladar(self, tx, ty):
        # Traslación de los vértices
        self.vertices_figura = [
            [x + tx, y + ty] for x, y in self.vertices_figura
        ]
        
    def vertices(self):
        return self.vertices_figura


    
    

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
   
    
    obj = figuras()
    print(obj.vertices_figura)  
    obj.trasladar(0,-1)
    print(obj.vertices_figura)   
    obj.rotar(45)
    print(obj.vertices_figura)  
    
   
   

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
