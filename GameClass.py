import random
from enum import Enum


class GameCellType(Enum):
    BOMB = 0
    EMPTY = 1


class GameCellTypeView(Enum):
    UNKNOWN = 0
    BOMB = 1
    EMPTY = 2
    PREDICT_BOMB = 3


class GameCell:
    def __init__(self):
        self.value = GameCellType.EMPTY
        self.countOfBombsNear = 0

    def is_it_bomb(self):
        return not self.value == GameCellType.EMPTY

    def __str__(self):
        return f'value: {self.value}, count: {self.countOfBombsNear}'


class GameCellView:
    def __init__(self, mother_cell: GameCell):
        self.motherCell = mother_cell
        self.value = GameCellTypeView.UNKNOWN
        self.countOfBombsNear = -1

    def open(self):
        if self.motherCell.is_it_bomb():
            self.value = GameCellTypeView.BOMB
        else:
            self.value = GameCellTypeView.EMPTY
            self.countOfBombsNear = self.motherCell.countOfBombsNear

    def predict_bomb(self):
        if self.value == GameCellTypeView.UNKNOWN:
            self.value = GameCellTypeView.PREDICT_BOMB
        elif self.value == GameCellTypeView.PREDICT_BOMB:
            self.value = GameCellTypeView.UNKNOWN


class Game:
    def __init__(self, size, bombs_count):
        self.size = size
        self.bombCount = bombs_count
        self.playingField = []
        self.playingFieldView = []

        for i in range(self.size):
            self.playingField.append([])
            for j in range(self.size):
                self.playingField[i].append(GameCell())

        for i in range(self.bombCount):
            while True:
                rand_width = random.randint(0, self.size-1)
                rand_height = random.randint(0, self.size-1)
                if not self.playingField[rand_height][rand_width].is_it_bomb():
                    self.playingField[rand_height][rand_width].value = GameCellType.BOMB
                    break

        for i in range(self.size):
            for j in range(self.size):
                if self.playingField[i][j].value != GameCellType.BOMB:
                    self.playingField[i][j].countOfBombsNear = self.how_many_bombs_are_there(i, j)

        for i in range(self.size):
            self.playingFieldView.append([])
            for j in range(self.size):
                self.playingFieldView[i].append(GameCellView(self.playingField[i][j]))

    def how_many_bombs_are_there(self, i, j):
        count = 0
        for k in self.neighbours(i, j):
            if self.playingField[k[0]][k[1]].is_it_bomb():
                count += 1
        return count

    def neighbours(self, i, j):
        result = []
        if i > 0 and j > 0:
            result.append([i - 1, j - 1])
        if i > 0:
            result.append([i - 1, j])
        if i > 0 and j < self.size - 1:
            result.append([i - 1, j + 1])

        if j > 0:
            result.append([i, j - 1])
        if j < self.size - 1:
            result.append([i, j + 1])

        if i < self.size - 1 and j > 0:
            result.append([i + 1, j - 1])
        if i < self.size - 1:
            result.append([i + 1, j])
        if i < self.size - 1 and j < self.size - 1:
            result.append([i + 1, j + 1])

        return result

    def open_cell(self, i, j):
        if self.playingFieldView[i][j].value == GameCellTypeView.UNKNOWN:
            self.playingFieldView[i][j].open()
            if self.playingFieldView[i][j].value == GameCellTypeView.BOMB:
                return
            else:
                if self.playingFieldView[i][j].countOfBombsNear == 0:
                    self.easy_cells(i, j)

    def check_cell(self, i, j):
        if self.playingFieldView[i][j].value == GameCellTypeView.UNKNOWN or \
           self.playingFieldView[i][j].value == GameCellTypeView.PREDICT_BOMB:
            self.playingFieldView[i][j].open()
            if self.playingFieldView[i][j].countOfBombsNear == 0:
                self.easy_cells(i, j)

    def easy_cells(self, i, j):
        for k in self.neighbours(i, j):
            self.check_cell(k[0], k[1])

    def check_answer(self):
        count = 0
        count_real_predict = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.playingFieldView[i][j].value == GameCellTypeView.BOMB:
                    return 'Lose'
                else:
                    if self.playingFieldView[i][j].value == GameCellTypeView.EMPTY:
                        count += 1

                if self.playingFieldView[i][j].value == GameCellTypeView.PREDICT_BOMB:
                    if self.playingFieldView[i][j].motherCell.is_it_bomb():
                        count_real_predict += 1

        if count == self.size**2 - self.bombCount or count_real_predict == self.bombCount:
            return 'Win'
        else:
            return 'In Game'

    def show_all_bomb(self):
        for i in self.playingFieldView:
            for j in i:
                if j.motherCell.is_it_bomb():
                    j.open()
