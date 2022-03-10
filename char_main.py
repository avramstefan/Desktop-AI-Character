from time import sleep
import pyautogui
import tkinter as tk
import random
import winsound
import win32api

root = tk.Tk()
root.wm_attributes("-topmost", 1)

#screen resolution
main_width = root.winfo_screenwidth()
main_height = root.winfo_screenheight()
width = root.winfo_screenwidth() - 400 
height = root.winfo_screenheight() - 203

def option_set(choice):
    
    global option
    
    option = choice
        

class Drinking_man():
    
    def __init__(self, pos_x, pos_y, pos_in_space_x):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_in_space_x = width
        root.geometry(f'{self.pos_x}x{self.pos_y}+{width}+{height}')
        
    def update_pos(self, walk_time, direction):
        
        idle = 0
        
        while walk_time > 0 and self.pos_in_space_x < main_width and self.pos_in_space_x > 0:
            
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
        
        event_number = random.randint(0, 5)
        
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
            
            sleep(2)
        elif event_number == 3:
            label.configure(image = drinking_left)
            
            sleep(2)
        elif event_number == 4:
            label.configure(image = walking_right)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, 1)
            
        elif event_number == 5:
            label.configure(image = walking_left)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, -1)

class R2D2():
    
    def __init__(self, pos_x, pos_y, pos_in_space_x, pos_in_space_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_in_space_x = width
        self.pos_in_space_y = height
        root.geometry(f'{self.pos_x}x{self.pos_y}+{width}+{height}')
        
    def update_pos(self, do_time, direction):
    
        if direction == 0 or direction == 1:
        
            while do_time > 0 and self.pos_in_space_x < main_width and self.pos_in_space_x > 0:
                
                do_time -= 1
                
                if direction == 1: #right
                    self.pos_in_space_x += 4 
                elif direction == 0: #left
                    self.pos_in_space_x -= 4   

                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{height}')
                
                root.update()
                
                sleep(0.08)
                
        elif direction == 2:
            
            while do_time > 0 and self.pos_in_space_y < main_height and self.pos_in_space_y > 0:
                
                do_time -= 1
                
                self.pos_in_space_y -= 50
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
            #after fly -> going down
            label.configure(image = stand)
            
            while self.pos_in_space_y < height:
                
                self.pos_in_space_y += 50
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
        elif direction == 3:
            
            while do_time > 0 and self.pos_in_space_y < main_height and self.pos_in_space_y > 0 and self.pos_in_space_x > 300 :
                
                do_time -= 1
                
                self.pos_in_space_y -= 50
                self.pos_in_space_x -= 20
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
            #after fly -> going down
            label.configure(image = stand)
            
            while self.pos_in_space_y < height and self.pos_in_space_x > 300:
                
                self.pos_in_space_y += 50
                self.pos_in_space_x -= 20
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
        elif direction == 4:
            
            while do_time > 0 and self.pos_in_space_y < main_height and self.pos_in_space_y > 0 and self.pos_in_space_x < width :
                
                do_time -= 1
                
                self.pos_in_space_y -= 50
                self.pos_in_space_x += 20
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
            #after fly -> going down
            label.configure(image = stand)
            
            while self.pos_in_space_y < height and self.pos_in_space_x < width:
                
                self.pos_in_space_y += 50
                self.pos_in_space_x += 20
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
        
    def event(self):
        
        event_number = random.randint(0, 5)

        if event_number == 0:
            label.configure(image = stand)
            
            sleep_time = random.randint(2, 3)
            
            sleep(sleep_time)
        elif event_number == 1:
            label.configure(image = left)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, 0)
        elif event_number == 2:
            label.configure(image = right)
            
            walk_time = random.randint(7, 12)
            
            self.update_pos(walk_time, 1)
        elif event_number == 3:
            label.configure(image = stand_fly)
            
            fly_time = random.randint(7, 12)
            
            self.update_pos(fly_time, 2)
        elif event_number == 4:
            label.configure(image = left_fly)
            
            fly_time = random.randint(7, 12)
            
            self.update_pos(fly_time, 3)
        else:
            label.configure(image = right_fly)
            
            fly_time = random.randint(7, 12)
            
            self.update_pos(fly_time, 4)
            
