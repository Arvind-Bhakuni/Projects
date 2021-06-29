# importing necessary libraries
import random
import tkinter as tk

# creating objects
root = tk.Tk()

# set geometry
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock Paper Scissor')

# defining global variable
user_score = 0
com_score = 0
user_choice = ''
com_choice = ''

# define a function to convert user choice to number
def choice_to_number(ch):
    rps = {'Rock' :0, 'Paper' :1, 'Scissor' :2}
    return rps[ch]


def number_to_choice(n):
    rps = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
    return rps[n]

# create a function to get the computer choice
def comp_choice():
    return random.choice(['Rock', 'Paper', 'Scissor'])


def play(human, com):
    global user_score
    global com_score
    user = choice_to_number(human)
    com = choice_to_number(com)

    if user == com:
        lb4.config(text="It's a Tie!")
        lb5.config(text="Your Choice: {}\nComputer's choice: {}".format(human, number_to_choice(com)))
        lb6.config(text='Computer Score: {}\nYour Score: {}'.format(com_score, user_score))
        # lb5.Text()

    elif (user-com)%3==1:
        lb4.config(text='You Win!')
        user_score += 1
        lb5.config(text="Your Choice: {}\nComputer's choice: {}".format(human, number_to_choice(com)))
        lb6.config(text='Computer Score: {}\nYour Score: {}'.format(com_score, user_score))

    else:
        lb4.config(text='Computer Win!')
        com_score += 1
        lb5.config(text="Your Choice: {}\nComputer's choice: {}".format(human, number_to_choice(com)))
        lb6.config(text='Computer Score: {}\nYour Score: {}'.format(com_score, user_score))

    disable_buttons()


# define 3 functions rock, paper and scissor
def rock():
    global user_choice, com_choice
    user_choice = 'Rock'
    com_choice = comp_choice()
    play(user_choice, com_choice)


def paper():
    global user_choice, com_choice
    user_choice = 'Paper'
    com_choice = comp_choice()
    play(user_choice, com_choice)


def scissor():
    global user_choice, com_choice
    user_choice = 'Scissor'
    com_choice = comp_choice()
    play(user_choice, com_choice)


# function to reset the play
def reset_play():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    lb1.config(text='Player')
    lb2.config(text='vs')
    lb3.config(text="Computer")
    lb4.config(text='')


# function to disable the buttons
def disable_buttons():
    b1['state'] = 'disable'
    b2['state'] = 'disable'
    b3['state'] = 'disable'

# adding labels
tk.Label(root, text='Rock Paper Scissor', font='normal 22 bold', fg='green').pack(pady=10)

frame1 = tk.Frame(root)
frame1.pack()

lb1 = tk.Label(frame1, text='Player', font=14)
lb1.pack(side=tk.LEFT)
lb2 = tk.Label(frame1, text='vs', font='normal 14 bold')
lb2.pack(side=tk.LEFT)
lb3 = tk.Label(frame1, text='Computer', font=14)
lb3.pack()
lb4 = tk.Label(root, text="", font='normal 22 bold', bg='#E0E3D9', width=15, borderwidth=2, relief='solid')
lb4.pack(pady=15)


frame2 = tk.Frame(root)
frame2.pack()

b1 = tk.Button(frame2, text='Rock', font=14, width=10, command=rock, bg='#E3D9E0')
b1.pack(side=tk.LEFT, pady=8)

b2 = tk.Button(frame2, text='Paper', font=14, width=10, command=paper, bg='#E3D9E0')
b2.pack(side=tk.LEFT, pady=8)

b3 = tk.Button(frame2, text='Scissor', font=14, width=10, command=scissor, bg='#E3D9E0')
b3.pack(side=tk.LEFT, pady=8)

lb5 = tk.Label(root, text="", font=5, bg='#E0E3D9', width=30, height=2, borderwidth=1, relief='solid')
lb5.pack()

lb6 = tk.Label(root, text="", font=5, bg='#E0E3D9', width=30, height=2, borderwidth=1, relief='solid')
lb6.pack()

# reset button
tk.Button(root, text='Reset Game', width=17, font=10, fg='orange', bg='#272951', command=reset_play).pack(side=tk.LEFT, pady=5)
# exit button
tk.Button(root, text="Exit Game", command=root.destroy, width=17, font=10, fg='orange', bg='#272951').pack(side=tk.RIGHT, pady=5)

root.mainloop()