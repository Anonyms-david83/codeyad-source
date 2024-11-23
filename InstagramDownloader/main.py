import urllib.request
from PIL import ImageTk, Image
import tkinter as tk

# create the Tkinter window
root = tk.Tk()

# set the window title
root.title("Display image from URL")

# open the image from the URL
url = "https://ibb.co/cbtn9tP"
with urllib.request.urlopen(url) as u:
    raw_data = u.read()

# convert the raw data to a Tkinter image
image = Image.open(io.BytesIO(raw_data))
photo = ImageTk.PhotoImage(image)

# create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# run the Tkinter event loop
root.mainloop()