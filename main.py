import tkinter as tk
from GameClass import Game, GameCellTypeView


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
    global game
    game.show_all_bomb()
    show_all()
    disable_all_button()


def disable_all_button():
    for i in range(size):
        for j in range(size):
            but_arr[i][j]['state'] = "disable"


def restart():
    global game
    game = Game(size, bombs)
    statusLabelText['text'] = f'{game.check_answer()}'
    show_all()


def right_click(event1 = None, i = 0, j = 0):
    game.playingFieldView[i][j].predect_bomb()
    show_all()
    status = game.check_answer()
    statusLabelText['text'] = f'{status}'
    if status == 'Lose' or status == 'Win':
        show_all_bomb()


def show_all():
    for i in range(size):
        for j in range(size):
            but_arr[i][j]['state'] = "normal"
            if game.playingFieldView[i][j].value == GameCellTypeView.UNKNOWN:
                but_arr[i][j]['background'] = 'grey'
                but_arr[i][j]['text'] = ''
            elif game.playingFieldView[i][j].value == GameCellTypeView.PREDICT_BOMB:
                but_arr[i][j]['background'] = 'grey'
                but_arr[i][j]['text'] = 'Bomb!'
            elif game.playingFieldView[i][j].value == GameCellTypeView.EMPTY:
                but_arr[i][j]['background'] = 'white'
                if game.playingFieldView[i][j].countOfBombsNear == 0:
                    but_arr[i][j]['text'] = f''
                else:
                    but_arr[i][j]['text'] = f'{game.playingFieldView[i][j].countOfBombsNear}'
            elif game.playingFieldView[i][j].value == GameCellTypeView.BOMB:
                but_arr[i][j]['background'] = 'red'
                but_arr[i][j]['text'] = "Bomb!"


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
#https://ru.stackoverflow.com/questions/1300913/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B2%D1%8B%D0%B2%D0%B5%D1%81%D1%82%D0%B8-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B5%D0%B5-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%B2-%D0%BE%D0%BA%D0%BD%D0%B5-tkinter