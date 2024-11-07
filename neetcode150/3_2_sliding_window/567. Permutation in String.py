# 567. Permutation in String - Medium
# url: https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.compare_match(s1, s2)
        # return self.compare_two_freqs(s1, s2)

    # time complexity: O(n), space complexity: O(26 * 2) = O(1)
    def compare_match(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1, freq2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # count match
        match = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                match += 1

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True

            index = ord(s2[r]) - ord('a')
            freq2[index] += 1
            if freq1[index] == freq2[index]:
                match += 1
            elif freq1[index] == freq2[index] - 1:
                match -= 1

            index = ord(s2[l]) - ord('a')
            freq2[index] -= 1
            if freq1[index] == freq2[index]:
                match += 1
            elif freq1[index] == freq2[index] + 1:
                match -= 1
            l += 1

        return match == 26

    # Time complexity: O(26n), space complexity: O(26 * 2) = O(1)
    def compare_two_freqs(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1, freq2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if freq1 == freq2:  # 26 comparisons
                return True

            index = ord(s2[r]) - ord('a')
            freq2[index] += 1

            index = ord(s2[l]) - ord('a')
            freq2[index] -= 1
            l += 1

        if freq1 == freq2:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))  # true
    print(s.checkInclusion("ab", "eidboaoo"))  # false
