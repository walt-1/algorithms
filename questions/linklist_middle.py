# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: [1, 2, 3, 4, 5]
# Output: Node 3 from this list(Serialization: [3, 4, 5])
# The returned node has value 3.  (The judge's serialization of this node is [3, 4, 5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

from SLNode import SLNode

def ll_middle(head):
    # initialize two variables, one that moves one node at a time, one that moves two nodes at a time
    single, double = head, head
    # loop while the double moveing pointer is not None
    while double and double.next:
        # increment single by one
        single = single.next
        # increment double by two
        double = double.next.next
    # return single node
    return single


# SYS OUT
head = SLNode(1, SLNode(2, SLNode(3, SLNode(4, SLNode(5, None)))))
print(ll_middle(head))
