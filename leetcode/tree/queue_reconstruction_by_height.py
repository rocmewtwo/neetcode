# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
# reference another solution in array section

from typing import List


class SegmentTree:
    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.val = 0
        self.left = None
        self.right = None

    def build(L, R):
        if L == R:
            leaf = SegmentTree(L, R)
            leaf.val = 1
            return leaf

        root = SegmentTree(L, R)
        M = (L + R) // 2
        root.left = SegmentTree.build(L, M)
        root.right = SegmentTree.build(M + 1, R)
        root.val = root.left.val + root.right.val
        return root

    def takeSpot(self, k):
        if self.L == self.R:
            self.val = 0
            return self.L

        index = None
        if k > self.left.val:
            index = self.right.takeSpot(k - self.left.val)
        else:
            index = self.left.takeSpot(k)

        self.val = self.left.val + self.right.val
        return index


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort ascending height and descending k
        # Think of it as inserting from most constrained to least, if 8 is single highest then [8,0] could be anywhere in the queue
        # OTOH if 4 is lowest height and we have [4, 4] we know when inserting 4 we need to leave exactly 4 spots as everyone will be taller
        people.sort(key=lambda x: (x[0], -x[1]))
        segmentTree = SegmentTree.build(0, len(people) - 1)

        result = [0] * len(people)

        for person in people:
            _, k = person
            # we want to leave k free spots in front so we take the k + 1'th spot
            index = segmentTree.takeSpot(k + 1)
            result[index] = person
        return result
