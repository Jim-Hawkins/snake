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
                if i == 0 or i == rows - 1:
                    self.mapa[i].append(3)
                else:
                    if j == 0 or j == cols - 1:
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

"""Texto de ejemplo para modificar el archivo"""

c = Tablero(15, 20)
print(c)
