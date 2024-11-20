import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    if not glfw.init():
        return

    ventanas = glfw.create_window(601, 601, "Puntos", None, None)
    if not ventanas:
        glfw.terminate()
        return

    glfw.make_context_current(ventanas)

    # Color de la ventana, blanco
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-300, 300, -300, 300)

    while not glfw.window_should_close(ventanas):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 0, 0)
        glBegin(GL_POINTS)

        for i in range(-300, 300):
            glVertex2i(i, 0)

        for j in range(-300, 300):
            glVertex2i(0, j)

        glEnd()

        glColor(0, 200, 159)
        glBegin(GL_POINTS)

        for k in range(-300, 300):
            glVertex2i(k, k)
        glEnd()
        glfw.swap_buffers(ventanas)

    glfw.terminate()


if __name__ == "__main__":
    main()
