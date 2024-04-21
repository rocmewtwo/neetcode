# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find middle and reverse fisrt linked list
        # head1 = prev, head2 = slow
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        max_sum = 0
        while slow:
            max_sum = max(max_sum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return max_sum
