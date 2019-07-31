from tkinter import *
from tkinter import messagebox
import csv
import sys
import random


def wincheck():
    global bx
    if bx[0] == bx[1] == bx[2] == "O" or bx[3] == bx[4] == bx[5] == "O" or bx[6] == bx[7] == bx[8] == "O":
        #messagebox._show("Game end", "Player : O wins")
        sys.exit()
    elif bx[0] == bx[1] == bx[2] == "X" or bx[3] == bx[4] == bx[5] == "X" or bx[6] == bx[7] == bx[8] == "X":
        dbchange("X")
        #messagebox._show("Game end", "Player : X wins")
        sys.exit()
    elif bx[0] == bx[3] == bx[6] == "O" or bx[1] == bx[4] == bx[7] == "O" or bx[2] == bx[5] == bx[8] == "O":
        dbchange("O")
        #messagebox._show("Game end", "Player : O wins")
        sys.exit()
    elif bx[0] == bx[3] == bx[6] == "X" or bx[1] == bx[4] == bx[7] == "X" or bx[2] == bx[5] == bx[8] == "X":
        dbchange("X")
        #messagebox._show("Game end", "Player : X wins")
        sys.exit()
    elif bx[0] == bx[4] == bx[8] == "O" or bx[2] == bx[4] == bx[6] == "O":
        dbchange("O")
        #messagebox._show("Game end", "Player : O wins")
        sys.exit()
    elif bx[0] == bx[4] == bx[8] == "X" or bx[2] == bx[4] == bx[6] == "X":
        dbchange("X")
        #messagebox._show("Game end", "Player : X wins")
        sys.exit()
    if "0" not in bx and "" not in bx:
        #messagebox._show(" Game end ", "Draw")
        sys.exit()


def ai():
    global aidb
    global aidb_cnt
    global b
    global cnt
    global var5  # position
    global var3  # weight
    global player
    var2 = [0] * 10
    global bx
    global db
    c = ""
    ar = c.join(bx)
    a = 0
    b = 0
    while a < 19683:
        if ar == db[a][0]:
            b = a
            aidb[aidb_cnt][0] = int(b)
            break
        a = a + 1
    ar1 = db[b]
    arr3 = ar1.copy()[1:]
    arr4 = []
    for val in arr3:
        arr4.append(int(val[9:]))
    var1 = arr4.index(max(arr4))
    var2 = ar1[var1 + 1]
    var2 = var2.replace('\n', '')
    var3 = var2[9:]
    var2 = var2[:9]
    aidb[aidb_cnt][1] = int(var1 + 1)
    aidb_cnt = aidb_cnt + 1
    for var4 in range(0, 9):
        if var2[var4] == "1":
            var5 = var4
            break
    if player == 2:
        if var5 == 0:
            button1.config(text="X")
            player = 1
            bx[0] = "X"
        elif var5 == 1:
            button2.config(text="X")
            player = 1
            bx[1] = "X"
        elif var5 == 2:
            button3.config(text="X")
            player = 1
            bx[2] = "X"
        elif var5 == 3:
            button4.config(text="X")
            player = 1
            bx[3] = "X"
        elif var5 == 4:
            button5.config(text="X")
            player = 1
            bx[4] = "X"
        elif var5 == 5:
            button6.config(text="X")
            player = 1
            bx[5] = "X"
        elif var5 == 6:
            button7.config(text="X")
            player = 1
            bx[6] = "X"
        elif var5 == 7:
            button8.config(text="X")
            player = 1
            bx[7] = "X"
        elif var5 == 8:
            button9.config(text="X")
            player = 1
            bx[8] = "X"
    cnt = cnt + 1
    wincheck()
    # train change
    #activate(1)


def dbchange(str1):
    global aidb_cnt
    global aidb
    global b
    global db
    global var3
    if str1 == "X":
        for x in range(0, aidb_cnt - 1):
            db[aidb[x][0]][aidb[x][1]] = db[aidb[x][0]][aidb[x][1]].replace("\n", "")[:9] + str(
                int(db[aidb[x][0]][aidb[x][1]].replace("\n", "")[9:]) + 1)
    elif str1 == "O":
        for x in range(0, aidb_cnt):
            db[aidb[x][0]][aidb[x][1]] = db[aidb[x][0]][aidb[x][1]].replace("\n", "")[:9] + str(int(db[aidb[x][0]][aidb[x][1]].replace("\n", "")[9:]) - 1)

    with open('db', 'w') as f:
        file = csv.writer(f, lineterminator='\n')
        file.writerows(db)


def activate(box):
    global cnt
    global player
    global bx
    # train change
    #while 1:
    #    box = random.choice([1,2,3,4,5,6,7,8,9])
    #    if box not in bx:
     #       break
    # .....................
    cnt = cnt + 1
    if player == 1:
        if box == 1:
            button1.config(text="O")
            player = 2
            bx[0] = "O"
        elif box == 2:
            button2.config(text="O")
            player = 2
            bx[1] = "O"
        elif box == 3:
            button3.config(text="O")
            player = 2
            bx[2] = "O"

        elif box == 4:
            button4.config(text="O")
            player = 2
            bx[3] = "O"

        elif box == 5:
            button5.config(text="O")
            player = 2
            bx[4] = "O"

        elif box == 6:
            button6.config(text="O")
            player = 2
            bx[5] = "O"

        elif box == 7:
            button7.config(text="O")
            player = 2
            bx[6] = "O"

        elif box == 8:
            button8.config(text="O")
            player = 2
            bx[7] = "O"

        elif box == 9:
            button9.config(text="O")
            player = 2
            bx[8] = "O"
    wincheck()
    ai()


b = 0
aidb = [[0 for x in range(2)] for y in range(10)]
aidb_cnt = 0
var5 = 9
var3 = 9
db = list(csv.reader(open("db", "r")))
bx = ["0"] * 9
cnt = 0
root = Tk()
root.geometry('290x258')

button1 = Button(root, text="  ", command=lambda: activate(1))
button1.grid(row='0', column='0', ipadx='40', ipady='30')

button2 = Button(root, text="  ", command=lambda: activate(2))
button2.grid(row='0', column='1', ipadx='40', ipady='30')

button3 = Button(root, text="  ", command=lambda: activate(3))
button3.grid(row='0', column='2', ipadx='40', ipady='30')

button4 = Button(root, text="  ", command=lambda: activate(4))
button4.grid(row='1', column='0', ipadx='40', ipady='30')

button5 = Button(root, text="  ", command=lambda: activate(5))
button5.grid(row='1', column='1', ipadx='40', ipady='30')

button6 = Button(root, text="  ", command=lambda: activate(6))
button6.grid(row='1', column='2', ipadx='40', ipady='30')

button7 = Button(root, text="  ", command=lambda: activate(7))
button7.grid(row='2', column='0', ipadx='40', ipady='30')

button8 = Button(root, text="  ", command=lambda: activate(8))
button8.grid(row='2', column='1', ipadx='40', ipady='30')

button9 = Button(root, text="  ", command=lambda: activate(9))
button9.grid(row='2', column='2', ipadx='40', ipady='30')

player = 1  # player1 = O, player2 = X
# train change
#activate(1)

root.mainloop()
