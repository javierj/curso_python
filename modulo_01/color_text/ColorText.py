#!/usr/bin/env python

text = "Hola Ana y bienvenida. \n Me encanta tu presentacion colorista, la verdad es que ya hacia falta algo mas de color en este foro Menos mal que ya te tenemos, ademas amarillo y morado siempre han sido mis colores faboritos, buena eleccion !!!.\n No te preocupes por aprender juegos, es facil... Todos los juegos traen instrucciones. \n Un saludo."
colors = ["[color=black]", "[color=red]", "[color=yellow]", "[color=pink]", "[color=green]", "[color=orange]", "[color=purple]", "[color=blue]", "[color=beige]", "[color=brown]", "[color=teal]", "[color=navy]", "[color=marron]", "[color=limegreen]"]
end = "[/color]"

index = 0
output = ""
close = False

for char in text:
    if char != " " and char != "\n":
        output += colors[index]
        close = True
        index+=1
        if index == len(colors):
            index = 0
    output += char
    if close:
        close = False
        output += end
    
print(output)

