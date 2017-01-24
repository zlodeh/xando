import random
board = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
next_move = []
def proverka():
    while True:
        cifra = input()
        try:
            cifra = int(cifra)
            if cifra <= 0:
                print("Вы вели число с меньшим значением, чем надо. Повоторите пожалуйста")
                return proverka()
            elif cifra >= 10:
                print("Вы вели число с больше значением, чем надо. Повоторите пожалуйста")
                return proverka()
            else:
                try:
                    next_move.index(cifra)
                    print("Данная клетка занята. Повторите пожалуйста")
                    return proverka()
                except ValueError:
                    print("Вы вели правильно")
                    next_move.append(cifra)
                    return cifra
        except ValueError:
            print("Вы вели букву. Ведите число")

def playx(a):
    board.update({a:"X"})
    return draw_board()

def playy(b):
    board.update({b:"0"})
    return draw_board()

def draw_board():
    print("-------------")
    print("|", board[1] , "|", board[2] , "|", board[3] , "|")
    print("-------------")
    print("|", board[4] , "|", board[5] , "|", board[6] , "|")
    print("-------------")
    print("|", board[7] , "|", board[8] , "|", board[9] , "|")
    print("-------------")
    if board[1] == board[2] == board[3]:
        print("Вы виграли ")
        raise SystemExit
    elif board[4] == board[5] == board[6]:
        print("Вы виграли ")
        raise SystemExit
    elif board[7] == board[8] == board[9]:
        print("Вы виграли ")
        raise SystemExit
    elif board[1] == board[4] == board[7]:
        print("Вы виграли ")
        raise SystemExit
    elif board[2] == board[5] == board[8]:
        print("Вы виграли ")
        raise SystemExit
    elif board[3] == board[6] == board[9]:
        print("Вы виграли ")
        raise SystemExit
    elif board[1] == board[5] == board[9]:
        print("Вы виграли ")
        raise SystemExit
    elif board[7] == board[5] == board[3]:
        print("Вы виграли ")
        raise SystemExit
    elif len(next_move) == 9:
        print("Ничья")
        raise SystemExit
print("Добро пожаловать в игру Х и О")
draw_board()
print("Для того, чтоб ходить, вам надо вести чилос, куда вы должны поставить X или 0")
while range(5):
        print("Ходить первый игрок X")
        first = proverka()
        playx(first)
        print("Ходтив второй игрок 0")
        second = proverka()
        playy(second)


