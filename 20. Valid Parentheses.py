class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []

        pares = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for char in s:
            if char in pares.values():
                pilha.append(char)
            else:
                if not pilha or pilha.pop() != pares[char]:
                    return False
        
        return not pilha
                
