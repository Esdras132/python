import customtkinter as ctk
import requests


janela = ctk.CTk()
janela.title('Produtos')
janela.geometry('400x400')
# janela.iconbitmap('favicon.ico')
janela.resizable(height=True,width=False)
# frame = ctk.CTkFrame(master=janela, width=380, height=50,fg_color="green",corner_radius=10).place(x=10, y=10)
tabView = ctk.CTkTabview(janela, width=400)
tabView.pack()
tabView.add('Nome')
tabView.add('Idade')
tabView.add('Genero')
tabView.tab('Nome').grid_columnconfigure(0, weight=20)
tabView.tab('Idade').grid_columnconfigure(0, weight=20)
tabView.tab('Genero').grid_columnconfigure(0, weight=20)

text =ctk.CTkLabel(tabView.tab('Nome'),text='jose')
text2 =ctk.CTkLabel(tabView.tab('Idade'),text='15')
text3 =ctk.CTkLabel(tabView.tab('Genero'),text='Masculino')
text.pack()
text2.pack()
text3.pack()


janela.mainloop()
