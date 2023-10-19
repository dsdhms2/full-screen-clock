import tkinter as tk
import time
from datetime import datetime

# Create a tkinter window
root = tk.Tk()
root.attributes('-fullscreen', True)

# Create a label to display the time
time_label = tk.Label(root, font=('Helvetica', 100), bg='black', fg='white')

# Update the time every second
def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

# Create a button to toggle full screen mode
def toggle_fullscreen():
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

fullscreen_button = tk.Button(root, text='Toggle Full Screen', command=toggle_fullscreen)
fullscreen_button.pack()

# Pack the label and start the update loop
time_label.pack(expand=True)
update_time()

# Run the tkinter event loop
root.mainloop()