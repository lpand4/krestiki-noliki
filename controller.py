from tkinter import *

frm = []
btn = []
play_area = [0, 0, 0, 0, 0, 0, 0, 0, 0]
who = True
root = Tk()


def start():
    root.geometry("500x200")
    root.config(background='LightSkyBlue1')
    root.title('Крестики-нолики')
    rule = Label(text='Игра "Крестики-нолики"', font=("Comic Sans MS", 25, "bold"), background='LightSkyBlue1',
                 foreground="black")
    rule.pack()
    button_quit = Button(text="Quit", font=('mono', 20, 'bold'), width=3, height=1, command=root.quit)
    button_quit.pack(expand=YES, fill='x', side=LEFT, padx=1, pady=1)
    button_play = Button(text="Play", font=('mono', 20, 'bold'), width=3, height=1, command=create_game_window)
    button_play.pack(expand=YES, fill='x', side=LEFT, padx=1, pady=1)

    mainloop()


# Узнает куда нудно поставить крестик/нолик
def game():
    for i in range(3):
        for j in range(3):
            btn[i * 3 + j].config(command=lambda n=i * 3 + j: play(n))


# Проверяет победу
def check_win(area):
    win_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_condition:
        if area[item[0]] == area[item[1]] == area[item[2]] == 1:
            create_msg('Победа Крестиков!')
            return 1
        if area[item[0]] == area[item[1]] == area[item[2]] == -1:
            create_msg('Победа Ноликов!')
            return 1
    return False


# Ставит крестик/нолик
def play(n):
    global who
    btn[n].config(text='X' if who else 'O', state=DISABLED)
    play_area[n] = 1 if who else -1
    check_win(play_area)
    who = not (who)
    if play_area.count(0) == 0:
        create_msg('Ничья!')



# Создает окно с игрой
def create_game_window():
    global root
    game_window = Toplevel(root)
    game_window.geometry('300x300')
    game_window.title('Game')
    add_playground(game_window)
    game()

# def obnullenie():
#     for i in range(9):
#         btn[i].config(text='')
#         play_area[i] = 0

# Создает окно с надписью
def create_msg(msg):
    msg_window = Toplevel(root)
    msg_window.title("Winner")
    #
    the_msg = Label(msg_window, text=msg, font=("Comic Sans MS", 24, "bold"), foreground="black")
    the_msg.pack()
    btn = Button(msg_window, text='Quit', font=("Comic Sans MS", 24, "bold"), command=quit)
    btn.pack()


# Создает игровое поле
def add_playground(game_window):
    for i in range(3):
        frm.append(Frame(game_window))
        frm[i].pack(expand=YES, fill=BOTH)
        for j in range(3):
            btn.append(Button(frm[i], text=' ', font=('mono', 25, 'bold'), width=3, height=1))
            btn[i * 3 + j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
