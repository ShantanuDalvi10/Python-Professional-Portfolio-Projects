
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk

def upload_image():
    global image,preview_image,w_preview_image
    preview_image = None
    image = None
    w_preview_image = None

    file_path = filedialog.askopenfilename()

    if file_path:
        image = Image.open(file_path)
        print("File uploaded successfully.")


        preview = image.copy()
        preview.thumbnail((200,100))

        preview_image = ImageTk.PhotoImage(preview)

        image_label.config(image=preview_image)

        upload_label.config(text="Image uploaded successfully.",fg="green")


def add_watermark():
    global w_preview_image
    if image is None:
        status_label.config(text="Please Enter the Image.")

    Draw = ImageDraw.Draw(image)

    text = text_entry.get()

    Draw.text(
        (10,10),
        text,
        fill="black"
    )
    status_label.config(text="Image has been watermarked.",fg="green",bg="white")

    w_preview = image.copy()
    w_preview.thumbnail((200,100))

    w_preview_image = ImageTk.PhotoImage(w_preview)
    watermarked_image_preview.config(image=w_preview_image)



def save_image():
    if image is None:
        status_label.config(text="please enter the image")

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image","*.png"),
                   ("JPEG Image","*.jpeg")]
    )

    if save_path:
        image.save(save_path)
        status_label.config(text="Watermarked image is saved.")




window = Tk()
window.title("Image Watermarking App")
window.config(bg="white")
window.geometry("350x500")

title_label = Label(text="Image Watermarking App",fg="black",font=("Bold",20),bg="white")
title_label.grid(column=1,row=0)

upload_button = Button(text="Upload Image",highlightthickness=0,width=20,height=2,bg="blue",fg="white",command=upload_image)
upload_button.grid(column=1,row=1)

upload_label = Label(text="Please upload an Image.",fg="red",bg="white",font=("Arial",8))
upload_label.grid(column=1,row=2)

preview_label = Label(text="Preview",fg="black",bg="white",font=("Arial",12,"bold"))
preview_label.grid(column=1,row=3)

image_label = Label()
image_label.grid(column=1,row=4)

watermark_label = Label(text="Enter Watermark text : ",fg="black",bg="white",font=("Arial",10,"bold"))
watermark_label.grid(column=1,row=5)

text_entry = Entry(width=30)
text_entry.grid(column=1,row=6)

watermark_button = Button(text="Add Watermark",highlightthickness=0,width=20,height=2,bg="blue",fg="white",command=add_watermark)
watermark_button.grid(column=1,row=7)

watermarked_label = Label(text="Watermarked Image Preview",fg="black",bg="white",font=("Arial",12,"bold"))
watermarked_label.grid(column=1,row=8)

watermarked_image_preview = Label()
watermarked_image_preview.grid(column=1,row=9)

status_label = Label(text="Image is not watermarked.",fg="red",bg="white",font=("Arial",10))
status_label.grid(column=1,row=10)

save_button = Button(text="Save",highlightthickness=0,width=10,height=2,bg="blue",fg="white",command=save_image)
save_button.grid(column=1,row=11)

window.mainloop()
