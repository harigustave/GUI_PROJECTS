import tkinter as tk
from PIL import ImageTk

bg_color="#17202A"
# Initialize the app
root= tk.Tk()
root.title("Kigali Public Bus Live")
root.eval("tk::PlaceWindow . center")

frame1=tk.Frame(root, width=1400, height=800, bg=bg_color, padx=20, pady=20)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_image=ImageTk.PhotoImage(file="assets/bus-stop.png")
logo_widget=tk.Label(frame1, image=logo_image, bg=bg_color)
logo_widget.image=logo_image
logo_widget.pack()

tk.Label(
    frame1, 
    text="Kigali City Public Bus Live Location",
    bg=bg_color,
    fg="yellow",
    font=("TkMenuFont", 28,"bold", ),
    pady=20
    ).pack()

tk.Label(
    frame1, 
    text="BUS No: 305,  Kanombe - DownTown",
    bg=bg_color,
    fg="#FFFFFF",
    font=("TkMenuFont", 14,),
    pady=0
    ).pack()

# Run the app
root.mainloop()