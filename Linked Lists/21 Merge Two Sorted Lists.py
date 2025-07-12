# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        
        head = ListNode(-101)
        cur = head
        prev_val = -101
        
        while list1 and list2:
            new_node = None
            
            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                list2 = list2.next
            
            cur.next = new_node
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        return head.next  