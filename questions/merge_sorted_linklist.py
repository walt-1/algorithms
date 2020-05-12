# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Input: 1 -> 2 -> 4, 1 -> 3 -> 4
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

from SLNode import SLNode

def merge_sorted_linkedlist(l1, l2):

    dummy = SLNode(0, None)
    head = dummy

    while l1 != None or l2 != None:
        if l1.val < l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l1
            l2 = l2.next
        
    # 1->2 + 2->3->[4]
    if l1 != None:
        dummy.next = l1
    else:
        dummy.next = l2
    
    return head.next

