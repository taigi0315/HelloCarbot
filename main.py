import os
import cv2
from tkinter import *
from PIL import Image, ImageTk

class FullScreenWindow:

    def __init__(self):
        self.dir = os.path.dirname(__file__)
        self.rel_path = "assets/background.jpg"

        self.window = Tk()
        self.window.geometry('350x200')
        self.window.title('Hello Carbot')
        self.window.configure(background='black')

        # Background Setup
        self.image = Image.open("assets/background.jpg")
        self.image_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self.window, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.state = False
        self.window.bind('<Return>', self.toggle_fullscreen)
        self.window.bind('<Escape>', self.end_fullscreen)

        self.window.attributes('-fullscreen', self.state)


    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.window.attributes('-fullscreen', self.state)
        return 'break'

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes('-fullscreen', False)
        return 'break'
    
    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.image_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)



if __name__ == '__main__':
    w = FullScreenWindow()
    w.window.mainloop()

