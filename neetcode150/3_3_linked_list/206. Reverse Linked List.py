# 206. Reverse Linked List - Easy
# url: https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n), space complexity: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode | None:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    s = Solution()

    # create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    # reverse the linked list: 5 -> 4 -> 3 -> 2 -> 1
    reversed_head = s.reverseList(node1)

    # print the reversed linked list
    while reversed_head:
        print(reversed_head.val, end=" -> ")
        reversed_head = reversed_head.next
    print("None")
