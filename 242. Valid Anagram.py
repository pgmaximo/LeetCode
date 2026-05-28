class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = {}
        tDic = {}

        if len(s) != len(t):
            return False

        for letra in s:
            sDic[letra] = sDic.get(letra,0) + 1
        
        for letra in t:
            tDic[letra] = tDic.get(letra,0) + 1
        
        return True if sDic == tDic else False