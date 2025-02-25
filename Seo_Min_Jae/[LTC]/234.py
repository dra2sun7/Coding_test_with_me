# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = [];
        while (head.next):
            list.append(head.val)
            head.val = head.next.val
            head.next = head.next.next
        list.append(head.val)

        for i in range(len(list)//2):
            if (list[i] != list[len(list)-1-i]):
                return False
        
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = [];

        if not head:
            return True

        node = head
        while node is not None:
            list.append(node.val)
            node = node.next

        while len(list) > 1:
            if list.pop(0) != list.pop():
                return False
        
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True

