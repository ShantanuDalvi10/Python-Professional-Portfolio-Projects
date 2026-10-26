from tkinter import *

window = Tk()
window.title("Dangerous Writing App")
window.geometry("800x500")
window.config(bg="white")

heading = Label(
    text="The Most Dangerous Typing App",
    font=("Arial",20,"bold"),
    fg="black",
    bg="white"
)
heading.pack(pady=20)

text_box = Text(
    font=("Arial",16),
    fg="black",
    bg="white"
)
text_box.pack(padx=20,pady=10,expand=True,fill="both")

timer = None

def delete_text():
    text_box.delete("1.0",END)

def reset_timer(event=None):
    global timer

    if timer is not None:
        window.after_cancel(timer)

    timer = window.after(5000,delete_text)


text_box.bind("<KeyRelease>",reset_timer)

window.mainloop()
