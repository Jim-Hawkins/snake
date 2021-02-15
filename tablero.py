class Tablero:
    def __init__(self, rows, cols):
        self.mapa = []
        if rows >= 4:
            self.rows = rows
        else:
            self.rows = 4
        if cols >= 4:
            self.cols = cols
        else:
            self.cols = 4

        for i in range(rows):
            self.mapa.append([])
            for j in range(cols):
                if i in (0, rows - 1):
                    self.mapa[i].append(3)
                else:
                    if j in (0, cols - 1):
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