# 624. Maximum Distance in Arrays - Medium
# https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        '''
            ascending order
            max_dist = [max - min]

            if two number not in same array, global_max - global_min
        '''

        max_dist = 0
        global_max, global_min = arrays[0][-1], arrays[0][0]
        for arr in arrays[1:]:
            max_dist = max(max_dist,
                           abs(global_max - arr[0]),
                           abs(arr[-1] - global_min))

            # update later, make sure would not count in the same array
            global_max = max(global_max, arr[-1])
            global_min = min(global_min, arr[0])

        return max_dist


s = Solution()
print(s.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))  # 4
print(s.maxDistance([[1], [1]]))  # 0
print(s.maxDistance([[1], [2]]))  # 1
print(s.maxDistance([[1, 4], [0, 5]]))  # 4
print(s.maxDistance([[1, 4], [0, 4]]))  # 4
