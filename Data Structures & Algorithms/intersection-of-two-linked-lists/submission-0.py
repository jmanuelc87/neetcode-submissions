# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashtable = {}
        tmp = headA
        while tmp is not None:
            hashtable[tmp.val] = tmp
            tmp = tmp.next
        
        tmp = headB
        while tmp is not None:
            if tmp.val in hashtable.keys() and hashtable[tmp.val] == tmp:
                return tmp
            tmp = tmp.next