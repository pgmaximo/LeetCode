class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dicionario de numero romano
        romans = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500, 'M': 1000}
        
        # Sessao de trocas de numeros
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        inteiro = 0
        for char in s:
            inteiro += romans[char]
        return inteiro