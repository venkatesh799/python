# Venkatest Thirunagiri

import random
import sys
import time
def show(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def check(c,x,y,z):
    if board[x] == c and board[y] == c and board[z] == c:
        return True
    else:
        return False
def quit():
    sys.exit()

def checkAll(c):
    if check(c,0,1,2):
        return True
    if check(c,3,4,5):
        return True
    if check(c,6,7,8):
        return True
    if check(c,0,3,6):
        return True
    if check(c,1,4,7):
        return True
    if check(c,2,5,8):
        return True
    if check(c,0,4,8):
        return True
    if check(c,6,4,2):
        return True
def isboardfull():
    if board.count(' ') >= 1:
        return False
    else:
        return True
   
def start():
    while True:
        try:
            spot=int(input("Enter Your Spot  From 0 To 9 : "))
        except:
            print("Only Numbers From 0 To 9 Allowed")
            start()
        
        spot=spot-1
        if spot < 0 and spot > 9:
            print("Invalid Spot")
            start()
        if (spot >= 0 and spot <=9) and (board[spot] != 'x' and board[spot] != 'o'):
            board[spot]='x'
            if checkAll('x') == True:
                show(board)
                print("\n")
                print("YOU - WINS")
                print("\n")
                print("Do You Want Play Again [Y/N]  : ")
                choice=input()
                choice=choice.lower()
                if choice == "y" or choice == "yes":
                    start()
                elif choice == "n" or choice == "no":
                    quit()
                break;
        else:
            print("Spot Alredy Taken")
            start()
        finding=True
        while finding:
            computer=random.randint(0,8)
            if(board[computer] != 'x' and board[computer] != 'o'):
                board[computer]='o'
                finding=False
                if checkAll('o') == True:
                    show(board)
                    print("\n")
                    print("COMPUTER  - WINS")
                    print("\n")
                    print("Do You Want Play Again [Y/N]  : ")
                    choice=input()
                    choice=choice.lower()
                    if choice == "y" or choice == "yes":
                        start()
                    elif choice == "n" or choice == "no":
                        quit()
                    break;
            else:
                if ' ' in board:
                    finding=True
                else:
                    finding=False
        if isboardfull():
            show(board)
            print("\n")
            print("Game Tie ")
            print("\n")
            print("Do You Want Play Again [Y/N]  :")
            choice=input()
            choice=choice.lower()
            if choice == "y" or choice == "yes":
                start()
            elif choice == "n" or choice == "no":
                quit()                    
            break;
    
        show(board)
def help():
    print("Soon  ")
board=[' 'for x in range(0,9)]
print("1.Satrt Game")
print("2.Quit Game")
print("3.Help")
status=int(input())
if status == 1:
    print("Loading.",end="")
    time.sleep(1)
    print("...")
    start()
elif status == 2:
    quit()
elif status == 3:
    help()
