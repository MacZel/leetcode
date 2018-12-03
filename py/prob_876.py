# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        curr_middle_node = head
        curr_middle_count = 1
        while curr_node.next:
            curr_node = curr_node.next
            curr_middle_count += 1
            if curr_middle_count % 2 == 0:
                curr_middle_node = curr_middle_node.next
        return curr_middle_node