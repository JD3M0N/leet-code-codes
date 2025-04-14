# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
    
    
# Funciones para probar el código
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Prueba con el ejemplo dado
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result_node = solution.addTwoNumbers(l1, l2)
print(linked_list_to_list(result_node))  # Debe imprimir [7, 0, 8]