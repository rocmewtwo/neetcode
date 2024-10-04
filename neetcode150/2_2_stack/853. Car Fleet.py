# 853. Car Fleet - Medium
# url: https://leetcode.com/problems/car-fleet/


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # return self.carFleet_stack(target, position, speed)
        return self.carFleet_save_max(target, position, speed)

    # time complexity: sorting O(nlogn) + traverse cars O(n) = O(nlogn)
    # space complexity: O(n)
    def carFleet_stack(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # store the car fleet time

        for p, s in cars:  # reverse order
            time = (target - p) / s

            # if the time is greater than the last car in the stack, it will form a new car fleet
            # otherwise, it will combine with the last car in the stack
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

    # save the current max time
    # if we have bigger time, it means we have new car fleet
    # time complexity: sorting O(nlogn) + traverse cars O(n) = O(nlogn)
    # space complexity: O(1)
    def carFleet_save_max(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        cur_max = 0

        for p, s in cars:
            time = (target - p) / s
            if time > cur_max:
                res += 1

            cur_max = max(cur_max, time)
        return res


if __name__ == "__main__":
    print(Solution().carFleet(target=12, position=[
          10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))  # 3

    print(Solution().carFleet(target=10, position=[3], speed=[3]))  # 1

    print(Solution().carFleet(target=100, position=[
          0, 2, 4], speed=[4, 2, 1]))  # 1
