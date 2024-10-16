# 981. Time Based Key-Value Store - Medium
# url: https://leetcode.com/problems/time-based-key-value-store/


import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.kv = defaultdict(list)

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    # O(logn)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        # find the last element that is less than or equal to timestamp
        # chr(127) is the largest ascii character
        i = bisect.bisect_right(self.kv[key], (timestamp, chr(127)))

        if i == 0:
            return ""
        return self.kv[key][i - 1][1]  # insertion point - 1


if __name__ == "__main__":
    keys = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    values = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
              ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    tm = TimeMap()
    for i in range(1, len(keys)):
        print(getattr(tm, keys[i])(*values[i]))
