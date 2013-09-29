width = 120
height = 120
offx = 0
offy = 0
n = 15
m = 11
number = 0
out = open("pokemon_sprites.css", "w")
sheet = "pokemon.png"
for j in range(m):
    for i in range(n):
        number += 1
        x = offx + (width+offx)*i
        y = offx + (width+offx)*j
        out.write(".pokemon-{number} {{\n"
            "width: {width}px;\n"
            "height: {height}px;\n"
            "background: url({sheet}) -{x}px -{y}px;\n"
            "}}\n\n".format(number=number, x=x, y=y, width=width, height=height, sheet=sheet))
