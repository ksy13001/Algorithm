/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode current = result;
        int over = 0;
        while(l1 != null || l2 != null || over > 0){
            int val1=0; int val2=0;
            if(l1 != null){
                val1 = l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                val2 = l2.val;
                l2 = l2.next;
            }
            int temp = val1 + val2 + over;
            over = temp / 10;
            temp = temp % 10;
            current.next = new ListNode(temp);
            current = current.next;
        }

        return result.next;
    }
}
