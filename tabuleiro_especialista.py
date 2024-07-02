from tabuleiro import Tabuleiro
import customtkinter as ctk
import numpy as np

class Especialista(Tabuleiro):
    def __init__(self, linhas, colunas, bombas):
        super().__init__(linhas, colunas, bombas)
        self.matriz = np.full((linhas, colunas), None)
        self.janela = ctk.CTk()
        self.FECHAR_JANELA = lambda: self.janela.destroy()
        self.matriz_bombas = self.alocar_bombas()
        self.matriz_botões = self.criar_botões()
        # self.matriz_bandeiras = np.full((linhas, colunas), False)
        self.bandeira = "🏴"
        self.bomba = "💣"
        self.dúvida = "❔"

    def interface(self):
        ctk.set_appearance_mode("dark")
        self.janela.title("Campo Minado - Especialista")
        self.janela.geometry("740x500")
        self.janela.resizable(False, False)

        frame_esp = ctk.CTkFrame(master=self.janela, width=740, height= 70, corner_radius=0, bg_color="#5550fc", fg_color="#5550fc")
        frame_esp.place(x=0, y=0)

        botão_desistir = ctk.CTkButton(master=self.janela, command=self.FECHAR_JANELA, text="Desistir", corner_radius=15, fg_color="red", bg_color="#5550fc", hover_color="darkred")
        botão_desistir.place(x=400, y=20)

        botão_reiniciar = ctk.CTkButton(master=self.janela, command=self.reiniciar_jogo, text="Reiniciar", text_color="#000", corner_radius=15, fg_color="#9fb0fc", bg_color="#5550fc", hover_color="gray")
        botão_reiniciar.place(x=20, y=20)

        self.janela.mainloop()

    def reiniciar_jogo(self):
        pass

    def alocação_bandeira(self, event, linha, coluna, x, y):
        print("Colocando bandeira")
        print(f"Pos {linha} - {coluna}")

        self.matriz_botões[linha][coluna] = ctk.CTkButton(master=self.janela, text=self.bandeira, text_color="black", command=lambda linha=linha, coluna=coluna: self.verificar_espaço(linha, coluna), width=20, height=20, corner_radius=0, hover_color="#36328c", fg_color="#5550fc")
        self.matriz_botões[linha][coluna].bind("<Button-3>", lambda event, linha=linha, coluna=coluna, posx=x, posy=y: self.alocação_dúvida(event, linha, coluna, posx, posy))
        self.matriz_botões[linha][coluna].place(x=x, y=y)

    def alocação_dúvida(self, event, linha, coluna, x, y):
        print("Colocando interrogação")
        print(f"Pos {linha} - {coluna}")

        self.matriz_botões[linha][coluna] = ctk.CTkButton(master=self.janela, text=self.dúvida, text_color="white", command=lambda linha=linha, coluna=coluna: self.verificar_espaço(linha, coluna), width=20, height=20, corner_radius=0, hover_color="#36328c", fg_color="#5550fc")
        self.matriz_botões[linha][coluna].bind("<Button-3>", lambda event, linha=linha, coluna=coluna, posx=x, posy=y: self.retirar_símbolo(event, linha, coluna, posx, posy))
        self.matriz_botões[linha][coluna].place(x=x, y=y)
    
    def retirar_símbolo(self, event, linha, coluna, x, y):
        print("Retirando simbolos")
        print(f"Pos {linha} - {coluna}")

        self.matriz_botões[linha][coluna] =  ctk.CTkButton(master=self.janela, text="", text_color="black", command=lambda linha=linha, coluna=coluna: self.verificar_espaço(linha, coluna), width=20, height=20, corner_radius=0, hover_color="#36328c", fg_color="#5550fc")
        self.matriz_botões[linha][coluna].bind("<Button-3>", lambda event, linha=linha, coluna=coluna, posx=x, posy=y: self.alocação_bandeira(event, linha, coluna, posx, posy))
        self.matriz_botões[linha][coluna].place(x=x, y=y)

    def verificar_espaço(self, idx1, idx2):
        print(f"{idx1} - {idx2}")

        if self.matriz_bombas[idx1][idx2] == "b":
            self.mostrar_bombas()

    def mostrar_bombas(self):
        posx = 40
        posy = 110

        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if self.matriz_bombas[linha][coluna] == "b":
                    espaço = ctk.CTkButton(master=self.janela, width=21, height=21, text=self.bomba, text_color="black", fg_color="#5550fc", bg_color="#5550fc", hover_color="#5550fc", corner_radius=0)
                    espaço.place(x=posx, y=posy)
                else:
                    espaço = ctk.CTkButton(master=self.janela, height=21, width=21, text="", fg_color="#5550fc", bg_color="#5550fc", hover_color="#5550fc", corner_radius=0)
                    espaço.place(x=posx, y=posy)
                posx += 22
            posx = 40
            posy += 22

    def criar_botões(self):
        botões = np.full((self.linhas, self.colunas), None)
        posx = 40
        posy = 110
        for linha in range(len(botões)):
            for coluna in range(len(botões[linha])):
                botões[linha][coluna] = ctk.CTkButton(master=self.janela, command=lambda linha=linha, coluna=coluna: self.verificar_espaço(linha, coluna), width=20, height=20, text="", corner_radius=0, hover_color="#36328c", fg_color="#5550fc")
                botões[linha][coluna].bind('<Button-3>', lambda event, linha=linha, coluna=coluna, posx=posx, posy=posy: self.alocação_bandeira(event, linha, coluna, posx, posy))
                botões[linha][coluna].place(x=posx, y=posy)
                posx += 22
            posx = 40
            posy += 22
        return botões
