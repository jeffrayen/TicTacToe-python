import random

def show_board(board):
    print(f"=======")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"=======")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"=======")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print(f"=======")

def playersymbol():
    letter = ''#local variable 'letter' referenced before assignment
    while not (letter == 'X' or letter == 'O'):#防呆,持續讓玩家選到X或O
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return 'X', 'O'
    if letter == 'O':
        return 'O', 'X'
'''
def symbol_playersymbol():
    user_playersymbol = ''
    com_playersymbol = ''
    while True:
        user_playersymbol = input().upper()
        if user_playersymbol == 'X':
            com_playersymbol = 'O'
            user_playersymbol = 'X'
            break
        if user_playersymbol == 'O':
            com_playersymbol = 'X'
            user_playersymbol = 'O'
            break
    return user_playersymbol, com_playersymbol
'''

def whogofirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def user_move(letter, board):
    while True:#不加這個會讓checkwin()產生Nontype,因為格子被重複選取會跳出判斷式,不知道回傳什麼,加了while之後就會一直執行到符合判斷式  
        userinput = int(input('pls enter 1~9 number:'))
        if userinput >= 1 and userinput <= 9 and board[userinput-1] == ' ':#限制選在1~9的位置,空格才能讓玩家輸入-1是符合index
            board[userinput-1] = letter
            show_board(board)#顯示現在的九宮格狀態
            return board#回傳現在的九宮格狀態
            #break
        else:
            print('the position is taken')

def com_move(letter, board):
    while True:#不加這個會讓checkwin()產生Nontype,因為格子被重複選取會跳出判斷式,不知道回傳什麼,加了while之後就會一直執行到符合判斷式
        cominput = random.randint(1,9)
        print(cominput)
        if board[cominput-1] == ' ':
            board[cominput-1] = letter
            show_board(board)#顯示現在的九宮格狀態
            return board#回傳現在的九宮格狀態
            #break

def checkwin(board, playerchoice):
    return ((board[0] == playerchoice and board[1] == playerchoice and board[2] == playerchoice) or
           (board[3] == playerchoice and board[4] == playerchoice and board[5] == playerchoice) or
           (board[6] == playerchoice and board[7] == playerchoice and board[8] == playerchoice) or
           (board[0] == playerchoice and board[3] == playerchoice and board[6] == playerchoice) or
           (board[1] == playerchoice and board[4] == playerchoice and board[7] == playerchoice) or
           (board[2] == playerchoice and board[5] == playerchoice and board[8] == playerchoice) or
           (board[0] == playerchoice and board[4] == playerchoice and board[8] == playerchoice) or
           (board[2] == playerchoice and board[4] == playerchoice and board[6] == playerchoice))

def checkfullboard(board):
    for i in board:#for loop 檢查borad
        if i == ' ':
            return False
            break
        #return Ture寫在for loop內if條件不成立然後逐行執行到這就會停了
    return True#因為沒有滿足for loop內的if條件所以跳出for loop



while True:
    user_choice, com_choice = playersymbol()
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]#reset board
    show_board(board)   
    turn = whogofirst()
    Gamestart = True
    while Gamestart:
        if turn == 'computer':
            board = com_move(com_choice, board)
            if checkwin(board, com_choice) == True:
                print('you lose this game')
                Gamestart = False
            if checkfullboard(board) == True:
                print('no one won this game')
                break
            else:
                turn = 'player'
        else:
            board = user_move(user_choice, board)
            if checkwin(board, user_choice) == True:
                print('you win this game')
                Gamestart = False
            if checkfullboard(board) == True:
                print('no one won this game')
                break
            else:
                turn = 'computer'    
    
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break