class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for indice in range(len(word)):
            letra = word[indice]

            # Guarda a ÚLTIMA posição da minúscula
            if letra.islower():
                lower[letra] = indice

            # Guarda a PRIMEIRA posição da maiúscula
            else:
                letra_minuscula = letra.lower()

                if letra_minuscula not in upper:
                    upper[letra_minuscula] = indice

        especiais = 0

        for letra in lower:
            if letra in upper:
                if lower[letra] < upper[letra]:
                    especiais += 1

        return especiais