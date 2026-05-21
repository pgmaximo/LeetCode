class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        esq = 0
        dir = len(height)-1
        
        maior = 0
        
        while esq < dir:
            largura = dir - esq
            
            altura = min(height[esq], height[dir])
            area = altura * largura
            
            if area > maior:
                maior = area
            
            if height[esq] < height[dir]:
                esq += 1
            else:
                dir -= 1
        return maior