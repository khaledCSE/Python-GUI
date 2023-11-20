import tkinter as tk
import ttkbootstrap as ttk

def convert():
  mile_input = entry_int.get()
  km_output = mile_input * 1.06
  output_val = f'{km_output} kilometers'
  output_string.set(output_val)

# Window
window = ttk.Window(themename='darkly')
window.title('Distance Converter')
window.geometry('300x150')

# Title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Calibri 20', textvariable=output_string)
output_label.pack()

# Run
window.mainloop()