import tkinter as tk
from tkinter import ttk, messagebox

class TableApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tabela de Dados")

        self.tree = ttk.Treeview(self.master, columns=("Nome", "Idade", "Cidade"))

        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Nome')
        self.tree.heading('#2', text='Idade')
        self.tree.heading('#3', text='Cidade')

        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)

        self.tree.pack(expand=True, fill='both')

        self.add_data("1", "João", "25", "São Paulo")
        self.add_data("2", "Maria", "30", "Rio de Janeiro")
        self.add_data("3", "Pedro", "28", "Belo Horizonte")

        self.add_button = tk.Button(self.master, text="Adicionar", command=self.add_row)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edit_button = tk.Button(self.master, text="Editar", command=self.edit_row)
        self.edit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_button = tk.Button(self.master, text="Atualizar", command=self.update_row)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_data(self, id, nome, idade, cidade):
        self.tree.insert('', 'end', text=id, values=(nome, idade, cidade))

    def add_row(self):
        self.add_edit_window = tk.Toplevel(self.master)
        self.add_edit_window.title("Adicionar Dados")

        tk.Label(self.add_edit_window, text="Nome:").grid(row=0, column=0)
        tk.Label(self.add_edit_window, text="Idade:").grid(row=1, column=0)
        tk.Label(self.add_edit_window, text="Cidade:").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.add_edit_window)
        self.name_entry.grid(row=0, column=1)

        self.age_entry = tk.Entry(self.add_edit_window)
        self.age_entry.grid(row=1, column=1)

        self.city_entry = tk.Entry(self.add_edit_window)
        self.city_entry.grid(row=2, column=1)

        add_button = tk.Button(self.add_edit_window, text="Adicionar", command=self.save_new_row)
        add_button.grid(row=3, columnspan=2)

    def save_new_row(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        city = self.city_entry.get()

        if name and age and city:
            new_id = len(self.tree.get_children()) + 1
            self.add_data(str(new_id), name, age, city)
            self.add_edit_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def edit_row(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione uma linha para editar.")
            return

        item = self.tree.item(selected_item)
        id = item['text']
        values = item['values']
        name, age, city = values

        self.add_edit_window = tk.Toplevel(self.master)
        self.add_edit_window.title("Editar Dados")

        tk.Label(self.add_edit_window, text="Nome:").grid(row=0, column=0)
        tk.Label(self.add_edit_window, text="Idade:").grid(row=1, column=0)
        tk.Label(self.add_edit_window, text="Cidade:").grid(row=2, column=0)

        self.name_entry = tk.Entry(self.add_edit_window)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.insert(0, name)

        self.age_entry = tk.Entry(self.add_edit_window)
        self.age_entry.grid(row=1, column=1)
        self.age_entry.insert(0, age)

        self.city_entry = tk.Entry(self.add_edit_window)
        self.city_entry.grid(row=2, column=1)
        self.city_entry.insert(0, city)

        save_button = tk.Button(self.add_edit_window, text="Salvar", command=lambda item=id: self.save_edited_row(item))
        save_button.grid(row=3, columnspan=2)

def save_edited_row(self, item):
    name = self.name_entry.get()
    age = self.age_entry.get()
    city = self.city_entry.get()

    if name and age and city:
        self.tree.item(item, text=item, values=(name, age, city))
        self.add_edit_window.destroy()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


    def update_row(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Por favor, selecione uma linha para atualizar.")
            return

        item = self.tree.item(selected_item)
        id = item['text']

        self.save_edited_row(id)

def main():
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
