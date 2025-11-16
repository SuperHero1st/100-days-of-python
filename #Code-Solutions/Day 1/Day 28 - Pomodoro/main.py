from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks=""
timer = None

def update_checkmarks_label():
    global checkmarks_label, check_marks
    check_marks+= "✔"
    checkmarks_label.config(text=check_marks)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text= "Timer", fg=GREEN)
    checkmarks_label.config(text= "")
    canvas.itemconfig(timer_text, text= "00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, title_label, window
    # Bring the window to the front
    window.lift()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    window.focus_force()

    reps += 1
    work_sec = WORK_MIN *1
    short_break_sec = SHORT_BREAK_MIN *1
    long_break_sec = LONG_BREAK_MIN *1
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text= "Break", fg=RED)
    elif reps %2 ==0:
        count_down(short_break_sec)
        title_label.config(text= "Break", fg=PINK)
    else:
        count_down(work_sec, work_session=True)
        title_label.config(text= "Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count, work_session=False):
    global timer
    count_min = math.floor(count/60)
    count_sec = count %60
    if count_sec <10:               #formatting seconds, using dynamic typing
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}: {count_sec}")
    if count> 0:
        timer = window.after(1000, count_down, count-1, work_session)
    elif work_session== True:
        update_checkmarks_label()
        start_timer()
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 100, bg=YELLOW)
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white", font=(FONT_NAME, 35 , "bold"))
canvas.grid(row= 1, column=1)

#Labels and buttons
title_label = Label(text= "Timer", font=(FONT_NAME, 38, "bold"), bg= YELLOW, fg= GREEN)
title_label.grid(row= 0, column= 1,)

checkmarks_label = Label(text= "", font=(FONT_NAME, 12, "bold"), bg= YELLOW, fg= GREEN)
checkmarks_label.grid(row= 3, column= 1,)

start_button = Button(text="Start", font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(row= 2, column= 0)

reset_button = Button(text="Reset", font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(row= 2, column= 2)

window.mainloop()