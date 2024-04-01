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
reps =0
timer = 0
check="     "

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label4.config(text="")
    label2.config(text= "TIMER", bg=YELLOW, fg=GREEN,  font= (FONT_NAME, 38, "bold"))
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer() :
    global reps
    global check

    reps +=1
    work_sec= 0
    short_break = 0
    long_break = LONG_BREAK_MIN

    if reps % 8==0:
        # check += "✔️" if reps != 1 else ""
        label4.config(text=check)
        count_down(10, long_break)
        label2.config(text="Break", fg= GREEN)

    elif reps % 2 == 0:
        count_down(10, short_break)
        label2.config(text="Break", fg= PINK)
        # check += "✔️" if reps != 1 else ""
        # label4.config(text=check)
    else:
        count_down(10, work_sec)
        label2.config(text="Work", fg= RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds , minutes):
    global timer
    global check


    canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}" if seconds>9 else  f"{minutes}:0{seconds}" )
    if minutes >=0 and seconds>0:
        timer =    window.after(1000, count_down,  seconds-1,minutes)

    if minutes > 0 and seconds == 0:
        timer =    window.after(1000, count_down, 59, minutes-1)
    if minutes == 0 and seconds == 0:
        check += "✔️"
        label4.config(text=check)
        start_timer()





# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("POMODORO")
window.config(padx=100, pady= 50, bg=YELLOW)
label2= Label(text= "TIMER", bg=YELLOW, fg=GREEN,  font= (FONT_NAME, 38, "bold"))
label2.grid(row= 0, column = 1)

start= PhotoImage(file = "start.png")
label1= Button(image= start, command= start_timer , bg= YELLOW, border=0)
label1.grid(row= 2, column = 0)
reset= PhotoImage(file = "restart.png")
label3= Button(image= reset, command= reset_timer , bg= YELLOW, border=0)
label3.grid(row= 2, column = 2)

label4= Label(text= "", bg = YELLOW, fg= GREEN , font=(36), anchor="center")
label4.grid(row= 3, column = 1)

canvas = Canvas(width=200 , height=224, highlightthickness=0)
canvas.config(bg = YELLOW)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image= tomato )
timer_text = canvas.create_text(102,130, text="00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row= 1, column = 1)


window.mainloop()
