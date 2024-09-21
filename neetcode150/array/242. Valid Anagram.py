# 242. Valid Anagram - Easy
# url: https://leetcode.com/problems/valid-anagram/


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s, t)
        # return self.sort_string(s, t)
        # return self.use_counter(s, t)

    # time complexity: O(s + t), where s is the length of the first string and t is the length of the second string
    # space complexity: O(s + t)
    def count_chars(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t

    # time complexity: O(s + t), where s is the length of the first string and t is the length of the second string
    # space complexity: O(s + t)
    def use_counter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    # time complexity: O(nlogn), where n is the length of the string
    # space complexity: O(1)
    def sort_string(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


s = Solution()
print(s.isAnagram('anagram', 'nagaram'))  # True
print(s.isAnagram('rat', 'car'))  # False
print(s.isAnagram('a', 'ab'))  # False
print(s.isAnagram('a', 'a'))  # True
print(s.isAnagram('a', 'b'))  # False
