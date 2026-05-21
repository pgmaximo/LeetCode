# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        dummy = ListNode(0)
        atual = dummy

        while l1 or l2 or carry:
            valor1 = l1.val if l1 else 0
            valor2 = l2.val if l2 else 0

            soma = valor1 + valor2 + carry

            digito = soma % 10
            carry = soma // 10

            atual.next = ListNode(digito)
            atual = atual.next

            if l1:
                l1 = l1.next
            
            if l2: 
                l2 = l2.next
        return dummy.next