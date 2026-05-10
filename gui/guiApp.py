import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame ,CTkEntry, CTkTextbox
from tkinter import filedialog, font

class GuiApp:
    def __init__(self, grammar):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = CTk()
        self.app.geometry("1280x750")
        self.app.resizable(True, True)
        self.app.title("Pascal to Kotlin & Java app")

        self.customFont = font.Font(family="Cascadia Code", size=16)
        self.tabWidth = self.customFont.measure(" " * 4)

        self.inputPage = CTkFrame(self.app)
        self.input_page_config()
        self.inputPage.pack(fill="both", expand=True)

        self.outputPage = CTkFrame(self.app)
        self.output_page_config()
        
        self.grammar = grammar

    def run(self):
        self.app.mainloop()

    def input_page_config(self):
        self.inputPage.grid_rowconfigure(0, pad=50)
        self.inputPage.grid_rowconfigure(1, weight=1)
        self.inputPage.grid_rowconfigure(2, pad=30)
        self.inputPage.grid_columnconfigure(0, weight=1)

        self.footerInputPage = CTkFrame(self.inputPage)

        self.footerInputPage.grid_rowconfigure(0, weight=1)
        self.footerInputPage.grid_columnconfigure(0)
        self.footerInputPage.grid_columnconfigure(1, weight=1)
        self.footerInputPage.grid_columnconfigure(2, weight=1)

        title = CTkLabel(self.inputPage, text="Pascal to Kotlin & Java", font=("Bauhaus 93", 60))
        self.textboxPascal = CTkTextbox(self.inputPage, font=("Cascadia Code", 16), tabs = (self.tabWidth,), text_color ="gray30")
        selectFileButton = CTkButton(self.footerInputPage, text="Wczytaj plik", command=self.choose_file)
        compileButton = CTkButton(self.footerInputPage, text="kompiluj", command=self.compile)
        self.filepathText = CTkLabel(self.footerInputPage, text="", font=("arial", 14))

        self.color_pascal_config()
        self.textboxPascal.bind("<KeyRelease>", self.entry_change)

        title.grid(column = 0, row=0, sticky="nsew")
        self.textboxPascal.grid(column = 0, row = 1, sticky="nsew", padx = 200, pady = 10)
        selectFileButton.grid(column = 0, row = 0, sticky="nsw",padx=50, pady=10)
        compileButton.grid(column = 2, row = 0, sticky="nse", padx=50, pady=10)
        self.filepathText.grid(column = 1, row = 0, sticky="nsw", padx=10, pady=10)
        self.footerInputPage.grid(column = 0, row = 2, sticky="nsew")


    def output_page_config(self):
        self.outputPage.grid_columnconfigure(0, weight=1)
        self.outputPage.grid_rowconfigure(0)
        self.outputPage.grid_rowconfigure(1, weight=1)
        self.outputPage.grid_rowconfigure(2)

        self.headerOutputPage = CTkFrame(self.outputPage)
        self.bodyOutputPage = CTkFrame(self.outputPage)
        self.footerOutputPage = CTkFrame(self.outputPage)

        self.headerOutputPage.grid(column=0, row=0, sticky="nsew")
        self.headerOutputPage.grid_columnconfigure(0, weight=1)
        self.headerOutputPage.grid_columnconfigure(1, weight=1)

        self.bodyOutputPage.grid_columnconfigure(0, weight=1)
        self.bodyOutputPage.grid_columnconfigure(1, weight=1)
        self.bodyOutputPage.grid_rowconfigure(0, weight=1)

        self.footerOutputPage.grid_columnconfigure(0, weight=1)
        self.footerOutputPage.grid_columnconfigure(1, weight=1)

        self.javaFrame = CTkFrame(self.bodyOutputPage)
        self.kotlinFrame = CTkFrame(self.bodyOutputPage)


        javatxt = CTkLabel(self.headerOutputPage, text="Java", font=("arial", 18))
        kotlintxt = CTkLabel(self.headerOutputPage, text="Kotlin", font=("arial", 18))
        self.textboxJava = CTkTextbox(self.javaFrame, font=("Cascadia Code", 16), tabs = (self.tabWidth,), state="disabled")
        self.textboxKotlin = CTkTextbox(self.kotlinFrame, font=("Cascadia Code", 16), tabs = (self.tabWidth,), state="disabled")
        javaButton = CTkButton(self.footerOutputPage, text="Download", command=self.download_java_file)
        kotlinButton = CTkButton(self.footerOutputPage, text="Download", command=self.download_kotlin_file)
        backButton = CTkButton(self.footerOutputPage, text="<-", command=self.go_back)

        self.color_kotlin_config()

        javatxt.grid(column=1, row=0, sticky="nsw",padx=20)
        kotlintxt.grid(column=0, row=0, sticky="nsw",padx=20)
        self.bodyOutputPage.grid(column = 0, row = 1, sticky="nsew")
        self.javaFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.kotlinFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.textboxJava.pack(fill="both", expand=True)
        self.textboxKotlin.pack(fill="both", expand=True)
        self.footerOutputPage.grid(column=0, row=2, sticky="nsew")
        javaButton.grid(column=1, row=0, sticky="nse", padx=20, pady=10)
        kotlinButton.grid(column=0, row=0, sticky="nse", padx=20, pady=10)
        backButton.grid(column=0, row=1, sticky="nsw", padx=10, pady=5)



    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki pascal", "*.pas")])
        print(f"plik: {file_path}")
        self.filepathText.configure(text=str(file_path))
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.textboxPascal.delete("1.0", "end")  # czyści pole
            self.textboxPascal.insert("1.0", content)  # wstawia tekst
            self.color_pascal(content)

    def entry_change(self, event = None):
        for tag in self.textboxPascal.tag_names():
            self.textboxPascal.tag_remove(tag, "1.0", "end")

        text = self.textboxPascal.get("1.0", "end")
        self.color_pascal(text)


    def color_pascal_config(self):
        self.textboxPascal.tag_config("STRING", foreground="green")
        self.textboxPascal.tag_config("NUMBER", foreground="cyan")
        self.textboxPascal.tag_config("TYPE", foreground="#167ef5")
        self.textboxPascal.tag_config("WORD", foreground="white")
        self.textboxPascal.tag_config("KEYWORD", foreground="orange")


    def color_kotlin_config(self):
        self.textboxKotlin.tag_config("STRING", foreground="green")
        self.textboxKotlin.tag_config("KEYWORD", foreground="orange")
        self.textboxKotlin.tag_config("NUMBER", foreground="cyan")
        self.textboxKotlin.tag_config("TYPE", foreground="#167ef5")


    def color_pascal(self, content):
        for token in self.grammar.get_pascal_tokens(content):
            self.textboxPascal.tag_add(token[0], f"{token[1]}.{token[2]}", f"{token[1]}.{token[3]}")

    def color_kotlin(self, content):
        for token in self.grammar.get_kotlin_tokens(content):
            self.textboxKotlin.tag_add(token[0], f"{token[1]}.{token[2]}", f"{token[1]}.{token[3]}")


    def download_java_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".java")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                content = self.textboxJava.get(1.0, "end")
                f.write(content)

    def download_kotlin_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".kt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                content = self.textboxKotlin.get(1.0, "end")
                f.write(content)

    def compile(self):
        self.inputPage.pack_forget()
        self.outputPage.pack(fill="both", expand=True)

        text = self.textboxPascal.get("1.0", "end")
        self.grammar.make_tree(text)

        java_code = self.grammar.get_java()
        kotlin_code = self.grammar.get_kotlin()

        self.textboxJava.configure(state="normal")
        self.textboxKotlin.configure(state="normal")

        self.textboxJava.delete("1.0", "end")
        self.textboxJava.insert("1.0", java_code)

        self.textboxKotlin.delete("1.0", "end")
        self.textboxKotlin.insert("1.0", kotlin_code)

        self.color_kotlin(kotlin_code)

        self.textboxJava.configure(state="disabled")
        self.textboxKotlin.configure(state="disabled")

    def go_back(self):
        self.outputPage.pack_forget()
        self.inputPage.pack(fill="both", expand=True)
