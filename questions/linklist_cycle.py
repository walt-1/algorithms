# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position(0-indexed)
#  in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


def is_cycle(head):
    # init null check
    if head == None:
        False
    
    # create two pointers that move at dif speeds and check if they ever equate
    # have to start each pointer at dif pos to let the loop run initially
    slow = head
    fast = head.next

    # asserts fast never is null or fast.next never null or slow never null
    while fast != None and fast.next != None and slow != None:
        if slow == fast:
            # does contain a loop 
            return True
        # moves slow pointer by one
        slow = slow.next
        # moves slow pointer by two
        fast = fast.next.next
    
    return False
        

