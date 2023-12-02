import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    passos = max(abs(dx), abs(dy)) # maior distancia entre os iniciais

    xIncrement = dx / passos 
    yIncrement = dy / passos

    x = x1
    y = y1

    # Lista para armazenar os pontos da linha
    points = []

    for i in range(passos + 1):
        points.append((round(x), round(y)))
        x += xIncrement
        y += yIncrement

    return points

def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    incrXonly = 2 * dy
    incrBoth = 2 * (dy - dx)
    d = 2 * dy - dx
    x = x0
    y = y0

    points = []
    coord = (x, y)
    points.append(coord)

    while x < x1:
        x += 1
        if d <= 0:
            d += incrXonly  # Corrigido para 'incrXonly'
        else:
            d += incrBoth
            y += 1
        coord = (x, y)
        points.append(coord)

    return points


def get_coordenadas():
    x1 = simpledialog.askinteger("Coordenadas", "Digite a coordenada x1:")
    y1 = simpledialog.askinteger("Coordenadas", "Digite a coordenada y1:")
    x2 = simpledialog.askinteger("Coordenadas", "Digite a coordenada x2:")
    y2 = simpledialog.askinteger("Coordenadas", "Digite a coordenada y2:")
    return x1, y1, x2, y2

def get_which():
    method = simpledialog.askstring("Método", "Escolha o método (0 para DDA, 1 para Bresenham):")
    return method

def main():
    root = tk.Tk()
    root.withdraw()

    x1, y1, x2, y2 = get_coordenadas()

    method = get_which()

    if method == '0':
        points = dda(x1, y1, x2, y2)
    elif method == '1':
        points = bresenham(x1, y1, x2, y2)
    else:
        print("Método inválido. Escolha '0' para DDA ou '1' para Bresenham.")
        return

    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title('Linha Desenhada')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
