# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        lists = list(filter(None, lists))
        
        if not lists:
            return []
        
        ans = ListNode(None)
        curr_ans_elem = ans
        
        values = [listnode.val for listnode in lists]
        while lists:
            min_val = min(values)
            min_pos = values.index(min_val)
            
            if lists[min_pos].next:
                lists[min_pos] = lists[min_pos].next
                values[min_pos] = lists[min_pos].val
            else:
                lists.pop(min_pos)
                values.pop(min_pos)
            
            curr_ans_elem.val = min_val
            if lists:
                curr_ans_elem.next = ListNode(None)
                curr_ans_elem = curr_ans_elem.next
        
        return ans