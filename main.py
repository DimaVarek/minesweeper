import tkinter as tk
from GameHandler import Game

size = 10
bombs = 10
game = Game(size, bombs)


def left_click(i, j):
    game.open_cell(i, j)
    show_all()
    status = game.check_answer()
    statusLabelText['text'] = f'{status}'
    if status == 'Lose' or status == 'Win':
        show_all_bomb()

def show_all_bomb():
    for i in range(size):
        for j in range(size):
            but_arr[i][j]['state'] = "disable"
            if game.playingField[i][j].value == 'Bomb':
                but_arr[i][j]['text'] = f"{game.playingField[i][j].value}"
                but_arr[i][j]['background'] = 'red'


def restart():
    global game
    game = Game(size, bombs)
    statusLabelText['text'] = f'{game.check_answer()}'
    for i in range(size):
        for j in range(size):
            but_arr[i][j]['state'] = "normal"
            but_arr[i][j]['background'] = 'grey'
            but_arr[i][j]['text'] = ''


def right_click(event1 = None, i = 0, j = 0):
    if not game.playingField[i][j].isOpen:
        if but_arr[i][j]['text'] != "Bomb!":
            but_arr[i][j]['text'] = f"Bomb!"
        else:
            but_arr[i][j]['text'] = f""


def show_all():
    for i in range(size):
        for j in range(size):
            but_arr[i][j]['state'] = "normal"
            if game.playingField[i][j].isOpen:
                if game.playingField[i][j].value != 'Bomb':
                    but_arr[i][j]['background'] = 'white'
                    if game.playingField[i][j].countOfBombsNear != 0:
                        but_arr[i][j]['text'] = f"{game.playingField[i][j].countOfBombsNear}"

                else:
                    but_arr[i][j]['text'] = f"{game.playingField[i][j].value}"
                    but_arr[i][j]['background'] = 'red'


MainWindow = tk.Tk()
MainWindow.title('Minesweeper')
MainWindow.geometry(f'{size*50}x{size*50 + 80}')

but_arr = []

for i in range(game.size):
    but_arr.append([])
    for j in range(game.size):
        but_arr[i].append(tk.Button(text='', background='grey', command=(lambda row=i, col=j: left_click(row, col))))
        but_arr[i][j].bind('<Button-3>', lambda event, row=i, col=j: right_click(event1=event,i=row,j=col))
        but_arr[i][j].place(x=i*50, y=j*50 + 80, width=50, height=50)

statusLabel = tk.Label(text='Status: ')
statusLabelText = tk.Label(text=f'{game.check_answer()}')
statusLabel.place(x=10, y=10, width=50)
statusLabelText.place(x=70, y=10, width=50)

restartButton = tk.Button(text='Restart', command=restart)
restartButton.place(x=130, y=10, width=80)


MainWindow.mainloop()
