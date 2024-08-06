# 3016. Minimum Number of Pushes to Type Word II
# url: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter
import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        return self.minimumPushes_heap(word)
        # return self.minimumPushes_bucket_sort(word)

    # heap solution

    def minimumPushes_heap(self, word: str) -> int:
        freq = Counter(word)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        used, res = 0, 0
        while heap:
            res += -heapq.heappop(heap) * (1 + used // 8)
            used += 1
        return res

    # bucket sort solution
    def minimumPushes_bucket_sort(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1

        freq.sort(reverse=True)
        res = 0
        for i in range(26):
            # early stopping
            if freq[i] == 0:
                break

            res += freq[i] * (1 + i // 8)
        return res


s = Solution()
print(s.minimumPushes("abcde"))  # 5
print(s.minimumPushes("xyzxyzxyzxyz"))  # 12
print(s.minimumPushes("aabbccddeeffgghhiiiiii"))  # 24
