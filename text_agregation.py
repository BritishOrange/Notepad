from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from finding_window_ui import FindingWindow

# Словарь цветовых тем приложения
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

# Словарь шрифтов
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}


# Смена темы приложения (темная/светлая)

def change_theme(theme, text_field):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']


# Обработка смены шрифта в панели

def change_fonts(font_id, text_field):
    text_field['font'] = fonts[font_id]['font']


# Выход из приложения (окно с подтверждением)

def notepad_exit(root):
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


# Обработка открытия файла

def open_file(text_field):
    file_path = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        with open(file_path, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                text_field.insert(END, line)


# Обработка сохранения файла

def save_file(text_field):
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()


# Обработка "Вырезать" контекстоного меню

def cut(text_field, root):
    try:
        text_to_clipboard = text_field.get("sel.first", "sel.last")
    except TclError:
        print("Выделенной области нет")
        text_to_clipboard = ""
    root.clipboard_clear()
    root.clipboard_append(text_to_clipboard)
    text_field.delete('sel.first', 'sel.last')


# Обработка "Копировать" контекстоного меню

def copy(text_field, root):
    try:
        text_to_clipboard = text_field.get("sel.first", "sel.last")
    except TclError:
        print("Выделенной области нет")
        text_to_clipboard = ""
    root.clipboard_clear()
    root.clipboard_append(text_to_clipboard)


# Обработка "Вставить" контекстоного меню

def paste(text_field, root):
    try:
        text_field.insert("insert", root.clipboard_get())
    except TclError:
        print("Буфер обмена пуст")


# Вызов контекстоного меню (на пкм)

def call_context_menu(event, text_field, context_menu):
    pos_x = text_field.winfo_rootx() + event.x
    pos_y = text_field.winfo_rooty() + event.y
    context_menu.tk_popup(pos_x, pos_y)


# Вызов меню поиска
def call_finding_menu(text_f):
    window = FindingWindow(text_f)
    window.root.mainloop()
