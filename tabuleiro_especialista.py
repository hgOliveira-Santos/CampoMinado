from tabuleiro import Tabuleiro
import customtkinter as ctk
import numpy as np

class Especialista(Tabuleiro):
    def __init__(self, linhas, colunas, bombas):
        super().__init__(linhas, colunas, bombas)
        self.matriz = np.full((linhas, colunas), None)
        self.janela = ctk.CTk()
        self.FECHAR_JANELA = lambda: self.janela.destroy()

    def interface(self):
        ctk.set_appearance_mode("dark")
        self.janela.title("Campo Minado - Especialista")
        self.janela.geometry("710x480")
        self.janela.resizable(False, False)

        frame_esp = ctk.CTkFrame(master=self.janela, width=710, height= 70, corner_radius=0, bg_color="#5550fc", fg_color="#5550fc")
        frame_esp.place(x=0, y=0)
        
        matriz_bombas = self.alocar_bombas()
        matriz_botões = self.criar_botões()

        botão_desistir = ctk.CTkButton(master=self.janela, command=self.FECHAR_JANELA, text="Desistir", corner_radius=15, fg_color="red", bg_color="#5550fc", hover_color="darkred")
        botão_desistir.place(x=20, y=20)

        self.janela.mainloop()

    def aloca_bandeira(self, event, idx1, idx2):
        print("Clique direito")
        print(f"Pos {idx1} - {idx2}")

    def verificar_espaço(self, idx1, idx2):
        print(f"{idx1} - {idx2}")
        
    def criar_botões(self):
        botões = np.full((self.linhas, self.colunas), None)

        posx = 40
        posy = 110
        for linha in range(len(botões)):
            for coluna in range(len(botões[linha])):
                botões[linha][coluna] = ctk.CTkButton(master=self.janela, command=lambda linha=linha, coluna=coluna: self.verificar_espaço(linha, coluna), width=20, height=20, text="", corner_radius=0, hover_color="#36328c", fg_color="#5550fc")
                posição_bandeira = lambda event, x=linha, y=coluna: self.aloca_bandeira(event, x, y)
                botões[linha][coluna].bind('<Button-3>', posição_bandeira)
                botões[linha][coluna].place(x=posx, y=posy)
                posx += 21
            posx = 40
            posy += 21

        return botões
    
esp = Especialista(16, 30, 99)
esp.interface()