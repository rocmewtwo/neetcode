# 3. Longest Substring Without Repeating Characters - Medium
# url: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# time complexity: O(n), space complexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.using_dict(s)
        # return self.using_set(s)

    def using_dict(self, s: str) -> int:
        window: dict[str, int] = dict()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in window:
                # Move the left pointer to the right of the last occurrence of s[r]
                # max() to ensure l is always moving forward
                l = max(window[s[r]] + 1, l)
            window[s[r]] = r
            res = max(res, r - l + 1)

        return res

    def using_set(self, s: str) -> int:
        window: set[str] = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if find duplicate, move
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))  # 1
    print(s.lengthOfLongestSubstring("pwwkew"))  # 3
