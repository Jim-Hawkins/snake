class Tablero:
    def __init__(sel
                        self.mapa[i].append(3)
                    else:
                        self.mapa[i].append(0)

    def __str__(self):
        res = ''
        for i in range(self.rows):
            for j in range(self.cols):
                res += str(self.mapa[i][j])
            res += '\n'

        return res


x = input("Introduce el número de filas del tablero ")
y = input("Introduce el número de columnas del tablero ")
c = Tablero(x, y)


for i in range(2):
    print(c)

print("Hola mundo")

jgvjbviebmoebi
bmebke`wbm
bme`wbéw
be