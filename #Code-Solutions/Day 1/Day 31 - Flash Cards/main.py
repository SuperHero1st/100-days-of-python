from tkinter import *
import pandas
import random
from functools import partial

BACKGROUND_COLOR = "#B1DDC6"
rand_index = 0

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')

words_to_learn = data.to_dict(orient="Records")

def correct_button_clicked():
    global rand_index, words_to_learn
    words_to_learn.pop(rand_index)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    update_card()

def update_card():
    global flip_timer, rand_index, words_to_learn
    window.after_cancel(flip_timer)
    front_canvas.itemconfig(card_background, image= front_card_pic)
    rand_index = random.randint(0,len(words_to_learn)-1)
    french_word = words_to_learn[rand_index]['French']
    front_canvas.itemconfig(title_text, text= "French", fill= 'black' )
    front_canvas.itemconfig(word_text, text= french_word, fill= 'black' )
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global rand_index
    english_word = words_to_learn[rand_index]['English']
    front_canvas.itemconfig(card_background, image= back_card_pic)
    front_canvas.itemconfig(title_text, text= "English", fill="white")
    front_canvas.itemconfig(word_text, text= english_word, fill="white")
    

###################################### UI SETUP ####################################
window = Tk()
window.title("Flash Cards")
window.config(width= 800, height= 526, padx=50, bg=BACKGROUND_COLOR)

#Buttons
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

right_button = Button(width=100, height=100, image=right_image, highlightthickness=0, borderwidth=0, command= correct_button_clicked )
right_button.grid(row=1, column=1)

wrong_button = Button(width=100, height=100, image=wrong_image, padx=0, highlightthickness=0, borderwidth=0, command= update_card)
wrong_button.grid(row=1, column=0, )

#Canvas
back_card_pic = PhotoImage(file='images/card_back.png')
front_card_pic = PhotoImage(file='images/card_front.png')
front_canvas = Canvas(width= 800, height= 526, )
card_background = front_canvas.create_image(400, 263, image= front_card_pic)
front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_canvas.grid(row= 0, column=0, columnspan=2)

title_text = front_canvas.create_text(400, 150, text="",fill="black", font=('Ariel', 40, "bold"))
word_text = front_canvas.create_text(400, 250, text="",fill="black", font=('Courier', 34 ))

flip_timer = window.after(3000, func= update_card)
update_card()   # Call update_card to display the first card immediately

window.mainloop()

