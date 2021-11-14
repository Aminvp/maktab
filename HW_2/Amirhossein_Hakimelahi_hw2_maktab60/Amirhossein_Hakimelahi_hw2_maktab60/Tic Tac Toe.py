import random


class Board:
    def __init__(self):
        self.cells = [' '] * 10

    def fill(self, le, position):
        self.cells[position] = le

    def isFull(self):
        # the cell with index '0' is always free
        if self.cells.count(' ') > 1:
            return False
        return True

    def isWinner(self, le):
        # check all of the possibilities to check if 'le' wins or not
        return ((self.cells[7] == le and self.cells[8] == le and self.cells[9] == le) or
                (self.cells[4] == le and self.cells[5] == le and self.cells[6] == le) or
                (self.cells[1] == le and self.cells[2] == le and self.cells[3] == le) or
                (self.cells[7] == le and self.cells[4] == le and self.cells[1] == le) or
                (self.cells[8] == le and self.cells[5] == le and self.cells[2] == le) or
                (self.cells[9] == le and self.cells[6] == le and self.cells[3] == le) or
                (self.cells[7] == le and self.cells[5] == le and self.cells[3] == le) or
                (self.cells[9] == le and self.cells[5] == le and self.cells[1] == le))

    def show(self):
        print('   |   |')
        print(' ' + self.cells[1] + ' | ' + self.cells[2] + ' | ' + self.cells[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.cells[4] + ' | ' + self.cells[5] + ' | ' + self.cells[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.cells[7] + ' | ' + self.cells[8] + ' | ' + self.cells[9])
        print('   |   |')

    def cellIsFree(self, position):
        return self.cells[position] == ' '


class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def move(self):
        while True:
            move = int(input('Please insert a number between 1 and 9 : '))
            # check if that cell is free
            if not self.board.cellIsFree(move):
                print('The cell number %i is occupied' % move)
            else:
                break

        self.board.fill('X', move)

    def isWinner(self):
        return self.board.isWinner('X')


class Computer:
    def __init__(self, board, level):
        self.level = level
        self.board = board

    def move(self):
        # check what cells are free
        freeCells = [i for i in range(len(self.board.cells)) if self.board.cells[i] == ' ']
        # the first cell with index '0' is always free and we do not need it
        freeCells.remove(0)
        # check if filling any of free cells could cause to win computer or the player
        if self.level == 2:
            for le in ['O', 'X']:
                for i in freeCells:
                    self.board.fill(le, i)
                    if self.board.isWinner('O'):
                        return
                    if self.board.isWinner('X'):
                        self.board.cells[i] = 'O'
                        return
                    self.board.cells[i] = ' '
        # choosing a random free cell in case of level '1' or not existing a winning position for computer or the player
        choice = random.choice(freeCells)
        self.board.cells[choice] = 'O'

    def isWinner(self):
        return self.board.isWinner('O')


bo = Board()
p = Player(input('Please enter your name : '), bo)
comp = Computer(bo, int(input('please enter the level of the game (1 or 2) :  ')))
bo.show()
while not bo.isFull():
    if not comp.isWinner():
        p.move()
    else:
        print('Computer Won')
        break
    if not (p.isWinner()):
        if bo.isFull():
            bo.show()
            print('Draw!!')
            break
        comp.move()
        bo.show()
    else:
        bo.show()
        print('%s Won' % p.name)
        break
