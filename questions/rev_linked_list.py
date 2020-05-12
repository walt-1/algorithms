# Reverse a singly linked list can be done iteratively and recursively
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

from SLNode import SLNode

def rev_linked_list(head):
    # base case
    if head == None or head.next == None:
        return head

    # subroutine
    rev = rev_linked_list(head.next)
    head.next.next = head.next
    head.next = None
    print(head.val)
    return rev


def rev_iter(head):
    prev_node = None
    cur_node = head
    next_node = None

    while cur_node:
        # save next pointer
        next_node = cur_node.next
        # reverse cur
        cur_node.next = prev_node
        # move prev fwd
        prev_node = cur_node
        # move cur fwd
        cur_node = next_node

    return prev_node

head = SLNode(1, SLNode(2, SLNode(3, SLNode(4, SLNode(5, None)))))

rev_linked_list(head)

