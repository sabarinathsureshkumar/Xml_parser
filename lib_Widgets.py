from tkinter import *
from tkinter import filedialog

main_window = Tk()


class CreateWidget:
    """Create Main Window Widget"""

    def __init__(self, **kwargs):
        print(kwargs.keys())
        self.widget = kwargs['widget_type']
        self.title = kwargs['title']
        self.iconimg = kwargs['iconimg']
        self.geometry = kwargs['geometry']
        self.bg = kwargs['bg']

    def create_mainwindow(self):
        main_window.title(self.title)
        main_window.iconbitmap(self.iconimg)
        main_window.geometry(self.geometry)
        main_window.configure(bg=self.bg)


class CreateLabel:
    """Create Label widget"""

    def __init__(self, **kwargs):
        self.text = kwargs['text']
        self.row = kwargs['row']
        self.bg = kwargs['bg']

    def create_inputlabel(self):
        Label(main_window, text=self.text, bg=self.bg).grid(row=self.row)


class CreateTextbox:
    """Create Testbox widget"""

    def __init__(self, **kwargs):
        self.row = kwargs['row']
        self.column = kwargs['column']
        self.text = kwargs['text']
        self.width = kwargs['width']
        ent = Entry(main_window, font=6, width=self.width)
        ent.grid(row=self.row, column=self.column)
        ent.insert(END, self.text)

    def create_inputtext(self):
        Entry(main_window).grid(row=self.row, column=self.column)
        Entry(main_window).insert(1, "test1")
        print("OBJ")
        print(self.text)


class CreateButtons:
    """Create Button widget"""

    def __init__(self, **kwargs):
        self.text = kwargs['text']
        self.command = kwargs['command']
        self.row = kwargs['row']
        self.column = kwargs['column']

    def create_button(self):
        Button(main_window, text=self.text, command=self.command).place(x=self.row,y=self.column)#grid(row=self.row, column=self.column)

    def browse_file(self):
        if self.command == 'browse_file':
            main_window.filename = filedialog.askopenfilename\
                (title="Selectarxml file", filetypes=(("xml files", "*.xml"), ("all files", "*.*")))
            Entry(main_window).delete('0')
            Entry(main_window).insert('0', main_window.filename)
