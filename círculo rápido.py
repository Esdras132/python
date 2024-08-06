from turtle import *

bgcolor("black")
speed(0)
hideturtle()

i = 0

while True:
    color("red")
    circle(i)

    right(10)  # Aumentando o ângulo de rotação
    forward(10)  # Aumentando a distância percorrida
    i += 5  # Aumentando o tamanho do círculo
    if i >= 100:  # Redefinindo o tamanho do círculo após atingir um certo limite
        i = 0
        clear()  # Limpa a tela para evitar que a tartaruga saia do controle

done()