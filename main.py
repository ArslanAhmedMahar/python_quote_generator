from tkinter import *
import requests


def get_quote():
    responce = requests.get("https://api.kanye.rest")
    responce.raise_for_status()
    data = responce.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Arslan Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Arslan Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

arslan_img = PhotoImage(file="quote1.png")

# Resize the image to make the button smaller
emoji_size = arslan_img.subsample(10, 10)  # Adjust subsample values as needed
arslan_button = Button(image=emoji_size, highlightthickness=0, command=get_quote)
arslan_button.grid(row=1, column=0)

window.mainloop()
