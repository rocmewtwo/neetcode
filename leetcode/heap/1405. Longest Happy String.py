# 1405. Longest Happy String - Medium
# url: https://leetcode.com/problems/longest-happy-string/

import heapq


# time: O(a + b + c), since we only have 3 char, heappop and heappush is O(1).
# we can have at most a + b + c iteration
# space: O(1), if we ignore the ans, we only use a constant space
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # max heap
        max_heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        ans = []
        while max_heap:
            count1, char1 = heapq.heappop(max_heap)

            # alread have two duplciate char
            if len(ans) >= 2 and ans[-1] == ans[-2] == char1:
                # find the 2nd most freq
                if not max_heap:  # alread empty and cant concate the 3rd same char
                    break

                count2, char2 = heapq.heappop(max_heap)
                ans.append(char2)
                count2 += 1  # drcrease count
                if count2:
                    heapq.heappush(max_heap, (count2, char2))
            else:
                count1 += 1  # decrease count
                ans.append(char1)

            # push count1 back to heap
            if count1:
                heapq.heappush(max_heap, (count1, char1))

        return ''.join(ans)
