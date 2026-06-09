class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        linha = len(matrix)
        coluna = len(matrix[0])

        set_linha = set()
        set_coluna = set()

        for i in range(linha):
            for j in range(coluna):
                if matrix[i][j] == 0:
                    set_linha.add(i)
                    set_coluna.add(j)
        
        for i in range(linha):
            for j in range(coluna):
                if i in set_linha or j in set_coluna:
                    matrix[i][j] = 0