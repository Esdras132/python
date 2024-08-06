import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    print(f"Nome: {name}")
    print(f"E-mail: {email}")
    print(f"Senha: {password}")
    
    # Limpar os campos após submeter
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Criar a janela principal
root = tk.Tk()
root.title("Formulário")

# Configurar o tamanho da janela para ocupar toda a tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Criar rótulos e campos de entrada
tk.Label(root, text="Nome:").pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

tk.Label(root, text="E-mail:").pack(pady=10)
email_entry = tk.Entry(root)
email_entry.pack(pady=10)

tk.Label(root, text="Senha:").pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Botão para submeter o formulário
submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.pack(pady=20)

# Executar a aplicação
root.mainloop()
