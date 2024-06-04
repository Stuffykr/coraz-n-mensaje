import turtle

# Configuración de la ventana
window = turtle.Screen()
window.title("Mensaje para Karla")
window.bgcolor("white")

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(3)

# Función para dibujar un corazón
def draw_heart():
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Función para escribir el texto
def write_message():
    t.up()
    t.setpos(-60, 60)
    t.down()
    t.color("white")
    t.write("Te amo Karla", font=("Arial", 24, "bold"))

# Dibujar el corazón y escribir el mensaje
draw_heart()
write_message()

# Ocultar la tortuga
t.hideturtle()

# Mantener la ventana abierta
window.mainloop()
  
