/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const middleNode = head => {
    let curr_node = head
    let curr_middle_node = head
    let curr_middle_count = 1
    
    while (curr_node.next) {
        curr_node = curr_node.next
        curr_middle_count++
        if (curr_middle_count % 2 == 0) {
            curr_middle_node = curr_middle_node.next
        }
    }
    return curr_middle_node
}