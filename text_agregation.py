from tkinter import END, TclError, WORD, NONE
from tkinter import messagebox
from tkinter import filedialog


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


current_file_path = ''
current_file_status = False

def change_wrap(text_field):
    if text_field['wrap'] == WORD:
        text_field['wrap'] = NONE
    else:
        text_field['wrap'] = WORD


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

def notepad_exit(root, text_field):
    global current_file_status

    if current_file_status:
        answer = messagebox.askyesno('Выход', 'Текущий фал сохранён. Вы уверены, что хотите выйти?')
        if answer:
            root.destroy()
        return

    answer = messagebox.askyesnocancel('Выход', 'Сохранить текущий файл?')
    if answer:
        success = save_file_as(text_field)
        if success:
            root.destroy()
        messagebox.showerror('Внимание!', 'Директория не выбрана - файл не был сохранён!')
    elif answer == False:
        root.destroy()


# Обработка открытия файла

def open_file(text_field):
    global current_file_path
    global current_file_status

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
        current_file_path = file_path
        current_file_status = False


# Обработка сохранения файла


def save_file(text_field):
    global current_file_path
    global current_file_status

    if current_file_path:
        f = open(current_file_path, 'w', encoding='utf-8')
        text = text_field.get('1.0', END)
        f.write(text)
        f.close()
        current_file_status = True


def save_file_as(text_field):
    global current_file_path
    global current_file_status

    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        f = open(file_path, 'w', encoding='utf-8')
        text = text_field.get('1.0', END)
        f.write(text)
        f.close()
        current_file_status = True
        current_file_path = file_path
        return True

    return False


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



