import os
import sys
from tkinter import *
import tkinter.font as font


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tk()
root.resizable(False, False)
root.title('Tic Tac Toe')
root["bg"] = "#ddd8ca"
root.iconbitmap(resource_path("ttt.ico"))

mylabel1 = Label(root)
mylabel2 = Label(root)

x_o, xo, list_x_o, count = '', ['X', 'O'], [0], 0


def mylabel_0(text, color):
    global mylabel2
    mylabel2 = Label(root, text=text, font=buttonfont, bg=color, padx=10, pady=5, borderwidth=5, relief="groove")
    mylabel2.grid(row=1, column=0, columnspan=3, pady=10)


def mylabel_1(text):
    global mylabel1
    mylabel1 = Label(root, text=text, font=buttonfont, bg='#361d26', fg='#f6f3ee', padx=20, pady=5, borderwidth=5,
                     relief="groove")
    mylabel1.grid(row=6, column=0, columnspan=3)


def mylabel_2():
    global mylabel2
    mylabel2 = Label(root, text="Click 'Tic Tac Toe' to RESTART", font=buttonfont, bg='#361d26', fg='#f6f3ee',
                     padx=10, pady=5, borderwidth=5, relief="groove")
    mylabel2.grid(row=1, column=0, columnspan=3, pady=10)


def mylabel_3(text1, text2):
    global mylabel2
    mylabel2 = Label(root, text=text1, font=buttonfont, bg=text2, padx=10, pady=5, borderwidth=5, relief="groove")
    mylabel2.grid(row=1, column=0, pady=10, columnspan=3)


def player_x():
    global x_o
    if button_x:
        x_o = 'X'


def player_o():
    global x_o
    if button_o:
        x_o = 'O'


def choice():
    button_x['state'] = DISABLED
    button_o['state'] = DISABLED
    mylabel1.destroy(), mylabel2.destroy()
    if x_o == 'X':
        mylabel_0('Player 1 choice is '+x_o, '#7df9ff')
    if x_o == 'O':
        mylabel_0('Player 1 choice is '+x_o, '#ccff00')


def change_text(m):
    global count, buttons
    buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    odd = [1, 3, 5, 7, 9]
    if x_o not in xo:
        mylabel1.destroy(), mylabel_1('ERROR: Must Choose X or O!')
    if x_o == 'X':
        count = count + 1
        if count in odd:
            buttons[m]['text'] = 'X'
            buttons[m]['bg'] = '#7df9ff'
        else:
            buttons[m]['text'] = 'O'
            buttons[m]['bg'] = '#ccff00'
    if x_o == 'O':
        count = count + 1
        if count in odd:
            buttons[m]['text'] = 'O'
            buttons[m]['bg'] = '#ccff00'
        else:
            buttons[m]['text'] = 'X'
            buttons[m]['bg'] = '#7df9ff'


def disable_button(n):
    if x_o in xo:
        buttons[n - 1]['state'] = DISABLED
        list_x_o.append(buttons[n - 1]['text'])


def disable_all():
    for i in range(9):
        buttons[i]['state'] = DISABLED


def win_check():
    combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for j in combinations:
        if buttons[j[0]]['text'] == buttons[j[1]]['text'] == buttons[j[2]]['text'] == 'X':
            buttons[j[0]]['bg'] = buttons[j[1]]['bg'] = buttons[j[2]]['bg'] = '#a9856a'
            return '*** PLAYER "X" WON ***'
        elif buttons[j[0]]['text'] == buttons[j[1]]['text'] == buttons[j[2]]['text'] == 'O':
            buttons[j[0]]['bg'] = buttons[j[1]]['bg'] = buttons[j[2]]['bg'] = '#a9856a'
            return '*** PLAYER "O" WON ***'
    else:
        pass


def tic_tac_toe():
    if list_x_o[-1] == 'X':
        mylabel1.destroy(), mylabel2.destroy(), mylabel_3('Player O Turn', '#ccff00')
    elif list_x_o[-1] == 'O':
        mylabel1.destroy(), mylabel2.destroy(), mylabel_3('Player X Turn', '#7df9ff')

    if len(list_x_o) <= 9:
        if win_check() == '*** PLAYER "X" WON ***' or win_check() == '*** PLAYER "O" WON ***':
            mylabel2.destroy(), mylabel_1(win_check()), mylabel_2(), disable_all()
    else:
        if win_check() == '*** PLAYER "X" WON ***' or win_check() == '*** PLAYER "O" WON ***':
            mylabel2.destroy(), mylabel_1(win_check()), mylabel_2(), disable_all()
        else:
            mylabel2.destroy(), mylabel_1('*** GAME DRAW ***'), mylabel_2()


def restart():
    global x_o, list_x_o, count
    button = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
    x_o = ''
    list_x_o = [0]
    count = 0
    button_x['state'] = NORMAL
    button_o['state'] = NORMAL
    for k in range(9):
        button[k]['state'] = NORMAL
        button[k]['text'] = ''
        button[k]['bg'] = '#e9ffdb'
    mylabel1.destroy(), mylabel2.destroy(), mylabel_0('Player 1 choose X or O!', '#77b5fe')


buttonfont = font.Font(family='Comic Sans MS', size=15, weight='bold')
mylabel_0('Player 1 choose X or O!', '#77b5fe')
button_x = Button(root, text='X', font=buttonfont, padx=15, pady=5,
                  borderwidth=5, bg='#7df9ff', command=lambda: [player_x(), choice()])
button_o = Button(root, text='O', font=buttonfont, padx=15, pady=5,
                  borderwidth=5, bg='#ccff00', command=lambda: [player_o(), choice()])
button_1 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(0), disable_button(1), tic_tac_toe()])
button_2 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(1), disable_button(2), tic_tac_toe()])
button_3 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(2), disable_button(3), tic_tac_toe()])
button_4 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(3), disable_button(4), tic_tac_toe()])
button_5 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(4), disable_button(5), tic_tac_toe()])
button_6 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(5), disable_button(6), tic_tac_toe()])
button_7 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(6), disable_button(7), tic_tac_toe()])
button_8 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(7), disable_button(8), tic_tac_toe()])
button_9 = Button(root, width=1, font=buttonfont, padx=60, pady=45,
                  bg='#e9ffdb', command=lambda: [change_text(8), disable_button(9), tic_tac_toe()])
button_0 = Button(root, width=4, text='Tic Tac Toe', font=buttonfont,
                  bg='#ed8545',  padx=40, pady=5, borderwidth=5, command=restart)

button_x.grid(row=0, column=0)
button_o.grid(row=0, column=2)
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=6, column=0)
button_5.grid(row=6, column=1)
button_6.grid(row=6, column=2)
button_7.grid(row=7, column=0)
button_8.grid(row=7, column=1)
button_9.grid(row=7, column=2)
button_0.grid(row=0, column=1, pady=10)

root.mainloop()
