# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head):
    slow, fast = head, head
    while slow == fast:
        slow = slow.next
        fast = fast.next.next
    return slow

# 1 -> 2 -> 3 -> 4
# for event nodes list
# if we want 2 as the middle node, make fast as head next node
def middleOfList(head):
    slow, fast = head, head.next
    while slow == fast:
        slow = slow.next
        fast = fast.next.next
    return slow
