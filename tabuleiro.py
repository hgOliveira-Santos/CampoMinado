import numpy as np
import customtkinter as ctk
from random import randint

class Tabuleiro():
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas

    def alocar_bombas(self):
        matriz_bombas = np.full((self.linhas, self.colunas), "")

        num_bombas = 0
        while num_bombas < self.bombas:
            idx1 = randint(0, self.linhas - 1)
            idx2 = randint(0, self.colunas - 1) 
            if matriz_bombas[idx1][idx2] == "b":
                continue
            else:
                matriz_bombas[idx1][idx2] = "b"
                num_bombas += 1

        return matriz_bombas
    