/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = (l1, l2) => {
    let curr_l1_elem = l1
    let curr_l2_elem = l2

    let res = new ListNode(0)
    let curr_res_elem = res
    let trailing_digit = 0
    
    while (true) {
        let curr_sum = trailing_digit
        if (curr_l1_elem) {
            curr_sum += curr_l1_elem.val
            curr_l1_elem = curr_l1_elem.next
        }
        if (curr_l2_elem) {
            curr_sum += curr_l2_elem.val
            curr_l2_elem = curr_l2_elem.next
        }
        trailing_digit = (curr_sum / 10) | 0
        curr_res_elem.val = curr_sum < 10 ? curr_sum : curr_sum % 10
        if (!curr_l1_elem && !curr_l2_elem && !trailing_digit) {
            break
        }
        curr_res_elem.next = new ListNode(0)
        curr_res_elem = curr_res_elem.next
        
    }
    return res
}