class RockSinger():
    
    def __init__(self, pos_x, pos_y, pos_in_space_x, pos_in_space_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_in_space_x = width
        self.pos_in_space_y = height
        root.geometry(f'{self.pos_x}x{self.pos_y}+{width}+{height}')
        
    def update_pos(self, do_time, direction):
        
        x_range = random.randint(200, 300) // (2 * do_time)
        
        if direction < 0 and self.pos_in_space_x < main_width and self.pos_in_space_x > 300:
            
            while do_time > 0:
                
                do_time -= 1
                
                self.pos_in_space_y -= 10
                self.pos_in_space_x -= x_range
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
            while self.pos_in_space_y < height:
                
                self.pos_in_space_y += 10
                self.pos_in_space_x -= x_range
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
        elif direction > 0 and self.pos_in_space_x < main_width - 300 and self.pos_in_space_x > 0:
            
            while do_time > 0:
                    
                do_time -= 1
                
                self.pos_in_space_y -= 10
                self.pos_in_space_x += x_range
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)
                
            while self.pos_in_space_y < height:
                
                self.pos_in_space_y += 10
                self.pos_in_space_x += x_range
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                
                sleep(0.1)

    def singing_frequency(self, do_time, move, side):
        
        while do_time > 0:
            
            do_time -= 1

            if move:
                
                if side == 1:
                    label.configure(image = stand_right_1)  
                else: 
                    label.configure(image = stand_left_1)
                root.update() 
                sleep(0.13)  
                move = 0
            else:  
                if side == 1: 
                    label.configure(image = stand_right_2)  
                else:     
                    label.configure(image = stand_left_2)
                root.update() 
                sleep(0.13)   
                move = 1      
                
    def mouse_condition(self):
        
        mouse_pos_x, mouse_pos_y = pyautogui.position()
        
        condition_a = False
        condition_b = False
        
        if mouse_pos_x >= self.pos_in_space_x and mouse_pos_x <= self.pos_in_space_x + 200:
            condition_a = True
            
        if  mouse_pos_y <= self.pos_in_space_y + 200 and mouse_pos_y >= self.pos_in_space_y:
            condition_b = True
            
        if condition_a and condition_b:
            return True
        return False
     
    def move_the_char(self):
         
        mouse_pressed = win32api.GetKeyState(0x01) 
        has_been_pressed = False

        while mouse_pressed < 0:
            
            has_been_pressed = True
            
            mouse_pos_x, mouse_pos_y = pyautogui.position()
            
            self.pos_in_space_x = mouse_pos_x
            self.pos_in_space_y = mouse_pos_y
            
            root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
            
            root.update()
            
            sleep(0.001)
            
            mouse_pressed = win32api.GetKeyState(0x01)
            
        if has_been_pressed == True:
             
            while self.pos_in_space_y + 60 < main_height - 200:
                
                self.pos_in_space_y += 60
                
                root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
                root.update()
                sleep(0.05)
            
            self.pos_in_space_y = main_height - 200
            
            root.geometry(f'{self.pos_x}x{self.pos_y}+{self.pos_in_space_x}+{self.pos_in_space_y}')
                
            root.update()
        
    def event(self):
        
        if self.mouse_condition():
            self.move_the_char()
                
        event_number =  random.randint(0, 2)
        
        if event_number == 0:
            do_time = random.randint(9, 10)
            move = random.randint(0, 1)
            
            self.singing_frequency(do_time, move, 1)
        elif event_number == 1:
            do_time = random.randint(9, 10)
            move = random.randint(0, 1)
            
            self.singing_frequency(do_time, move, 0)
        elif event_number == 2:
            
            case = random.randint(0, 1)
            
            if case:
            
                label.configure(image = jump_right)
                
                jump_time = random.randint(3, 4)
                
                self.update_pos(jump_time, 1)
                
            else:
                
                label.configure(image = jump_left)
            
                jump_time = random.randint(3, 4)
                
                self.update_pos(jump_time, -1)

option = -1
start = 1

while 1:
    
    if option < 0:
        
        root.geometry('900x908+500+0')
        
        bg_photo = tk.PhotoImage(file = "start_bg.png")

        bg_label = tk.Label(root, image = bg_photo)
        bg_label.image = bg_photo
        bg_label.pack()
        
        button_1 = tk.Button(root, text = "Drinking man", padx = 20,
                        pady = 3, fg = "white", bg = "dark red", command = lambda : option_set(1))
        button_1.place(x = 370, y = 320)
        
        button_2 = tk.Button(root, text = "R2D2", padx = 20,
                        pady = 3, fg = "white", bg = "dark red", command = lambda : option_set(2))
        button_2.place(x = 395, y = 360)

        button_3 = tk.Button(root, text = "Rock Singer", padx = 20,
                        pady = 3, fg = "white", bg = "dark red", command = lambda : option_set(3))
        button_3.place(x = 374, y = 400)
        
        while option < 0:
            
            root.update()

        bg_label.destroy()
            
    else:
        
        if start:
         
            root.config(highlightbackground='black')
            label = tk.Label(root, bd = 0, bg = 'black')
            root.overrideredirect(True)
            root.wm_attributes('-transparentcolor','black')          

            label.pack()
            
            start = 0
    
            if option == 1:
                
                char_gif = [tk.PhotoImage(file = "drinking_man_5.gif", format = 'gif -index %i' %(i))
                    for i in range(6)]
                
                character = Drinking_man(200, 200, width) 
                
                stand_right = char_gif[0]
                stand_left = char_gif[1]
                drinking_right = char_gif[2]
                drinking_left = char_gif[3]
                walking_right = char_gif[4]
                walking_left = char_gif[5]
                
            elif option == 2:
                
                char_gif = [tk.PhotoImage(file = "r2d2.gif", format = 'gif -index %i' %(i))
                    for i in range(6)]
                
                character = R2D2(200, 200, width, height) 
                
                stand = char_gif[0]
                left = char_gif[1]
                right = char_gif[2]
                stand_fly = char_gif[3]
                left_fly = char_gif[4]
                right_fly = char_gif[5]
                
            elif option == 3:
                
                char_gif = [tk.PhotoImage(file = "rocker_singing.gif", format = 'gif -index %i' %(i))
                    for i in range(6)]
                
                character = RockSinger(200, 200, width, height)
                
                stand_right_1 = char_gif[0]
                stand_left_1 = char_gif[1]
                jump_right = char_gif[2]
                jump_left = char_gif[3]
                stand_right_2 = char_gif[4]
                stand_left_2 = char_gif[5]
                
                winsound.PlaySound("rocksinger_guitar.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)
            
        character.event()
        
        root.update()

root.mainloop()
