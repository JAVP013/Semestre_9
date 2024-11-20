import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 
import time 

TM = 800 # pixeles
TC = 15  # unidades


class Triangulo_Equilatero:
    def __init__(self, lado=1, tx=0, ty=0):
        ap = np.sqrt(3) * lado / 6
        h = 3 * ap
        self.vertices = np.array([
            [-lado/2 + tx, -ap + ty],
            [lado/2 + tx, -ap + ty],
            [tx, h - ap + ty]
        ], dtype=np.float32)

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


           
class Cuadrado:
    def __init__(self, lado=1):
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



class Circunferencia:
    def __init__(self, r=1,v=50):
        self.vertices =np.array([[r*np.cos(t),r*np.sin(t)] for t in np.linspace(0,np.pi,v)],dtype=np.float32)

        
    def trazar(self):
        glBegin(GL_LINE_STRIP)
        
        for x in self.vertices:
            glVertex2fv(x)
            
        glEnd()
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32)

    def rotar(self, theta):
        t = np.radians(theta)
        for i, (x, y) in enumerate(self.vertices):
            self.vertices[i] = [x * np.cos(t) - y * np.sin(t), x * np.sin(t) + y * np.cos(t)]
    def escalar(self, sx, sy):
        self.vertices *= np.array([sx, sy], dtype=np.float32)


      


class lapiz:
    def __init__(self, l=10):
       
        self.cua = Cuadrado()
        self.cua.escalar(0.1*l,0.8*l)
        
        self.tri = Triangulo_Equilatero(0.1*l)
        ap = np.sqrt(3) * 0.1*l / 6
        h = 3 * ap
        self.tri.trasladar(0,ap)
        self.tri.escalar(1,0.1*l/h)
        self.tri.trasladar(0, 0.8*l /2)


        self.cir = Circunferencia(0.1*l/2)
        self.cir.rotar(180)
        self.cir.escalar(1,2)
        self.cir.trasladar(0,-(0.8*l / 2))
    
    def trazar(self):
        self.cua.trazar()
        self.tri.trazar()
        self.cir.trazar()
    
    def rotar(self, theta):
        self.cua.rotar(theta)
        self.tri.rotar(theta)
        self.cir.rotar(theta)
    
    def trasladar(self, tx, ty):
        self.cua.trasladar(tx, ty)
        self.tri.trasladar(tx, ty)
        self.cir.trasladar(tx, ty)

class Sol:
    def __init__(self):
        self.t1=Triangulo_Equilatero()
        self.t2=Triangulo_Equilatero()
        self.t3=Triangulo_Equilatero()
        self.t4=Triangulo_Equilatero()
        self.t5=Triangulo_Equilatero()
        self.t6=Triangulo_Equilatero()
        self.t7=Triangulo_Equilatero()
        self.t8=Triangulo_Equilatero()

        self.t1.escalar(1,2)
        self.t1.rotar(-90)
        self.t1.trasladar(7,0)

        self.t2.escalar(1,2)
        self.t2.rotar(-45)
        self.t2.trasladar(7/np.sqrt(2),7/np.sqrt(2))

        self.t3.escalar(1,2)
        self.t3.rotar(0)
        self.t3.trasladar(0,7)

        self.t4.escalar(1,2)
        self.t4.rotar(45)
        self.t4.trasladar(-7/np.sqrt(2),7/np.sqrt(2))

        self.t5.escalar(1,2)
        self.t5.rotar(90)
        self.t5.trasladar(-7,0)

        self.t6.escalar(1,2)
        self.t6.rotar(135)
        self.t6.trasladar(-7/np.sqrt(2),-7/np.sqrt(2))

        self.t7.escalar(1,2)
        self.t7.rotar(180)
        self.t7.trasladar(0,-7)

        self.t8.escalar(1,2)
        self.t8.rotar(225)
        self.t8.trasladar(7/np.sqrt(2),-7/np.sqrt(2))
    def trazar(self):
        
        self.t1.trazar()
        self.t2.trazar()
        self.t3.trazar()
        self.t4.trazar()
        self.t5.trazar()
        self.t6.trazar()
        self.t7.trazar()
        self.t8.trazar()
    def escalar(self, sx, sy):
        self.t1.escalar(sx, sy)
        self.t2.escalar(sx, sy)
        self.t3.escalar(sx, sy) 
        self.t4.escalar(sx, sy)
        self.t5.escalar(sx, sy)
        self.t6.escalar(sx, sy)
        self.t7.escalar(sx, sy)
        self.t8.escalar(sx, sy)
    def rotar(self, theta):
        self.t1.rotar(theta)
        self.t2.rotar(theta)
        self.t3.rotar(theta)
        self.t4.rotar(theta)
        self.t5.rotar(theta)
        self.t6.rotar(theta)
        self.t7.rotar(theta)
        self.t8.rotar(theta)
    

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
   
    
    sol = Sol()
    
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
        
        sol.trazar()
        time.sleep(0.01)
        sol.rotar(-.5)

    


        glfw.swap_buffers(ventana)

    glfw.terminate()

if __name__ == "__main__":
    main()
