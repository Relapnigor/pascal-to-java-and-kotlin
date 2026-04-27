import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame ,CTkEntry, CTkTextbox
from tkinter import filedialog, font

class ModernApp2():
    def __init__(self, grammar):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = CTk()
        self.app.geometry("1280x750")
        self.app.resizable(True, True)
        self.app.title("Pascal to Kotlin & Java app")
        self.grammar = grammar

        self.customFont = font.Font(family="Cascadia Code", size=16)
        self.tabWidth = self.customFont.measure(" " * 4)

        self.menu = CTkFrame(self.app)
        self.menu_config()
        self.menu.pack(fill="both", expand=True)

        self.notmenu = CTkFrame(self.app)
        self.notmenu_config()

    def run(self):
        self.app.mainloop()

    def menu_config(self):
        self.menu.grid_rowconfigure(0, pad=50)
        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_rowconfigure(2, pad=30)
        self.menu.grid_columnconfigure(0, weight=1)

        title = CTkLabel(self.menu, text="Pascal to Kotlin & Java", font=("Bauhaus 93", 60))
        title.grid(column = 0, row=0, sticky="nsew")

        self.textbox = CTkTextbox(self.menu, font=("Cascadia Code", 16), tabs = (self.tabWidth,), text_color = "gray30", state="disabled")
        self.textbox.grid(column = 0, row = 1, sticky="nsew", padx = 200, pady = 10)
        self.color_pascal_config()

        self.footerMenu = CTkFrame(self.menu)
        self.footerMenu.grid_rowconfigure(0, weight=1)
        self.footerMenu.grid_columnconfigure(0)
        self.footerMenu.grid_columnconfigure(1, weight=1)
        self.footerMenu.grid_columnconfigure(2, weight=1)

        button = CTkButton(self.footerMenu, text="Wczytaj plik", command=self.choose_file)
        button.grid(column = 0, row = 0, sticky="nsw",padx=50, pady=10)
        button2 = CTkButton(self.footerMenu, text="kompiluj", command=self.compile)
        button2.grid(column = 2, row = 0, sticky="nse", padx=50, pady=10)

        self.filepath = CTkLabel(self.footerMenu, text="",font=("arial", 14))
        self.filepath.grid(column = 1, row = 0, sticky="nsw", padx=10, pady=10)

        self.footerMenu.grid(column = 0, row = 2, sticky="nsew")

    def notmenu_config(self):
        self.notmenu.grid_columnconfigure(0, weight=1)
        self.notmenu.grid_rowconfigure(0)
        self.notmenu.grid_rowconfigure(1, weight=1)
        self.notmenu.grid_rowconfigure(2)

        self.header_notmenu = CTkFrame(self.notmenu)
        self.header_notmenu.grid(column=0, row=0, sticky="nsew")
        self.header_notmenu.grid_columnconfigure(0, weight=1)
        self.header_notmenu.grid_columnconfigure(1, weight=1)

        javatxt = CTkLabel(self.header_notmenu, text="Java", font=("arial", 18))
        javatxt.grid(column=1, row=0, sticky="nsw",padx=20)

        kotlintxt = CTkLabel(self.header_notmenu, text="Kotlin", font=("arial", 18))
        kotlintxt.grid(column=0, row=0, sticky="nsw",padx=20)

        self.mid_notmenu = CTkFrame(self.notmenu)
        self.mid_notmenu.grid(column = 0, row = 1, sticky="nsew")

        self.mid_notmenu.grid_columnconfigure(0, weight=1)
        self.mid_notmenu.grid_columnconfigure(1, weight=1)
        self.mid_notmenu.grid_rowconfigure(0, weight=1)


        self.javaFrame = CTkFrame(self.mid_notmenu)
        self.kotlinFrame = CTkFrame(self.mid_notmenu)

        self.javaFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.kotlinFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.textboxjava = CTkTextbox(self.javaFrame, font=("Cascadia Code", 16), tabs = (self.tabWidth,), state="disabled")
        self.textboxjava.pack(fill="both", expand=True)
        self.textboxkotlin = CTkTextbox(self.kotlinFrame, font=("Cascadia Code", 16), tabs = (self.tabWidth,), state="disabled")
        self.textboxkotlin.pack(fill="both", expand=True)

        self.footernotmenu = CTkFrame(self.notmenu)
        self.footernotmenu.grid(column=0, row=2, sticky="nsew")

        self.footernotmenu.grid_columnconfigure(0,weight=1)
        self.footernotmenu.grid_columnconfigure(1, weight=1)


        javaButton = CTkButton(self.footernotmenu, text="Download", command=self.download_java_file)
        javaButton.grid(column=1, row=0, sticky="nse", padx=20, pady=10)

        kotlinButton = CTkButton(self.footernotmenu, text="Download", command=self.download_kotlin_file)
        kotlinButton.grid(column=0, row=0, sticky="nse", padx=20, pady=10)

        backButton = CTkButton(self.footernotmenu, text="<-", command=self.go_back)
        backButton.grid(column=0, row=1, sticky="nsw", padx=10, pady=5)



    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki pascal", "*.pas")])
        print(f"plik: {file_path}")
        self.filepath.configure(text=str(file_path))
        if file_path:
            self.textbox.configure(state="normal")
            content = self.grammar.load(file_path)
            self.textbox.delete("1.0", "end")  # czyści pole
            self.textbox.insert("1.0", content)  # wstawia tekst
            self.color_pascal()
            self.textbox.configure(state="disabled")

    def color_pascal_config(self):
        self.textbox.tag_config("string", foreground="green")
        self.textbox.tag_config("numeric", foreground="cyan")
        self.textbox.tag_config("type", foreground="#167ef5")
        self.textbox.tag_config("word", foreground="white")
        self.textbox.tag_config("keyword", foreground="orange")


    def color_pascal(self):
        data = self.grammar.get_data()
        for token in self.grammar.get_tokens():
            self.textbox.tag_add(data[token[0]], f"{token[1]}.{token[2]}", f"{token[1]}.{token[3]}")

    def download_java_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".java")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                content = self.textboxjava.get(1.0, "end")
                f.write(content)

    def download_kotlin_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".kt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                content = self.textboxkotlin.get(1.0, "end")
                f.write(content)

    def compile(self):
        self.menu.pack_forget()
        self.notmenu.pack(fill="both", expand=True)

        self.grammar.make_tree()
        java_code = self.grammar.get_java()
        kotlin_code = self.grammar.get_kotlin()

        self.textboxjava.configure(state="normal")
        self.textboxkotlin.configure(state="normal")

        self.textboxjava.delete("1.0", "end")
        self.textboxjava.insert("1.0", java_code)

        self.textboxkotlin.delete("1.0", "end")
        self.textboxkotlin.insert("1.0", kotlin_code)

        self.textboxjava.configure(state="disabled")
        self.textboxkotlin.configure(state="disabled")

    def go_back(self):
        self.notmenu.pack_forget()
        self.menu.pack(fill="both", expand=True)
