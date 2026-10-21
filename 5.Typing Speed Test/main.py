from tkinter import *
import time

SAMPLE_TEXT = ("India is a diverse country with a rich cultural heritage. "
"It is famous for its festivals and delicious traditional food. "
"Explore India every day to learn about its history and beauty.")

start_time = None
timer_running = None
timer_id = None

def start_timer(event=None):
    global start_time,timer_running

    if not timer_running:
        start_time = time.time()
        timer_running = True
        update_timer()


def update_timer():
    global timer_id

    if timer_running:
        elapsed = int(time.time() - start_time)
        timer_label.config(text=f"Time : {elapsed} seconds")
        timer_id = window.after(1000,update_timer)

def calculate_speed():
    global timer_running,timer_id

    if not timer_running:
        result_label.config(text="Please start typing")
        return

    end_time = time.time()
    elapsed = end_time - start_time

    typed_text = typing_area.get("1.0","end-1c")
    words = len(typed_text.split())

    if elapsed > 0:
        wpm = words / elapsed * 60
    else:
        wpm = 0

    timer_running = False

    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

    timer_label.config(text=f"Time: {elapsed:.1f} seconds")
    result_label.config(
        text=f"Your typing speed: {wpm:.1f} WPM\n"
             f"Words typed: {words}"
    )

def reset_test():
    global start_time, timer_running, timer_id

    timer_running = False

    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

    start_time = None

    typing_area.config(state="normal")
    typing_area.delete("1.0","end")

    timer_label.config(text="Time: 0 seconds")
    result_label.config(text="Start typing to begin!")

    typing_area.focus_set()

window = Tk()
window.title("Typing Speed Test")
window.geometry("700x500")
window.configure(bg="#f0f4f8")

title_label = Label(text="Typing Speed Test",
                    font=("Arial",24,"bold"),
                    bg="#f0f4f8",
                    fg="#1e3a5f")
title_label.pack(pady=15)

instruction_label = Label(text="Type the sample text as fast as you can.",
                          font=("Arial",12),
                          bg="#f0f4f8")
instruction_label.pack()

sample_label = Label(text=SAMPLE_TEXT,
                     font=("Arial",12),
                     wraplength=620,
                     bg="white",
                     fg="#333333",
                     padx=10,
                     pady=10)
sample_label.pack(pady=15)

typing_area = Text(height=6,
                   width=65,
                   font=("Arial",12),
                   wrap="word")
typing_area.pack(pady=10 )

typing_area.bind("<KeyPress>",start_timer)

timer_label = Label(
    text="Time : 0 seconds",
    font=("Arial",14),
    bg="#f0f4f8"
)
timer_label.pack(pady=5)

result_label = Label(
    text="Start Typing to Begin",
    font=("Arial",14),
    bg="#f0f4f8",
    fg="#167d5a"
)
result_label.pack(pady=5)

button_frame = Frame(window,bg="#f0f4f8")
button_frame.pack(pady=10)

finish_button = Button(
    button_frame,
    text="Finish Test",
    bg="#2563eb",
    fg="white",
    command=calculate_speed
)
finish_button.pack(side="left",padx=10)

restart_button = Button(
    button_frame,
    text="Restart",
    bg="#16a34a",
    fg="white",
    command=reset_test
)
restart_button.pack(side="left",padx=10)

window.mainloop()