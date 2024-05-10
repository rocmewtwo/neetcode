# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.heap_merge(lists)
        # return self.divide_merge(lists)

    # merge with heap
    # time: O(nlogk), store k heads, visit every sing node n
    def heap_merge(self, lists: List[Optional[ListNode]]):
        # add k head into list
        min_heap = []
        for l in lists:
            if l:
                # if fisrt vals are equal, it will compare second element
                heappush(min_heap, (l.val, id(l), l))

        head = cur = ListNode()
        # pop while min_heap empty
        while min_heap:
            _, _, l = heappop(min_heap)
            cur.next = l
            cur = cur.next
            l = l.next
            if l:
                heappush(min_heap, (l.val, id(l), l))
        return head.next

    # merge two by two
    # time: O(nlogk), we merge k steps, we need to visit every single node n
    def divide_merge(self, lists: List[Optional[ListNode]]):
        if not lists:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):  # tree height logk
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                temp.append(self.merge_two_lists(l1, l2))
            lists = temp
        return lists[0]

    def merge_two_lists(self, list1, list2):
        head = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return head.next


s = Solution()
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
for i in range(len(lists)):
    h = c = ListNode()
    for j in range(len(lists[i])):
        c.next = ListNode(lists[i][j])
        c = c.next
    lists[i] = h

# print(lists)
print(s.mergeKLists(lists))
