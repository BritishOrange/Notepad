Привет ^_^

Это текстовый редактор, который поддерживает:
@ создание/открытие/сохранение текстовых файлов,
@ возможность смены темы приложения
@ изменение шрифтов
@ поиск подстрок внутри файла - результат выделяется жёлтым
@ позволяет считывать файл в память построчно


Что же творится в фалах:

main.py - обычный мэйник, все запускает

notepad_ui.py - внутри интерфейс самого блокнота, класс Notepad. Всё реализовано с помошью Tkinter
создал окно, сверху панель, некоторые кнопки с уровнем вложенности, скролл бар, контекстное меню на пкм, все дела...

finding_window.py - тоже интерфейс, но уже для окна поиска 

text_finder.py - содержит все вспомогателные функции, которые используются для поиска и разметки данных, а также на проверку корректности ввода (пока только непустая строка)

text_agregation.py - методы обработки почти всего взаимодействия с пользователем:

@chande_theme/fonts - меняет темы и шрифт - реакция на соотв. кнопки в панели
@notepad_exit - выход из приложение с диалоговым окном подтверждения
@open_file - предлагаем выбрать директорию и в удачном случае открываем файл - считывание построчно
@save_file - сохраняем файл с указанным именем
@cut/copy/paste - (-_-)
@call_context/finding_menu - отображают контекстное менб при нажатии пкм и меню поиска по кнопке


finding_window_agregation - запуск окна поиска и его прерывание

example.txt - текстовик с песенкой London Dridge is falling down - если надо поиграться с редактором 

Как-то так <3

