import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

class NotepadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bloco de Notas")
        self.textarea = scrolledtext.ScrolledText(self.master, wrap=tk.WORD)
        self.textarea.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_command(label="Salvar como...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.exit_app)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(1.0, content)

    def save_file(self):
        content = self.textarea.get(1.0, tk.END)
        if not content.strip():
            messagebox.showerror("Erro", "Não há conteúdo para salvar.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

    def save_as_file(self):
        content = self.textarea.get(1.0, tk.END)
        if not content.strip():
            messagebox.showerror("Erro", "Não há conteúdo para salvar.")
            return
        file_path = filedialog.asksaveasfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

    def exit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
