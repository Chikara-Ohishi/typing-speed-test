from word_container import WordContainer
from tkinter import *

COLOR1="#f0f5f9"
COLOR2="#c9d6df"
COLOR3="#52616b"
COLOR4="#1e2022"

BG_COLOR=COLOR1
FRAME_BG_COLOR=COLOR2
TEXT_COLOR1=COLOR3
TEXT_COLOR2=COLOR4
TEXT_COLOR3="#e84a5f"

FONT=("Helvetica", 40)
FONT_SMALL=("Helvetica", 20)

TYPING_SEC = 60

class TypingSpeedTestGUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Typing Speed Test")
        master.config(padx=30, pady=30, bg=BG_COLOR)
        master.bind('<Any-KeyPress>', self.key_press)
        self.pack()
        self.init_widget()

        self.init_message()
        self.state = 'initial'
        self.wc = WordContainer()

        self.input_string = ""
        self.wordlist = []
        self.timer = None
        self.n_char = 0
        self.n_char_ok = 0
        self.n_ok = 0
        self.n_ng = 0

    def init_widget(self):
        self.top_label = self.top_label = Label(width=40, fg=TEXT_COLOR1, bg=BG_COLOR, font=FONT_SMALL, anchor=W)
        self.top_label.pack()
        self.frame = Frame(width=400, height=300, bg=FRAME_BG_COLOR)
        self.frame.pack(fill=BOTH)
        self.input_label = Label(width=20, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT)
        self.input_label.pack(padx=10, pady=10)

        self.main_label = []
        for i in range(0, 5):
            self.main_label.append( Label(self.frame, fg=TEXT_COLOR1, bg=FRAME_BG_COLOR, font=FONT) )
            self.main_label[i].pack()

    def init_message(self):
        self.main_label[1].config(text="typing speed test for 60 sec.", fg=TEXT_COLOR1)
        self.main_label[2].config(text="press SPACE to start", fg=TEXT_COLOR1)
        self.input_label.config(text="input box", fg=TEXT_COLOR1)

    def key_press(self, event):
        if event.keysym == "Return":
            key = " "
        else:
            key = event.char
        # print(f"key pressed: keysym({event.keysym}), char({key})")

        if ( self.state == 'initial' and key == " ") or (self.state == 'result' and key == "n"):
            self.start_typing()

        elif self.state == 'typing':
            self.n_char += 1
            self.n_char_ok += 1
            if key == " ":
                self.finish_input_string()
            else:
                self.update_intput_string(key)

            header_text = f"Type Count: {self.n_char}, Correct Word: {self.n_ok}"
            self.top_label.config(text=header_text)

    def update_intput_string(self, char):
        self.input_string += char
        self.input_label.config(text=self.input_string, fg=TEXT_COLOR2)

        if len(self.input_string) <  len(self.wordlist[0]):
            if self.input_string != self.wordlist[0][:len(self.input_string)]:
                self.main_label[0].config(fg=TEXT_COLOR3)
        elif self.input_string == self.wordlist[0]:
            self.main_label[0].config(fg=TEXT_COLOR2)
        else:
            self.main_label[0].config(fg=TEXT_COLOR3)

    def finish_input_string(self):
        if self.input_string == self.wordlist[0]:
            self.count_ok()
        else:
            self.count_ng()

        self.input_string = ""
        self.input_label.config(text=self.input_string, fg=TEXT_COLOR2)

        self.wordlist.pop(0)
        self.wordlist.append(self.wc.get_next())
        self.update_main_label()

    def count_ok(self):
        print("count ok")
        self.n_ok += 1

    def count_ng(self):
        print("count ng")
        self.n_ng += 1
        self.n_char_ok -= len(self.input_string)

    def start_typing(self):
        self.n_char = 0
        self.n_char_ok = 0
        self.n_ok = 0
        self.n_ng = 0

        self.input_string = ""
        self.input_label.config(text=self.input_string, fg=TEXT_COLOR2)

        print("start typing")
        self.state = 'typing'
        self.wc.init_list()
        self.wordlist = []
        for i in range(0, 5):
            self.wordlist.append(self.wc.get_next())
        self.update_main_label()

        self.timer = super().after(TYPING_SEC*1000, self.time_up)

    def update_main_label(self):
        for i in range(0, 5):
            self.main_label[i].config(text=self.wordlist[i], fg=TEXT_COLOR1)

    def time_up(self):
        print("time up")
        super().after_cancel(self.timer)

        self.state = 'result'
        self.show_result()

    def show_result(self):
        self.main_label[0].config(text=f"Total Type Count: {self.n_char}", fg=TEXT_COLOR1)
        self.main_label[1].config(text=f"Correct Type Count: {self.n_char_ok}", fg=TEXT_COLOR1)
        self.main_label[2].config(text=f"Correct Word: {self.n_ok}", fg=TEXT_COLOR1)
        self.main_label[3].config(text=f"Incorrect Word: {self.n_ng}", fg=TEXT_COLOR1)
        self.main_label[4].config(text="press n to restart", fg=TEXT_COLOR1)
        self.input_label.config(text="input box", fg=TEXT_COLOR1)


root = Tk()
app = TypingSpeedTestGUI(master=root)
app.mainloop()
