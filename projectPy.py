from tkinter import *
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x650')
        self.root.title('هنرستان موسیقی پسران')
        self.root.configure(bg='#3F4E4F')
        self.root.resizable(False, False)
        first_name = StringVar()
        last_name = StringVar()
        class_code = StringVar()
        group = StringVar()
        saz = StringVar()
        master_name = StringVar()


        # Frames
        main_frame = Frame(self.root, bg='#3F4E4F')
        main_frame.place(relwidth=1, relheight=1)

        right_frame = Frame(main_frame, bd=2, padx=30, pady=0, bg="#3F4E4F")
        right_frame.pack(side=RIGHT, fill=Y)

        self.title_label = Label(right_frame, font=('sepahbod ghasem soleymani', 22, 'bold'), text='هنرستان موسیقی پسران', fg='#C0C78C', bg='#3F4E4F', padx=0)
        self.title_label.grid()

        left_frame = Frame(main_frame, bg='#DCD7C9', width=1110, height=650, padx=0, pady=0)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Treeview
        tv = ttk.Treeview(left_frame, columns=(1, 2, 3, 4, 5, 6))
        tv.heading("#0", text='شماره ردیف', anchor=W)
        tv.heading(6, text='نام', anchor=W)  # Column for row number
        tv.heading(5, text='نام خانوادگی', anchor=W)
        tv.heading(4, text='کلاس', anchor=W)
        tv.heading(3, text='گروه', anchor=W)
        tv.heading(2, text='ساز', anchor=W)
        tv.heading(1, text='نام استاد', anchor=W)

        # Set column width
        tv.column(6, width=200)
        tv.column(5, width=120)
        tv.column(4, width=120)
        tv.column(3, width=80)
        tv.column(2, width=120)
        tv.column(1, width=120)
        tv.pack(fill=BOTH, expand=True)

        # Labels and Entry
        self.first_name_label = Label(right_frame, text='نام', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.first_name_label.place(x=300, y=70)
        self.first_name_Entry = Entry(right_frame, textvariable=first_name, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.first_name_Entry.place(x=10, y=70)

        self.last_name_label = Label(right_frame, text='نام خانوادگی', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.last_name_label.place(x=205, y=130)
        self.last_name_Entry = Entry(right_frame, textvariable=last_name, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.last_name_Entry.place(x=10, y=130)

        self.class_code_label = Label(right_frame, text='کلاس', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.class_code_label.place(x=275, y=190)
        self.class_code_Entry = Entry(right_frame, textvariable=class_code, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.class_code_Entry.place(x=10, y=190)

        self.group_label = Label(right_frame, text='گروه', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.group_label.place(x=280, y=250)
        self.group_Entry = Entry(right_frame, textvariable=group, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.group_Entry.place(x=10, y=250)

        self.saz_label = Label(right_frame, text='ساز', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.saz_label.place(x=285, y=315)
        self.saz_Entry = Entry(right_frame, textvariable=saz, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.saz_Entry.place(x=10, y=315)

        self.master_name_label = Label(right_frame, text='نام استاد', font=('b yekan', 18, 'bold'), bg='#3F4E4F', fg='#E8DFCA')
        self.master_name_label.place(x=245, y=380)
        self.master_name_Entry = Entry(right_frame, textvariable=master_name, font=('b yekan', 15, 'bold'), bg='white', fg='#33372C', width=12)
        self.master_name_Entry.place(x=10, y=380)

        # Buttons
        self.add_btn = Button(right_frame, text="اضافه کنید", bg='#6196A6', fg='white', font=('Lalezar', 15, 'bold'), width=12, height=1,
                              highlightthickness=1, highlightcolor='white', relief=RIDGE)
        self.add_btn.place(x=20, y=450)

        self.remove_btn = Button(right_frame, text="حذف کنید", bg='#750E21', fg='white', font=('Lalezar', 15, 'bold'),
                              width=12, height=1, highlightthickness=1, highlightcolor='white', relief=RIDGE)
        self.remove_btn.place(x=180, y=450)

        self.search_btn = Button(right_frame, text="جستجو کنید", bg='#FFB534', fg='white', font=('Lalezar', 15, 'bold'),
                                 width=12, height=1, highlightthickness=1, highlightcolor='white', relief=RIDGE)
        self.search_btn.place(x=180, y=515)

        self.update_btn = Button(right_frame, text="به روزرسانی کنید", bg='#6D5D6E', fg='white', font=('Lalezar', 15, 'bold'),
                                 width=12, height=1, highlightthickness=1, highlightcolor='white', relief=RIDGE)
        self.update_btn.place(x=20, y=515)


if __name__ == "__main__":
    root = Tk()
    application = Application(root)
    root.mainloop()