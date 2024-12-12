# Projeto bandeira da África do Sul com zoom
import turtle

turtle.shape("classic")
turtle.setup(800, 600)

# Fator de zoom
zoom = 1.5

# Parte vermelha
turtle.color("red")
turtle.penup()
turtle.goto(30 * zoom, 170 * zoom)
turtle.pendown()
turtle.begin_fill()

def pontos_verm():  # Função sem argumento
    pontos_verm = [
        (180 * zoom, 170 * zoom),
        (180 * zoom, 140 * zoom),
        (60 * zoom, 140 * zoom),
        (30 * zoom, 170 * zoom)
    ]
    for (x, y) in pontos_verm:
        turtle.goto(x, y)
pontos_verm()  # Chamada de função
turtle.end_fill()

# Parte azul
turtle.color("blue")
turtle.penup()
turtle.goto(30 * zoom, 70 * zoom)
turtle.pendown()
turtle.begin_fill()

def pontos_azul():
    pontos_azul = [
        (60 * zoom, 100 * zoom),
        (180 * zoom, 100 * zoom),
        (180 * zoom, 70 * zoom),
        (30 * zoom, 70 * zoom)
    ]
    for (x, y) in pontos_azul:
        turtle.goto(x, y)
pontos_azul()
turtle.end_fill()

# Parte verde
turtle.color("green")
turtle.penup()
turtle.goto(20 * zoom, 70 * zoom)
turtle.pendown()
turtle.begin_fill()

def pontos_verde():
    pontos_verde = [
        (60 * zoom, 110 * zoom),
        (180 * zoom, 110 * zoom),
        (180 * zoom, 130 * zoom),
        (60 * zoom, 130 * zoom),
        (20 * zoom, 170 * zoom),
        (20 * zoom, 160 * zoom),
        (60 * zoom, 120 * zoom),
        (20 * zoom, 80 * zoom),
        (20 * zoom, 70 * zoom)
    ]
    for (x, y) in pontos_verde:
        turtle.goto(x, y)
pontos_verde()
turtle.end_fill()

# Parte amarela
turtle.color("yellow")
turtle.penup()
turtle.goto(20 * zoom, 160 * zoom)
turtle.pendown()
turtle.begin_fill()

def pontos_amar():
    pontos_amar = [
        (60 * zoom, 120 * zoom),
        (20 * zoom, 80 * zoom),
        (20 * zoom, 90 * zoom),
        (50 * zoom, 120 * zoom),
        (20 * zoom, 150 * zoom),
        (20 * zoom, 160 * zoom)
    ]
    for (x, y) in pontos_amar:
        turtle.goto(x, y)
pontos_amar()
turtle.end_fill()

# Parte preta
turtle.color("black")
turtle.penup()
turtle.goto(20 * zoom, 90 * zoom)
turtle.pendown()
turtle.begin_fill()

def pontos_preto():
    pontos_preto = [
        (50 * zoom, 120 * zoom),
        (20 * zoom, 150 * zoom),
        (20 * zoom, 90 * zoom)
    ]
    for (x, y) in pontos_preto:
        turtle.goto(x, y)
pontos_preto()
turtle.end_fill()

# Borda
turtle.color("black")
turtle.penup()
turtle.goto(20 * zoom, 70 * zoom)
turtle.pendown()

def borda():
    borda = [
        (180 * zoom, 70 * zoom),
        (180 * zoom, 170 * zoom),
        (20 * zoom, 170 * zoom),
        (20 * zoom, 70 * zoom)
    ]
    for (x, y) in borda:
        turtle.goto(x, y)
borda()

turtle.done()
