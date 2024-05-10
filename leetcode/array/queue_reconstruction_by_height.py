# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/description/

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        return self.sort_h_k(people)

    # time: O(nlogn), space: O(n)
    def sort_h_k(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []

        # print(people)
        for p in people:
            res.insert(p[1], p)
            # print(res, p)
        return res


s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
