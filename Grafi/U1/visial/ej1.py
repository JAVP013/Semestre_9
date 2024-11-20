import glfw
from OpenGL.GL import *


def main():
    if not glfw.init():
        return

    ventanas = glfw.create_window(800, 600, "Puntos", None, None)
    if not ventanas:
        glfw.terminate()
        return

    glfw.make_context_current(ventanas)

    # Color de la ventana, blanco
    glClearColor(0, 0, 0, 0)

    while not glfw.window_should_close(ventanas):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 0, 0)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2i(0, 0)
        glVertex2i(1, 1)
        glVertex2i(-1, 1)
        glVertex2i(1, -1)
        glVertex2i(-1, -1)
        glEnd()
        glfw.swap_buffers(ventanas)

    glfw.terminate()


if __name__ == "__main__":
    main()
