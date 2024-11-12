# 21. Merge Two Sorted Lists - Easy
# url: https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity: O(n + m), space complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return head.next


if __name__ == "__main__":
    s = Solution()
    # 1 -> 2 -> 4
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # 1 -> 3 -> 4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # 1 -> 1 -> 2 -> 3 -> 4 -> 4
    result = s.mergeTwoLists(list1, list2)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")
