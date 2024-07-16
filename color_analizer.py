import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def get_colors(image_path):
    image = Image.open(image_path)
    image_rgb = image.convert("RGB")
    colors = image_rgb.getcolors(maxcolors=1000000)
    colors = sorted(colors, reverse=True, key=lambda x: x[0])
    top_colors = colors[:10]
    return top_colors

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        try:
            colors = get_colors(file_path)
            display_colors(colors)
            img = Image.open(file_path)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img
        except Exception as e:
            messagebox.showerror("Error", f"Error processing image: {e}")

def display_colors(colors):
    colors_list.delete(0, tk.END)
    for count, color in colors:
        colors_list.insert(tk.END, f"RGB: {color} - Count: {count}")
        colors_list.itemconfig(tk.END, {'bg': f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'})

app = tk.Tk()
app.title("ColorAnalyzer")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

open_button = tk.Button(frame, text="Open Image", command=open_file)
open_button.pack()

image_label = tk.Label(frame)
image_label.pack()

colors_list = tk.Listbox(frame, width=50)
colors_list.pack()

app.mainloop()
