# 1297. Maximum Number of Occurrences of a Substring
# url: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# Difficulty: medium

from collections import defaultdict


# we only need to check for substrings of length minSize
# the frequency of substrings of length minSize will be greater than or equal to the frequency of substrings of length maxSize
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = 0
        max_freq = 0
        counter = defaultdict(int)
        letters = defaultdict(int)

        for r in range(len(s)):
            letters[s[r]] += 1
            if r - l + 1 > minSize:
                letters[s[l]] -= 1
                if letters[s[l]] == 0:
                    del letters[s[l]]
                l += 1

            if r - l + 1 == minSize and len(letters) <= maxLetters:
                counter[s[l:r + 1]] += 1
                max_freq = max(max_freq, counter[s[l:r + 1]])
        return max_freq


s = Solution()
print(s.maxFreq("aababcaab", 2, 3, 4))  # 2
print(s.maxFreq("aaaa", 1, 3, 3))  # 2
print(s.maxFreq("aabcabcab", 2, 2, 3))  # 3
print(s.maxFreq("abcde", 2, 3, 3))  # 0
