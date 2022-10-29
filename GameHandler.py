import random


class Game:
    def __init__(self, size, bombs_count):
        self.size = size
        self.bombCount = bombs_count
        self.playingField = []

        for i in range(self.size):
            self.playingField.append([])
            for j in range(self.size):
                self.playingField[i].append(GameCell())

        for i in range(self.bombCount):
            while True:
                rand_width = random.randint(0, self.size-1)
                rand_height = random.randint(0, self.size-1)
                if not self.playingField[rand_height][rand_width].is_it_bomb():
                    self.playingField[rand_height][rand_width].value = 'Bomb'
                    break

        for i in range(self.size):
            for j in range(self.size):
                if self.playingField[i][j].value != 'Bomb':
                    self.playingField[i][j].countOfBombsNear = self.how_many_bombs_are_there(i, j)


    def how_many_bombs_are_there(self, i, j):
        count = 0
        if i > 0 and j > 0:
            count += self.playingField[i - 1][j - 1].is_it_bomb()
        if i > 0:
            count += self.playingField[i - 1][j].is_it_bomb()
        if i > 0 and j < self.size - 1:
            count += self.playingField[i - 1][j + 1].is_it_bomb()

        if j > 0:
            count += self.playingField[i][j - 1].is_it_bomb()
        if j < self.size - 1:
            count += self.playingField[i][j + 1].is_it_bomb()

        if i < self.size - 1 and j > 0:
            count += self.playingField[i + 1][j - 1].is_it_bomb()
        if i < self.size - 1:
            count += self.playingField[i + 1][j].is_it_bomb()
        if i < self.size - 1 and j < self.size - 1:
            count += self.playingField[i + 1][j + 1].is_it_bomb()

        return count


class GameCell:
    def __init__(self):
        self.value = 'Empty'
        self.countOfBombsNear = 0
        self.isOpen = False

    def is_it_bomb(self):
        if self.value == 'Empty':
            return False
        else:
            return True


    def __str__(self):
        return f'value: {self.value}, count: {self.countOfBombsNear}'
