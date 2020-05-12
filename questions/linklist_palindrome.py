# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1 -> 2
# Output: false

# Example 2:
# Input: 1 -> 2 -> 2 -> 1
# Output: true


def is_palindrome(head):
    # manage pointers
    fast = head
    slow = head

    # set pointers
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = fast.next

    # reset fast
    fast = head
    # revers slow
    slow = _reverse(slow)

    while slow != None
       # assert values are the same
        if slow.val != fast.val:
            # if not then return False
            return False

        # move pointers
        slow = slow.next
        fast = fast.next

    return True


def _reverse(head):
    prev = None
    while head != None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
