import png
import pyqrcode
import tkinter as tk
from flask import Flask
app = Flask(__name__)


@app.route("/")
def generate_qr_code():
    # Get the URL from the user input
    url = user_input.get()

    # Generate the QR code
    qr = pyqrcode.create(url)

    # Save the QR code as a PNG file
    qr.png('qr_code.png', scale=8)

    # Display the QR code in the GUI
    qr_image = tk.PhotoImage(file='qr_code.png')
    qr_label.config(image=qr_image)
    qr_label.image = qr_image


# Create the main window
root = tk.Tk()

# Create a label and an input field for the URL
tk.Label(root, text='Enter URL:').pack()
user_input = tk.Entry(root)
user_input.pack()

# Create a button to generate the QR code
tk.Button(root, text='Generate QR Code', command=generate_qr_code).pack()

# Create a label to display the QR code
qr_label = tk.Label(root)
qr_label.pack()

# Create a button to download the QR code image


def download():
    # Save the QR code image to a file
    qr_label.image.write("qr_code.png", format="png")


download_button = tk.Button(root, text='Download QR Code', command=download)
download_button.pack()

# Run the main loop
root.mainloop()
