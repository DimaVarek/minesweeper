import tkinter as tk
from GameHandler import Game

size = 10
bombs = 10
game = Game(size, bombs)


def show_content(i, j):
    if game.playingField[i][j].value == 'Bomb':
        but_arr[i][j]['text'] = f"{game.playingField[i][j].value}"
    else:
        but_arr[i][j]['text'] = f"{game.playingField[i][j].countOfBombsNear}"


MainWindow = tk.Tk()
MainWindow.title('Сапер')
MainWindow.geometry(f'{size*50}x{size*50}')

but_arr = []
for c in range(game.size):
    MainWindow.columnconfigure(index=c, weight=1)
for r in range(game.size):
    MainWindow.rowconfigure(index=r, weight=1)

for i in range(game.size):
    but_arr.append([])
    for j in range(game.size):
        but_arr[i].append(tk.Button(text = '      ', command=(lambda row=i, col=j: show_content(row, col))))
        but_arr[i][j].place(x=i*50, y=j*50, width=50, height=50)

MainWindow.mainloop()
