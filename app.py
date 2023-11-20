import tkinter as tk

root = tk.Tk()
# root.geometry()

left_frame = tk.Frame(root, width=250, height=700, bg='red')
left_frame.pack(side=tk.LEFT)

center_frame = tk.Frame(root, width=600, height=700, bg='green')
center_frame.pack(side=tk.LEFT)

right_frame = tk.Frame(root, width=400, height=700, bg='blue')
right_frame.pack(side=tk.LEFT)

root.mainloop()


