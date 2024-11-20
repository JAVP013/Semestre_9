# T1A06-20400833.py
# Nombre: Valdez Ponce Jose Alberto
# Control: 20400833

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Clase que representa una circunferencia
class Circunferencia:
    def __init__(self, radio, h=0, k=0):
        self.radio = radio  # Radio de la circunferencia
        self.h = h          # Coordenada x del centro
        self.k = k          # Coordenada y del centro

    # Método que dibuja el arco de la circunferencia entre los ángulos de inicio y fin
    def trazar(self, inicio, fin):
        x = 0
        y = self.radio
        d = 3 - 2 * self.radio

        glBegin(GL_POINTS)  # Empezamos a dibujar con puntos
        while x <= y:
            # Calculamos el ángulo en radianes y luego lo convertimos a grados
            angulo = math.atan2(y, x)
            grados = math.degrees(angulo)

            # Dibujamos los puntos solo si están dentro del rango de grados deseado
            if inicio <= grados <= fin:
                # Puntos en la parte superior de la circunferencia
                glVertex2i(round(x + self.h), round(y + self.k))
                glVertex2i(round(-x + self.h), round(y + self.k))

            # Algoritmo de Bresenham para la circunferencia
            if d < 0:
                d = d + 4 * x + 6
            else:
                d = d + 4 * (x - y) + 10
                y -= 1
            x += 1
        glEnd()

# Clase que representa el objeto geométrico solicitado
class Objeto_Geometrico:
    def __init__(self, a):
        self.a = a  # Lado del cuadrado/rombo
        self.radio = a / (2 * math.sqrt(2))  # El radio de la circunferencia se basa en el tamaño del rombo
        self.circunferencia = Circunferencia(self.radio)

    def trazar(self):
        # Trazar el arco de circunferencia superior
        self.circunferencia.trazar(0, 90)  # Dibuja el arco superior

        # Trazar el cuadrado/rombo usando solo puntos
        mitad = self.a / 2
        glBegin(GL_POINTS)
        for i in range(-int(mitad), int(mitad) + 1):
            # Coordenadas de los vértices para formar el rombo
            glVertex2i(i, int(self.radio) - abs(i))  # Lado superior
            glVertex2i(i, -int(self.radio) - self.a + abs(i))  # Lado inferior
        glEnd()

# Función principal
def main():
    # Inicializar GLFW
    if not glfw.init():
        return

    # Crear la ventana con el título de tu número de control
    ventana = glfw.create_window(501, 501, "20400833", None, None)
    if not ventana:
        glfw.terminate()
        return

    # Hacer el contexto de la ventana actual
    glfw.make_context_current(ventana)
    
    # Configurar el sistema de coordenadas (proyección ortogonal)
    gluOrtho2D(-250, 250, -250, 250)

    # Crear el objeto geométrico con a = 70
    objeto = Objeto_Geometrico(70)

    # Bucle principal de la ventana
    while not glfw.window_should_close(ventana):
        glfw.poll_events()  # Verifica los eventos de la ventana
        glClear(GL_COLOR_BUFFER_BIT)  # Limpiar la ventana

        # Dibujar ejes cartesianos en rojo
        glColor3f(1, 0, 0)
        glBegin(GL_POINTS)
        for i in range(-250, 251):
            glVertex2i(i, 0)  # Eje X
            glVertex2i(0, i)  # Eje Y
        glEnd()

        # Dibujar el objeto geométrico en verde
        glColor3f(0, 1, 0)
        objeto.trazar()

        # Intercambiar buffers (doble buffer)
        glfw.swap_buffers(ventana)

    # Finalizar GLFW
    glfw.terminate()

# Ejecutar el programa
if __name__ == "__main__":
    main()
