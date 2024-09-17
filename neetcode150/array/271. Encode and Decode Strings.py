# 271. Encode and Decode Strings - Medium
# url: https://neetcode.io/problems/string-encode-and-decode

from typing import List


# append length of string before the string
# encode: ["hello", "world"] -> "5#hello5#world"
# decode: "5#hello5#world" -> ["hello", "world"]
# Time: O(n), Space: O(1)
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1:j + 1 + length])
            i = j + 1 + length


if __name__ == "__main__":
    s = Solution()
    strs = ["hello", "world"]
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))

    strs = ["hello", "world", "python"]
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))

    strs = ["4#hello", "world", "python", "java"]
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))
