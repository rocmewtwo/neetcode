# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)

'''
    P: head -> cycle head
    C: cycle length
    X: slow == fast node

    2 * slow = fast
    2 * (P + C - X) = P + C + C - X
    2P + 2C - 2X = P + 2C - X
    P = X (head -> cycle head equals to slow-fast node)
'''


def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:  # no cycle
        return None

    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
