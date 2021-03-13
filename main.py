import random

from tkinter import *

class WordContainer:
    def __init__(self):
        self.word_list = None
        with open("frequent_words_1-2000.txt") as file:
            self.word_list = file.read().splitlines()
        self.init_list()

    def init_list(self):
        random.shuffle(self.word_list)


COLOR1="#f0f5f9"
COLOR2="#c9d6df"
COLOR3="#52616b"
COLOR4="#1e2022"

BG_COLOR=COLOR1
FRAME_BG_COLOR=COLOR2
TEXT_COLOR1=COLOR3
TEXT_COLOR2=COLOR4
TEXT_COLOR3="#e84a5f"

FONT=("Cuurier", 40)

class TypingSpeedTestGUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Typing Speed Test")
        master.config(padx=30, pady=30, bg=BG_COLOR)
        master.bind('<Any-KeyPress>', self.key_press)
        self.pack()
        self.init_widget()
        self.init_message()

        self.input_string = ""


    def init_widget(self):
        self.frame = Frame(width=400, height=300, bg=FRAME_BG_COLOR)
        self.frame.pack(fill=BOTH)
        self.input_label = Label(width=20, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.input_label.pack(padx=10, pady=10)

        self.main_label1 = Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.main_label1.pack()
        self.main_label2 = Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.main_label2.pack()
        self.main_label3 = Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.main_label3.pack()
        self.main_label4 = Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.main_label4.pack()
        self.main_label5 = Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.main_label5.pack()

    def init_message(self):
        self.main_label1.config(text="typing speed test for 60 sec.", fg=TEXT_COLOR1)
        self.main_label2.config(text="press SPACE to start", fg=TEXT_COLOR1)
        self.input_label.config(text="input box", fg=TEXT_COLOR1)

    def key_press(self, event):
        if event.keysym == "Return":
            key = " "
        else:
            key = event.char
        print(f"key pressed: keysym({event.keysym}), char({key})")
        if key == " ":
            self.finish_input_string()
        else:
            self.update_intput_string(key)

    def update_intput_string(self, char):
        self.input_string += char
        self.input_label.config(text=self.input_string, fg=TEXT_COLOR2)

    def finish_input_string(self):
        self.input_string = ""
        self.input_label.config(text="input box", fg=TEXT_COLOR1)

root = Tk()
app = TypingSpeedTestGUI(master=root)
app.mainloop()
