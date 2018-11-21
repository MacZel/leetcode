# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_l1_elem = l1
        curr_l2_elem = l2
        
        ans = ListNode(None)
        curr_ans_elem = ans
        
        while l1 and l2:
            if l1.val > l2.val:
                curr_ans_elem.next = l2
                l2 = l2.next
                curr_ans_elem = curr_ans_elem.next
            else:
                curr_ans_elem.next = l1
                l1 = l1.next
                curr_ans_elem = curr_ans_elem.next
        if l1 is None:
            curr_ans_elem.next = l2
        if l2 is None:
            curr_ans_elem.next = l1
        ans = ans.next
        
        return ans