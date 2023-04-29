import math
from tkinter import *

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
timer = None





# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer",fg=GREEN)
    check.config(text="")
    window.after_cancel(timer)
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    reps=0





# ---------------------------- TIMER MECHANISM ------------------------------- # 

def click_start():
    global reps
    reps += 1
    work_time = WORK_MIN*60
    short_break_time = SHORT_BREAK_MIN*60
    long_break_time = LONG_BREAK_MIN*60

    if reps % 2 == 0:
        count_down(short_break_time)
        label.config(text="Break",fg=PINK)

    elif reps % 8 == 0:
        count_down(long_break_time)
        label.config(text="Break" , fg=RED)
    else:
        count_down(work_time)
        label.config(text = "Work" , fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if int(count_sec) <= 9 and int(count_sec) > 0:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        click_start()
        marks=""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✓"
        check.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)

label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 15), bg=YELLOW, bd=0, highlightthickness=0, width=7,
                      height=2, command=click_start)
start_button.grid(row=3, column=1)

check = Label(window, font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN)
check.grid(row=3, column=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg=YELLOW, bd=0, highlightthickness=0, width=7, height=2,
                      fg=PINK,command=reset)
reset_button.grid(row=3, column=3)

window.mainloop()
