from time import sleep
import pyautogui
import tkinter as tk
import random

root = tk.Tk()

#screen resolution
width = root.winfo_screenwidth() - 400 
height = root.winfo_screenheight() - 203

class Character():
    
    def __init__(self, pos_x, pos_y, pos_in_space_x):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_in_space_x = width
        root.geometry(f'{self.pos_x}x{self.pos_y}+{width}+{height}')
        
    def update_pos(self, walk_time, direction):
        
        idle = 0
        
        while walk_time > 0 and self.pos_in_space_x < width + 400 and self.pos_in_space_x > 0:
            
            if idle == 0:
                if direction == 1:
                    label.configure(image = stand_right)
                else:
                    label.configure(image = stand_left)
                idle = 1
            else:
                if direction == 1:
                    label.configure(image = walking_right)
                else:
                    label.configure(image = walking_left)
                idle = 0

            walk_time -= 1
            
            if direction == 1:
                self.pos_in_space_x += 4
            else:
                self.pos_in_space_x -= 4

            root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{height}')
            
            root.update()
            
            sleep(0.08)
    
    def event(self):
        
        event_number = random.randint(0, 6)
        
        if event_number == 0:
            label.configure(image = stand_right)
            
            sleep_time = random.randint(2, 3)
            
            sleep(sleep_time)
        elif event_number == 1:
            label.configure(image = stand_left)
            
            sleep_time = random.randint(2, 3)
            
            sleep(sleep_time)
        elif event_number == 2:
            label.configure(image = drinking_right)
            
            #sleep_time = random.randint(2, 3)
            
            sleep(2)
        elif event_number == 3:
            label.configure(image = drinking_left)
            
            #sleep_time = random.randint(2, 3)
            
            sleep(2)
        elif event_number == 4:
            label.configure(image = walking_right)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, 1)
            
        elif event_number == 5:
            label.configure(image = walking_left)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, -1)
            
   
character = Character(200, 200, width)        

char_gif = [tk.PhotoImage(file = "drinking_man_5.gif", format = 'gif -index %i' %(i))
            for i in range(6)]

stand_right = char_gif[0]
stand_left = char_gif[1]
drinking_right = char_gif[2]
drinking_left = char_gif[3]
walking_right = char_gif[4]
walking_left = char_gif[5]
           
root.config(highlightbackground='black')
label = tk.Label(root, bd = 0, bg = 'black')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','black')          

label.pack()

index = 0
start = 0

while 1:
    
    character.event()
        
    root.update()

root.mainloop()