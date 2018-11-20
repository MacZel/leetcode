# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr_l1_elem = l1
        curr_l2_elem = l2
        
        res = ListNode(0)
        curr_res_elem = res
        trailing_digit = 0
        
        while True:
            curr_sum = trailing_digit
            if curr_l1_elem:
                curr_sum += curr_l1_elem.val
                curr_l1_elem = curr_l1_elem.next
            if curr_l2_elem:
                curr_sum += curr_l2_elem.val
                curr_l2_elem = curr_l2_elem.next
            
            curr_dig = curr_sum if curr_sum < 10 else curr_sum % 10
            trailing_digit = int(curr_sum / 10)
            curr_res_elem.val = curr_dig
                
            if not curr_l1_elem and not curr_l2_elem and not trailing_digit:
                break
            
            curr_res_elem.next = ListNode(0)
            curr_res_elem = curr_res_elem.next
            
        return res
