# 49. Group Anagrams - Medium
# url: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.count_chars(strs)
        # return self.sorted_string(strs)

    # time complexity: O(n * m), n is the length of strs, m is the length of the longest string in strs
    # space complexity: O(n * m)
    def count_chars(self, strs: str) -> str:
        group = defaultdict(list)

        for s in strs:
            count = [0] * 26
            # count frequency as a key
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)

        return group.values()

    # time complexity: O(n * m * log(m)), n is the length of strs, m is the length of the longest string in strs
    # space complexity: O(n * m)
    def sorted_string(self, strs: str) -> str:
        group = defaultdict(list)

        for s in strs:
            sorted_str = tuple(sorted(s))
            group[sorted_str].append(s)

        return group.values()


s = Solution()
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))  # Output: [[""]]
