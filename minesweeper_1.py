from random import randint
from tkinter import *
from time import sleep

rows = []
cols = []
A = []
field = Tk()
buttons = []
label = Label(field, text="Just try", font="Times 20")

def bomb_gen():
    x=randint(0,9)
    y=randint(0,9)
    if A[x][y] == "X":
        bomb_gen()
    else:
        A[x][y] = "X"

def over():
    label.config(text="U so ded")
    for x in range(10):
        for y in range(10):
            if A[x][y] == "X":
                buttons[x][y].grid_forget()
                c = Label(field,height="2",width="4",bg="red",text=str(A[x][y]))
                c.grid(row=x,column=y)

def flag(x,y,effects=None):
    buttons[x][y].config(bg='red')
    print('should be red tho')

def press(x,y):
    if buttons[x][y] == 0:
        pass
    else:        
        if A[x][y] == 'X':
            over()
        elif A[x][y] == 0:
            buttons[x][y].grid_forget()
            buttons[x][y] = 0
            c = Label(field,height="2",width="4",text=' ')
            c.grid(row=x,column=y)
            
            if x == 0:
                if y == 0:
                    for a in range(2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x+a,y+b)
                elif y == 9:
                    for a in range(2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x+a,y-b)
                else:
                    for a in range(2):
                        for b in range(3):
                            if a == 0 and b == 1:
                                pass
                            else:
                                press(x+a,y+b-1)
            elif x == 9:
                if y == 0:
                    for a in range(2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x-a,y+b)
                elif y == 9:
                    for a in range(2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x-a,y-b)
                else:
                    for a in range(2):
                        for b in range(3):
                            if a == 0 and b == 1:
                                pass
                            else:
                                press(x-a,y+b-1)
            else:
                if y == 0:
                    for a in range(-1,2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x+a,y+b)
                elif y == 9:
                    for a in range(-1,2):
                        for b in range(2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x+a,y-b)
                else:    
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if a == 0 and b == 0:
                                pass
                            else:
                                press(x+a,y+b)
        else:
            buttons[x][y].grid_forget()
            c = Label(field,height="2",width="4",text=str(A[x][y]))
            c.grid(row=x,column=y)

for i in range(10):
    rows.append(i)
    cols.append(i)
    A.append([])
    for j in range(10):
        A[i].append(0)

for i in range(10):
    bomb_gen()

for x in range(10):
    for y in range(10):
        if A[x][y] == "X":
            pass
        elif x == 0:
            if y == 0:
                for a in range(2):
                    for b in range(2):
                        if A[x+a][y+b] == 'X':
                            A[x][y] += 1
            elif y == 9:
                for a in range(2):
                    for b in range(2):
                        if A[x+a][y-b] == 'X':
                            A[x][y] += 1
            else:
                for a in range(2):
                    for b in range(3):
                        if A[x+a][y+b-1] == 'X':
                            A[x][y] += 1
        elif x == 9:
            if y == 0:
                for a in range(2):
                    for b in range(2):
                        if A[x-a][y+b] == 'X':
                            A[x][y] += 1
            elif y == 9:
                for a in range(2):
                    for b in range(2):
                        if A[x-a][y-b] == 'X':
                            A[x][y] += 1
            else:
                for a in range(2):
                    for b in range(3):
                        if A[x-a][y+b-1] == 'X':
                            A[x][y] += 1
        else:
            if y == 0:
                for a in range(-1,2):
                    for b in range(2):
                        if A[x+a][y+b] == 'X':
                            A[x][y] += 1
            elif y == 9:
                for a in range(-1,2):
                    for b in range(2):
                        if A[x+a][y-b] == 'X':
                            A[x][y] += 1
            else:    
                for a in range(-1,2):
                    for b in range(-1,2):
                        if A[x+a][y+b] == 'X':
                            A[x][y] += 1

for xpos in range(10):
    print(A[xpos])
    button_row = []
    for ypos in range(10):
        tile = Button(field,height="2",width="4", command = lambda x=xpos, y=ypos: press(x,y))
        tile.bind('<Button-3>',print('hi'))
        button_row.append(tile)
        tile.grid(row=xpos,column=ypos)
    buttons.append(button_row)
label = Label(field, text="Just try", font="Times 20")
label.grid(row=10, column=0, columnspan=10)
print('fuk')

for x in range(10):
    for y in range(10):
        buttons[x][y].bind('<Button-3>',print('hi'))
print('fuk')
field.mainloop()
