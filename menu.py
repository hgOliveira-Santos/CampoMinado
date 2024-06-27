import customtkinter as ctk
from comandos import definir_dificuldade

FECHAR_JANELA = lambda: janela.destroy()

def set_fácil():
    definir_dificuldade("fácil")
    FECHAR_JANELA()

def set_intermediário():
    definir_dificuldade("intermediário")
    FECHAR_JANELA()

def set_especialista():
    definir_dificuldade("especialista")
    FECHAR_JANELA()


ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("Campo Minado")
janela.geometry("600x350+650+300")
janela.resizable(False, False)

head_frame = ctk.CTkFrame(master=janela, width=600, height=70, bg_color="#5432d0", fg_color="#5432d0")
head_frame.place(x=0, y=20)

head_label = ctk.CTkLabel(master=head_frame, text="Campo Minado", font=("Montserrat bold", 32), text_color="#fff")
head_label.place(x=200, y=18)

seleção_label = ctk.CTkLabel(master=janela, text="Selecione a dificuldade: ", font=("Montserrat", 20), text_color="#fff")
seleção_label.place(x=205, y=120)

fácil_botão = ctk.CTkButton(master=janela, text="Fácil", font=("Montserrat", 16), command=set_fácil, width=120, height=40, corner_radius=12, fg_color="#6969d0", hover_color="#432caf")
fácil_botão.place(x=80, y=200)

intermediário_botão = ctk.CTkButton(master=janela, text="Intermediário", font=("Montserrat", 18), command=set_intermediário, width=130, height=40, corner_radius=12, fg_color="#6969d0", hover_color="#432caf")
intermediário_botão.place(x=240, y=200)

especialista_botão = ctk.CTkButton(master=janela, text="Especialista", font=("Montserrat", 18), command=set_especialista, width=125, height=40, corner_radius=12, fg_color="#6969d0", hover_color="#432caf")
especialista_botão.place(x=410, y=200)

janela.mainloop()