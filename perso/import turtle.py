import turtle
import random

# Initialisation de l'écran
screen = turtle.Screen()
screen.bgcolor("midnightblue")

# Création de la tortue
pen = turtle.Turtle()
pen.speed(10)

# Fonction pour dessiner un cercle plein
def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Fonction pour dessiner un demi-cercle (pour la lune)
def draw_half_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(radius, 180)
    pen.end_fill()

# Fonction pour dessiner la lune
def draw_moon():
    draw_circle(200, 150, 50, "white")   # Cercle plein pour la lune
    draw_circle(220, 150, 40, "midnightblue")  # Cercle pour créer l'ombre

# Fonction pour dessiner des montagnes avec perspective et dégradé de couleurs
def draw_mountain(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

# Fonction pour dessiner des collines
def draw_hill(x, y, radius):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("forestgreen")
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(radius, 180)
    pen.end_fill()

# Fonction pour dessiner un arbre avec des branches plus détaillées
def draw_tree(x, y, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Tronc
    pen.color("saddlebrown")
    pen.begin_fill()
    pen.setheading(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(height)
    pen.end_fill()

    # Branches (formes triangulaires)
    pen.color("darkgreen")
    top = y + height
    branch_size = 60
    for i in range(3):
        pen.penup()
        pen.goto(x - branch_size // 2 + 10, top - i * 20)
        pen.pendown()
        pen.begin_fill()
        for _ in range(3):
            pen.forward(branch_size)
            pen.left(120)
        pen.end_fill()
        branch_size -= 20

# Fonction pour dessiner une rivière avec des reflets
def draw_river():
    pen.penup()
    pen.goto(-300, -200)
    pen.setheading(-60)
    pen.color("deepskyblue")
    pen.pendown()
    pen.begin_fill()
    pen.forward(700)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(700)
    pen.left(120)
    pen.forward(100)
    pen.end_fill()

# Fonction pour dessiner un village avec des petites maisons
def draw_house(x, y):
    # Dessiner le corps de la maison
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("lightyellow")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    # Dessiner le toit
    pen.penup()
    pen.goto(x, y + 50)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(50)
        pen.left(120)
    pen.end_fill()

# Fonction pour dessiner des étoiles dispersées
def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Fonction principale pour dessiner le paysage
def draw_complex_landscape():
    # Ciel étoilé avec la lune
    draw_moon()
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(100, 300)
        draw_star(x, y, random.randint(10, 20))

    # Montagnes avec perspective (différentes teintes)
    draw_mountain(-400, -100, 400, 300, "dimgray")
    draw_mountain(-100, -100, 500, 300, "gray")
    draw_mountain(200, -100, 300, 250, "lightgray")

    # Collines vertes
    draw_hill(-200, -100, 200)
    draw_hill(100, -100, 150)

    # Rivière avec des reflets
    draw_river()

    # Arbres détaillés
    draw_tree(-250, -180, 100)
    draw_tree(150, -170, 80)

    # Petit village avec des maisons
    for i in range(3):
        draw_house(-100 + i * 70, -220)

# Lancer le dessin du paysage très complexe
draw_complex_landscape()

# Attendre que l'utilisateur ferme la fenêtre
turtle.done()
