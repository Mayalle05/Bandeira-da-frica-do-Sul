# Projeto bandeira da Africa do Sul
import turtle

turtle.shape("classic")
turtle.setup(800,600)


# Parte vermelha
turtle.color("red")
turtle.penup()
turtle.goto(30,170)
turtle.pendown()
turtle.begin_fill()

def pontos_verm(): # Função sem argumento
    pontos_verm = [
        (180,170),
        (180,140),
        (60,140),
        (30,170)

    ]
    for (x,y) in pontos_verm:
        turtle.goto(x,y)
pontos_verm() # Chamada de função
turtle.end_fill()

# end for
 # end def 

# Parte azul
turtle.color("blue")
turtle.penup()
turtle.goto(30,70)
turtle.pendown()
turtle.begin_fill()

def pontos_azul():
    pontos_azul = [
        (60,100),
        (180,100),
        (180,70),
        (30,70)
        
    ]
    for (x,y) in pontos_azul:
        turtle.goto(x,y)
pontos_azul()
turtle.end_fill()

# end for
 # end def 

# Parte verde
turtle.color("green")
turtle.penup()
turtle.goto(20,70)
turtle.pendown()
turtle.begin_fill()

def pontos_verde():
    pontos_verde = [
        (60,110),
        (180,110),
        (180,130),
        (60,130),
        (20,170),
        (20,160),
        (60,120),
        (20,80),
        (20,70)
        
    ]
    for (x,y) in pontos_verde:
        turtle.goto(x,y)
pontos_verde()
turtle.end_fill()

# end for
 # end def 

# Parte amarela
turtle.color("yellow")
turtle.penup()
turtle.goto(20,160)
turtle.pendown()
turtle.begin_fill()

def pontos_amar():
    pontos_amar = [
        (60,120),
        (20,80),
        (20,90),
        (50,120),
        (20,150),
        (20,160)
        
    ]
    for (x,y) in pontos_amar:
        turtle.goto(x,y)
pontos_amar()
turtle.end_fill()

# end for
 # end def 

# Parte preta
turtle.color("black")
turtle.penup()
turtle.goto(20,90)
turtle.pendown()
turtle.begin_fill()

def pontos_preto():
    pontos_preto = [
        (50,120),
        (20,150),
        (20,90)
        
    ]
    for (x,y) in pontos_preto:
        turtle.goto(x,y)
pontos_preto()
turtle.end_fill()

# end for
 # end def 

# Borda
turtle.color("black")
turtle.penup()
turtle.goto(20,70)
turtle.pendown()

def borda():
    borda = [
        (180,70),
        (180,170),
        (20,170),
        (20,70)
         
    ]
    for (x,y) in borda:
        turtle.goto(x,y)
borda()


turtle.done()
