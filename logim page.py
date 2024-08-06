import tkinter as tk
 
label_age = int

def erro_form():
    root = tk.Tk()
    root.title('Erro')
    texto = tk.Label(root, text="Todos os campos precisam estar preenchidos")
    texto.grid(row=3, column=0, columnspan=2)
    botao_ok = tk.Button(root, text='OK', command=root.destroy)
    botao_ok.grid(row=5, column=0, columnspan=2)

def validate_form():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    
    if not name or not age or not email:
        erro_form()
        return False
    return True

def submit_form(event=None):
    if not validate_form():
        return
    
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    print("Name:", name)
    print("Age:", age)
    print("Email:", email)

    # Clear the form fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
def submit_for():
    if not validate_form():
        return

    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print(name, "foi adicionado\n")

    # Clear the form fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Form Example")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0)


label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

button_submit = tk.Button(root, text="Submit", command=submit_for)
button_submit.grid(row=3, column=0, columnspan=2)

root.bind('<Return>', submit_form)  

root.mainloop()
