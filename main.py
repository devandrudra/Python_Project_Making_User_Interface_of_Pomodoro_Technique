from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # https://colorhunt.co/palettes/vintage
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0

# ---------------------------- TIMER RESET ------------------------------- #

timer = None


def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text = 'Timer')
    check_mark_label.config(text="")
    global resp
    resp = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global resp
    resp += 1
    print(resp)
    if resp == 8:
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
        title_label.config(text = "Break", fg = RED)

    elif resp % 2 == 0:
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
        title_label.config(text="Break", fg = PINK)

    else:
        work_sec = WORK_MIN * 60
        count_down(work_sec)
        title_label.config(text="WORK", fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min= "00"
    elif count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(20, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(resp/ 2)):
            mark += "✔"
        check_mark_label.config(text = mark)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx = 50, pady = 50, bg = YELLOW)


title_label = Label(text = "Timer", fg = 'Green', bg = "#f7f5dd", font = ("Courier", 40))
title_label.grid(row = 0, column = 1)



canvas = Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness= False)
img = PhotoImage(file = "tomato.png")
canvas.create_image(101, 108, image = img)
timer_text = canvas.create_text(103, 130, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(row = 1, column = 1)

start_button = Button(text = "Start", command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_mark_label = Label(font = ("Courier", 20), bg = YELLOW, fg = "green")
check_mark_label.grid(row = 3, column = 1)




window.mainloop()