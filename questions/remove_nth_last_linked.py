# Given linked list: 1 -> 2 -> 3 -> 4 -> 5, and n = 2.
# After removing the second node from the end, the linked list becomes 1 -> 2 -> 3 -> 5.
from .SLNode import SLNode

def remove_nth_last(head, n):
    if head.next == None:
        return None

    dummy = ListNode(0, head)
    
    cur_node = nth_node = dummy
    count = 0

    while cur_node.next:
        cur_node = cur_node.next
        count += 1
        if count >= n + 1:
            nth_node = nth_node.next
    node_removed = nth_node.next.val
    nth_node.next = nth_node.next.next
    
    print("removed " + str(node_removed))
    return dummy.next


head = SLNode(1, SLNode(2, SLNode(3, SLNode(4, SLNode(5, None)))))
remove_nth_last(head, 2)

