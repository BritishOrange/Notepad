from tkinter import *
import text_agregation as ta
import finding_window_agregation as fwa


class Notepad:
    def __init__(self):
        self.root = Tk()
        self.root.title('Текстовый редактор')
        self.root.geometry('600x700')

        self.main_menu = Menu(self.root)
        # Файл
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='Открыть', command=lambda: ta.open_file(self.text_field))
        self.file_menu.add_command(label='Сохранить', command=lambda: ta.save_file(self.text_field))
        self.file_menu.add_command(label='Сохранить как...', command=lambda: ta.save_file_as(self.text_field))
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Закрыть', command=lambda: ta.notepad_exit(self.root, self.text_field))
        self.root.config(menu=self.file_menu)

        # Вид

        self.view_menu = Menu(self.main_menu, tearoff=0)
        self.view_menu_sub = Menu(self.view_menu, tearoff=0)
        self.font_menu_sub = Menu(self.view_menu, tearoff=0)
        self.view_menu_sub.add_command(label='Тёмная', command=lambda: ta.change_theme('dark', self.text_field))
        self.view_menu_sub.add_command(label='Светлая', command=lambda: ta.change_theme('light', self.text_field))
        self.view_menu.add_cascade(label='Тема', menu=self.view_menu_sub)

        self.font_menu_sub.add_command(label='Arial', command=lambda: ta.change_fonts('Arial', self.text_field))
        self.font_menu_sub.add_command(label='Comic Sans MS', command=lambda: ta.change_fonts('CSMS', self.text_field))
        self.font_menu_sub.add_command(label='Times New Roman', command=lambda: ta.change_fonts('TNR', self.text_field))
        self.view_menu.add_cascade(label='Шрифт...', menu=self.font_menu_sub)
        self.root.config(menu=self.view_menu)

        # Добавление списков меню
        self.main_menu.add_cascade(label='Файл', menu=self.file_menu)
        self.main_menu.add_cascade(label='Вид', menu=self.view_menu)
        self.main_menu.add_cascade(label='Режим переноса слов', command=lambda: ta.change_wrap(self.text_field))
        self.main_menu.add_command(label='Найти подстроку', command=lambda: fwa.call_finding_menu(self.text_field))
        self.root.config(menu=self.main_menu)

        # Добавление контекстного меню

        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Копировать", command=lambda: ta.copy(self.text_field, self.root))
        self.context_menu.add_command(label="Вставить", command=lambda: ta.paste(self.text_field, self.root))
        self.context_menu.add_command(label="Вырезать", command=lambda: ta.cut(self.text_field, self.root))

        self.f_text = Frame(self.root)
        self.f_text.pack(fill=BOTH, expand=1)

        self.text_field = Text(self.f_text,
                               bg='white',
                               fg='black',
                               padx=10,
                               pady=10,
                               wrap=NONE,
                               insertbackground='black',
                               selectbackground='#8D917A',
                               spacing3=10,
                               width=30,
                               font='Arial 14 bold'
                               )
        self.text_field.pack(expand=1, fill=BOTH, side=LEFT)

        # Скролл бар

        self.scroll = Scrollbar(self.f_text, command=self.text_field.yview)
        self.scroll.pack(side=LEFT, fill=Y)
        self.text_field.config(yscrollcommand=self.scroll.set)

        # Обработка нажатия пкм
        self.text_field.bind("<ButtonRelease-3>",
                             lambda e, tf=self.text_field, cm=self.context_menu: ta.call_context_menu(e, tf, cm))

        self.root.protocol('WM_DELETE_WINDOW', lambda a=self.root, b=self.text_field: ta.notepad_exit(a, b))



