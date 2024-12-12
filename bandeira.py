# Projeto bandeira da África do Sul com zoom e centralizada
import turtle

turtle.shape("classic")
turtle.setup(400, 300)

# Começar a desenhar
input("ENTER para começar a desenhar")

# Fator de zoom
zoom = 1.5

# Função para centralizar o desenho
def centralizar(x, y):
    largura = 180 * zoom  # Largura máxima da bandeira
    altura = 170 * zoom  # Altura máxima da bandeira
    centro_x = largura / 2
    centro_y = altura / 2
    return x - centro_x, y - centro_y

# Parte vermelha
turtle.color("red")
turtle.penup()
turtle.goto(centralizar(30 * zoom, 170 * zoom))
turtle.pendown()
turtle.begin_fill()

def pontos_verm():  # Função sem argumento
    pontos_verm = [
        centralizar(180 * zoom, 170 * zoom),
        centralizar(180 * zoom, 140 * zoom),
        centralizar(60 * zoom, 140 * zoom),
        centralizar(30 * zoom, 170 * zoom)
    ]
    for (x, y) in pontos_verm:
        turtle.goto(x, y)
pontos_verm()  # Chamada de função
turtle.end_fill()

# Parte azul
turtle.color("blue")
turtle.penup()
turtle.goto(centralizar(30 * zoom, 70 * zoom))
turtle.pendown()
turtle.begin_fill()

def pontos_azul():
    pontos_azul = [
        centralizar(60 * zoom, 100 * zoom),
        centralizar(180 * zoom, 100 * zoom),
        centralizar(180 * zoom, 70 * zoom),
        centralizar(30 * zoom, 70 * zoom)
    ]
    for (x, y) in pontos_azul:
        turtle.goto(x, y)
pontos_azul()
turtle.end_fill()

# Parte verde
turtle.color("green")
turtle.penup()
turtle.goto(centralizar(20 * zoom, 70 * zoom))
turtle.pendown()
turtle.begin_fill()

def pontos_verde():
    pontos_verde = [
        centralizar(60 * zoom, 110 * zoom),
        centralizar(180 * zoom, 110 * zoom),
        centralizar(180 * zoom, 130 * zoom),
        centralizar(60 * zoom, 130 * zoom),
        centralizar(20 * zoom, 170 * zoom),
        centralizar(20 * zoom, 160 * zoom),
        centralizar(60 * zoom, 120 * zoom),
        centralizar(20 * zoom, 80 * zoom),
        centralizar(20 * zoom, 70 * zoom)
    ]
    for (x, y) in pontos_verde:
        turtle.goto(x, y)
pontos_verde()
turtle.end_fill()

# Parte amarela
turtle.color("yellow")
turtle.penup()
turtle.goto(centralizar(20 * zoom, 160 * zoom))
turtle.pendown()
turtle.begin_fill()

def pontos_amar():
    pontos_amar = [
        centralizar(60 * zoom, 120 * zoom),
        centralizar(20 * zoom, 80 * zoom),
        centralizar(20 * zoom, 90 * zoom),
        centralizar(50 * zoom, 120 * zoom),
        centralizar(20 * zoom, 150 * zoom),
        centralizar(20 * zoom, 160 * zoom)
    ]
    for (x, y) in pontos_amar:
        turtle.goto(x, y)
pontos_amar()
turtle.end_fill()

# Parte preta
turtle.color("black")
turtle.penup()
turtle.goto(centralizar(20 * zoom, 90 * zoom))
turtle.pendown()
turtle.begin_fill()

def pontos_preto():
    pontos_preto = [
        centralizar(50 * zoom, 120 * zoom),
        centralizar(20 * zoom, 150 * zoom),
        centralizar(20 * zoom, 90 * zoom)
    ]
    for (x, y) in pontos_preto:
        turtle.goto(x, y)
pontos_preto()
turtle.end_fill()

# Borda
turtle.color("black")
turtle.penup()
turtle.goto(centralizar(20 * zoom, 70 * zoom))
turtle.pendown()

def borda():
    borda = [
        centralizar(180 * zoom, 70 * zoom),
        centralizar(180 * zoom, 170 * zoom),
        centralizar(20 * zoom, 170 * zoom),
        centralizar(20 * zoom, 70 * zoom)
    ]
    for (x, y) in borda:
        turtle.goto(x, y)
borda()

turtle.done()
