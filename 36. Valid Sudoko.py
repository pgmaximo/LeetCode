class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        linhas = [set() for _ in range(9)]
        colunas = [set() for _ in range(9)]
        blocos = [set() for _ in range(9)]

        for linha in range(9):
            for coluna in range(9):
                valor = board[linha][coluna]

                if valor == ".":
                    continue

                bloco = (linha // 3) * 3 + (coluna // 3)

                if (valor in linhas[linha]) or (valor in colunas[coluna]) or (valor in blocos[bloco]):
                    return False
                
                linhas[linha].add(valor)
                colunas[coluna].add(valor)
                blocos[bloco].add(valor)
        
        return True