# import tkinter as tk
# from tkinter import ttk
import customtkinter as ctk

class App(ctk.CTk):
  def __init__(self, start_size):
    super().__init__()
    self.title('Responsive Layout')
    self.geometry(f'{start_size[0]}x{start_size[1]}')

    self.frame = ctk.CTkFrame(self)
    self.frame.pack(expand = True, fill = 'both')

    size_notifier = SizeNotifier(self, { 
      300: self.create_small_layout, 
      600: self.create_medium_layout,
      1200: self.create_large_layout,
      })
    self.mainloop()
  
  def create_small_layout(self):
      self.frame.pack_forget()
      self.frame = ctk.CTkFrame(self)
      ctk.CTkLabel(self.frame, text = 'Label 1', fg_color =  'red').pack(expand = True, fill = 'both', padx = 10, pady = 5)
      ctk.CTkLabel(self.frame, text = 'Label 2', fg_color =  'green').pack(expand = True, fill = 'both', padx = 10, pady = 5)
      ctk.CTkLabel(self.frame, text = 'Label 3', fg_color =  'blue').pack(expand = True, fill = 'both', padx = 10, pady = 5)
      # ctk.CTkLabel(self.frame, text = 'Label 4', fg_color =  'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 5)
      self.frame.pack(expand = True, fill = 'both')
  
  def create_medium_layout(self):
      self.frame.pack_forget()
      self.frame = ctk.CTkFrame(self)
      self.frame.columnconfigure((0,1), weight = 1, uniform = 'a')
      self.frame.rowconfigure((0,1), weight = 1, uniform = 'a')
      self.frame.pack(expand = True, fill = 'both')

      
      # * Controls
      ctk.CTkLabel(self.frame, text = 'Label 1', fg_color =  'red').grid(column = 0, row = 0, sticky = 'nsew', padx = 10, pady = 10)
      
      # * Image
      ctk.CTkLabel(self.frame, text = 'Label 2', fg_color =  'green').grid(column = 0, row = 1, columnspan = 3, sticky = 'nsew', padx = 10, pady = 10)

      # * Info
      ctk.CTkLabel(self.frame, text = 'Label 3', fg_color =  'blue').grid(column = 1, row = 0, sticky = 'nsew', padx = 10, pady = 10)
      # ttk.Label(self.frame, text = 'Label 4', fg_color =  'yellow').grid(column = 1, row = 1, sticky = 'nsew', padx = 10, pady = 10)
  
  def create_large_layout(self):
      self.frame.pack_forget()
      
      self.frame = ctk.CTkFrame(self)
      self.frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
      self.frame.rowconfigure(0, weight = 1, uniform = 'a')
      self.frame.pack(expand = True, fill = 'both')

      ctk.CTkLabel(self.frame, text = 'Label 1', fg_color =  'red').grid(column = 0, row = 0, sticky = 'nsew', padx = 10, pady = 10)
      ctk.CTkLabel(self.frame, text = 'Label 2', fg_color =  'green').grid(column = 1, row = 0, columnspan = 2, sticky = 'nsew', padx = 10, pady = 10)
      ctk.CTkLabel(self.frame, text = 'Label 3', fg_color =  'blue').grid(column = 3, row = 0, sticky = 'nsew', padx = 10, pady = 10)
      # ttk.Label(self.frame, text = 'Label 4', fg_color =  'yellow').grid(column = 3, row = 0, sticky = 'nsew', padx = 10, pady = 10)


class SizeNotifier:
  def __init__(self, window, size_dict):
      self.window = window
      self.size_dict = {key: value for key, value in sorted(size_dict.items())}
      self.current_min_size = None
      self.window.bind('<Configure>', self.check_size)

      self.window.update()

      min_height = self.window.winfo_height()
      min_width = list(self.size_dict)[0]
      self.window.minsize(min_width, min_height)
  
  def check_size(self, event):
      if event.widget == self.window:
        window_width = event.width
        checked_size = None

        for min_size in self.size_dict:
          delta = window_width - min_size
          if delta >= 0:
            checked_size = min_size

        if checked_size != self.current_min_size:
          self.current_min_size = checked_size
          self.size_dict[self.current_min_size]()

app = App((800, 600))