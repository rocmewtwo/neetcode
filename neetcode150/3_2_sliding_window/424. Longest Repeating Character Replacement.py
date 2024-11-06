# 424. Longest Repeating Character Replacement - Medium
# url: https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import defaultdict


# valid window: len - max(count.values()) <= k
# Time complexity: O(26n) = O(n), space complexity: O(26) = O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count: defaultdict[str, int] = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:  # time complexity: O(26)
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement("ABAB", 2))  # 4
    print(s.characterReplacement("AABABBA", 1))  # 4
