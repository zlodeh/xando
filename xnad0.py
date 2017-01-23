import random
board = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
b = []
def proverka():
    while True:
        cifra = input()
        try:
            if int(cifra) <= 0:
                print("Вы вели число с меньшим значением, чем надо. Повоторите пожалуйста")
                return proverka()
            elif int(cifra) >= 10:
                print("Вы вели число с больше значением, чем надо. Повоторите пожалуйста")
                return proverka()
            else:
                try:
                    b.index(int(cifra))
                    print("Данная клетка занята. Повторите пожалуйста")
                    return proverka()
                except ValueError:
                    print("Вы вели правильно")
                    b.append(int(cifra))
                    return int(cifra)
        except ValueError:
            print("Вы вели букву. Ведите число")

def playx(a):
    for i in range(9):
        board.update({a:"X"})
    return draw_board()

def playy(b):
    for i in range(9):
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
print("Добро пожаловать в игру Х и О")
draw_board()
print("Для того, чтоб ходить, вам надо вести чилос, куда вы должны поставить X или 0")
for i in range(10):
    print("Ходить первый игрок X")
    first = proverka()
    playx(first)
    print("Ходтив второй игрок 0")
    second = proverka()
    playy(second)


