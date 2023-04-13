from tkinter import *
import text_finder as tf


class FindingWindow:
    def __init__(self, text_field):
        self.root = Toplevel()
        self.root.title('Поиск подстроки')
        self.root.geometry('150x100')
        self.entry = Entry(self.root, bd=5)
        self.entry.pack(anchor=NW, padx=6, pady=15)

        self.btn = Button(self.root, text="Найти", command=lambda: tf.check_correct(self.entry, text_field))
        self.btn.pack(anchor=NW, padx=50, pady=6)
