# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/description/

from sortedcontainers import SortedList


class SortedSet_MyCalendar:
    # sorted set. time: O(logn)
    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        i = self.events.bisect_left((start, ))

        # check with next
        if i < len(self.events) and end > self.events[i][0]:
            return False

        # check with prev
        if i > 0 and start < self.events[i-1][1]:
            return False

        self.events.add((start, end))
        return True


class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None


class Binary_Tree_MyCalendar:
    # binary search tree, time: worse case O(n)
    def __init__(self):
        self.root = None

    def insert(self, root, s, e):
        if not root:
            root = Node(s, e)
            return root, True

        if s >= root.e:
            root.right, res = self.insert(root.right, s, e)
        elif e <= root.s:
            root.left, res = self.insert(root.left, s, e)
        else:
            return root, False

        return root, res

    def book(self, start: int, end: int) -> bool:
        self.root, res = self.insert(self.root, start, end)
        return res


# c = Binary_Tree_MyCalendar()
c = SortedSet_MyCalendar()

events = [[47, 50], [33, 41], [39, 45], [33, 42], [
    25, 32], [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]]
ans = []
for s, e in events:
    ans.append(c.book(s, e))
print(ans)
assert [True, True, False, False, True, False, True, True, True, False] == ans
