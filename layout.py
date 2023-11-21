# import tkinter as tk
# from tkinter import ttk
from textwrap import fill
from turtle import title
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

      # * Controls
      left = ctk.CTkFrame(self.frame)
      left.grid(column = 0, row = 0, sticky = 'nsew', padx = 10, pady = 10)

      left_header = ctk.CTkLabel(left, text='Enter Data', font=('Roboto', 24), padx = 10, pady = 10)
      image_chooser_label = ctk.CTkLabel(left, text='Choose an Image:', font=('Roboto', 14), padx = 10, pady = 20)
      upload_button = ctk.CTkButton(left, text = 'Select Image', font=('Roboto', 14), border_spacing=10)
      model_chooser_label = ctk.CTkLabel(left, text='Select a Model:', font=('Roboto', 14), padx = 10, pady = 20)
      model_selector_combo = ctk.CTkComboBox(left, values=['YOLO v8', 'YOLO v7', 'YOLO v6', 'YOLO v5'], corner_radius=10)

      # * Filter Selection
      filter_selection_frame = ctk.CTkFrame(left, corner_radius=10)
      image_filter_label = ctk.CTkLabel(filter_selection_frame, text='Image Filters', font=('Roboto', 18), pady=20)
      resolution_label = ctk.CTkLabel(filter_selection_frame, text='Select Resolution', font=('Roboto', 14), pady=10)
      resolution_selector_combo = ctk.CTkComboBox(filter_selection_frame, values=['Low', 'Medium', 'High'])
      noise_label = ctk.CTkLabel(filter_selection_frame, text='Select Noise', font=('Roboto', 14), pady=10)
      noise_selector_combo = ctk.CTkComboBox(filter_selection_frame, values=['Low', 'Medium', 'High'])
      contrast_label = ctk.CTkLabel(filter_selection_frame, text='Select Contrast', font=('Roboto', 14), pady=10)
      contrast_selector_combo = ctk.CTkComboBox(filter_selection_frame, values=['Low', 'Medium', 'High'])
      color_label = ctk.CTkLabel(filter_selection_frame, text='Select Color', font=('Roboto', 14), pady=10)
      color_selector_combo = ctk.CTkComboBox(filter_selection_frame, values=['Red', 'Green', 'Blue'])

      filter_frame_empty_label = ctk.CTkLabel(filter_selection_frame, text='', pady=5)

      image_filter_label.pack()
      resolution_label.pack()
      resolution_selector_combo.pack()
      noise_label.pack()
      noise_selector_combo.pack()
      contrast_label.pack()
      contrast_selector_combo.pack()
      color_label.pack()
      color_selector_combo.pack()
      filter_frame_empty_label.pack()
      
      # * Packing
      left_header.pack()
      image_chooser_label.pack()
      upload_button.pack()
      model_chooser_label.pack()
      model_selector_combo.pack()
      filter_selection_frame.pack(expand = True, fill='x')

      # * Call to action
      proceed_button = ctk.CTkButton(left, text='Process Image', font=('Roboto', 18), border_spacing=10)
      proceed_button.pack()

      # * Empty Label for spacing
      proceed_label = ctk.CTkLabel(left, text='', pady=5)
      proceed_label.pack()

      # ************* Left end ******************

      # * Image
      ctk.CTkLabel(self.frame, text = 'Label 2', fg_color =  'green').grid(column = 1, row = 0, columnspan = 2, sticky = 'nsew', padx = 10, pady = 10)

      # * Info
      right = ctk.CTkFrame(self.frame)
      right.grid(column = 3, row = 0, sticky = 'nsew', padx = 10, pady = 10)

      right_header = ctk.CTkLabel(right, text='Detected Parts', font=('Roboto', 24), padx = 10, pady = 10)

      detection_result_frame = ctk.CTkFrame(right)

      # * Detection GRID
      detect_frame_left = ctk.CTkFrame(detection_result_frame, fg_color='transparent')
      detect_frame_right = ctk.CTkFrame(detection_result_frame, fg_color='transparent')

      detect_frame_left.pack(side='left')
      detect_frame_right.pack(side='right')

      for i in range(0, 14):
         if i % 2 == 0:
            ctk.CTkLabel(detect_frame_left, text=f'{i + 1}: tibia [0, 74]', padx=10).pack(side=ctk.TOP)
         else:
            ctk.CTkLabel(detect_frame_right, text=f'{i + 1}: tibia [0, 74]', padx=10).pack(side=ctk.TOP)
      # * ******* Detection GRID end ***********

      display_info_prompt = ctk.CTkLabel(right, text='Select a Part to Display', font=('Roboto', 14), padx = 10, pady = 10)
      component_selector_combo = ctk.CTkComboBox(right, values=['Component 1', 'Component 2', 'Component 3'])
      component_empty_label = ctk.CTkLabel(right, text='')
      component_show_button = ctk.CTkButton(right, text='Show Component')

      selected_result_frame = ctk.CTkFrame(right)

      selected_result_output = [
         'Lh Standard Footrest SW 38Cm/40,5Cm - Short',
         'Lower Tube, Part number: 1530620',
         'included parts',
         'Fixed Footplate Ng Left 174mm (Sw38-40.5)',
         'Part number: 1529643',
         'Footrest Tube, Short',
         'Part number: 1434561-0010',
         'Screw Kit, Footrest Fixed',
         'Part number: 1430433',
         'Plug Ikpt 2017S',
         'Part number: 1424576',
         'Lh Standard Footrest SW 38Cm/40,5Cm - Short',
         'Lower Tube, Part number: 1530620',
         'included parts',
         'Fixed Footplate Ng Left 174mm (Sw38-40.5)',
         'Part number: 1529643',
         'Footrest Tube, Short',
         'Part number: 1434561-0010',
         'Screw Kit, Footrest Fixed',
         'Part number: 1430433',
         'Plug Ikpt 2017S',
         'Part number: 1424576'
      ]

      for i, string in enumerate(selected_result_output):
         ctk.CTkLabel(selected_result_frame, text=string, justify=ctk.LEFT).pack(side=ctk.TOP, anchor='w')

      # * Packing
      right_header.pack()
      detection_result_frame.pack(expand=True, fill='x')
      display_info_prompt.pack()
      component_selector_combo.pack()
      component_empty_label.pack()
      component_show_button.pack()
      selected_result_frame.pack(expand=True, fill='x', side='left')

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

ctk.set_default_color_theme('green')
app = App((1200, 720))