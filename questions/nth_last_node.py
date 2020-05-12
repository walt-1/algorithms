class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# accepts list head (Node) and num for tail (int) with rtype: Node 
def nth_last_node(head, n):

    # create dummy head
    dum = Node(0)
    dum.next = head

    # create two pointers init to dummy head
    p1 = dum
    p2 = dum

    # loop in range of 1 to n + 1 + 1 to set distance of pointers from each other
    for i in range(1, n + 2):
        p1 = p1.next
    
    # loop through list until n pointer is at tail
    while p1:
        p1 = p1.next
        p2 = p2.next
    
    # set first pointer.next to pointer.next.next i.e node4.next = node5.next and node5
    p2.next = p2.next.next

    return dum.next
    