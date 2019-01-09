import tkinter as tk
from convert_funcs import options, convert


class Conversion:
    """
    just a comment to check the github how it does work
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Conversion")
        w = 512
        h = 384
        self.root.geometry("+{}+{}".format(w, h))

        self.mode = tk.IntVar()
        self.mode.set(0)

        tk.Label(root, text="Choose your desired conversion unit:", justify=tk.LEFT, padx=20).pack()
        for num, parameter in enumerate(options):
            tk.Radiobutton(root,                            #набор словарей - к ключу name имя конвертируемого параметра
                           text=parameter['name'],
                           indicatoron=0,
                           width=20,
                           padx=20,
                           variable=self.mode,
                           command=self.set_mode,              # вызов функции
                           value=num).pack(anchor=tk.CENTER)
        self.mainFrame = tk.LabelFrame(root, text="Init")
        self.mainFrame.pack(side='top')

        frame_left = tk.Frame(self.mainFrame)
        frame_left.pack(side='left')                            # левый блок
        self.label_left = tk.Label(frame_left, text="Unit 1")
        self.label_left.pack(side='top')
        self.unit_one = tk.StringVar()
        self.unit_one.trace_add('write', lambda name, index, mode: self.compute_one())  # быстрая конвертация - как оптимизация кода
        self.entry_one = tk.Entry(frame_left, textvariable=self.unit_one)
        self.entry_one.pack(side='top')

        frame_center = tk.Frame(self.mainFrame)
        frame_center.pack(side='left')
        self.label_center = tk.Label(frame_center, text="Unit 2")
        self.label_center.pack(side='top')
        self.unit_two = tk.StringVar()
        self.unit_two.trace_add('write', lambda name, index, mode: self.compute_two())
        self.entry_two = tk.Entry(frame_center, textvariable=self.unit_two)
        self.entry_two.pack(side='top')

        frame_right = tk.Frame(self.mainFrame)
        frame_right.pack(side='left')
        self.label_right = tk.Label(frame_right, text="Unit 3")
        self.label_right.pack(side='top')
        self.unit_three = tk.StringVar()
        self.unit_three.trace_add('write', lambda name, index, mode: self.compute_three())
        self.entry_three = tk.Entry(frame_right, textvariable=self.unit_three)
        self.entry_three.pack(side='top')

        self.set_mode()                 # включение режим конвертации

    def set_mode(self):                         # функционал вызываемой функции
        mode_num = self.mode.get()
        self.mainFrame['text'] = options[mode_num]['name']
        self.label_left['text'] = options[mode_num]['units'][0]
        self.label_center['text'] = options[mode_num]['units'][1]
        self.label_right['text'] = options[mode_num]['units'][2]
        self.unit_one.set('')
        self.unit_two.set('')
        self.unit_three.set('')
        self.entry_one.focus_set()               # курсор в первый юнит и клавиша табуляции переключится

    def compute_one(self):                       # привязана к переменной в первой ячейки
        if self.root.focus_get() == self.entry_one:   #курсор на данном окне - иначе будут процесс изменения других переменных (будет конвертация)
            unit_one, unit_two, unit_three = convert(self.mode.get(), unit_one=self.unit_one.get()) # величины которые конвертируем в остальные два -
            self.unit_one.set(unit_one)          # после конвертации устанавливаем значение величины
            self.unit_two.set(unit_two)
            self.unit_three.set(unit_three)

    def compute_two(self):
        if self.root.focus_get() == self.entry_two:
            unit_one, unit_two, unit_three = convert(self.mode.get(), unit_two=self.unit_two.get())
            self.unit_one.set(unit_one)
            self.unit_two.set(unit_two)
            self.unit_three.set(unit_three)

    def compute_three(self):
        if self.root.focus_get() == self.entry_three:
            unit_one, unit_two, unit_three = convert(self.mode.get(), unit_three=self.unit_three.get())
            self.unit_one.set(unit_one)
            self.unit_two.set(unit_two)
            self.unit_three.set(unit_three)


root = tk.Tk()
conv = Conversion(root)
root.mainloop()
