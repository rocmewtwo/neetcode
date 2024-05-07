from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combine_factorial(n, k)
        # return self.combine_dfs(n, k)

    # time: O(k * C(n, k))
    def combine_factorial(self, n: int, k: int) -> List[List[int]]:
        res, cur_comb = [], []

        def dfs(i):
            if len(cur_comb) == k:
                res.append(cur_comb.copy())
                return

            if i > n:
                return

            for j in range(i, n + 1):
                cur_comb.append(j)
                dfs(j + 1)
                cur_comb.pop()
        dfs(1)
        return res

    # time: O(k * 2^n)
    def combine_dfs(self, n: int, k: int) -> List[List[int]]:
        res, cur_comb = [], []

        def dfs(i):
            if len(cur_comb) == k:
                res.append(cur_comb.copy())
                return

            if i > n:
                return

            # choose i
            cur_comb.append(i)
            dfs(i + 1)
            cur_comb.pop()

            # not choose i
            dfs(i + 1)

        dfs(1)
        return res
