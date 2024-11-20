import glfw

glfw.init()
window = glfw.create_window(300, 300, "Prueba", None, None)
glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()
