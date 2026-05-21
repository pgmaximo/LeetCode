class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Defino a variavel prefixo com a primeira palavra e sua 
        prefixo = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefixo):
                prefixo = prefixo[:-1]
        
        return prefixo
