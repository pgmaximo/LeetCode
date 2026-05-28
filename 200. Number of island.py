class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ilhas = 0 

        linhas = len(grid)
        colunas = len(grid[0])

        def dfs (linha, coluna):
            # Verifica se saiu da matriz e Verifica se a celula é mar
            if(
                linha < 0 or 
                linha >= linhas or 
                coluna < 0 or 
                coluna >= colunas or
                grid[linha][coluna] != "1"
            ):
                return
            
            # Marca como visitada
            grid[linha][coluna] = "0"

            # Visita vizinhos
            dfs(linha+1, coluna)
            dfs(linha-1, coluna)
            dfs(linha, coluna+1)
            dfs(linha, coluna-1)

        for linha in range(linhas):
            for coluna in range(colunas):
                if grid[linha][coluna] == "1":
                    ilhas+=1
                    dfs(linha, coluna)
        return ilhas