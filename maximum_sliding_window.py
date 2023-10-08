from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        de = deque()

        for i, num in enumerate(nums):
            while de and de[0] < i - k + 1:
                de.popleft()

            while de and nums[de[-1]] < num:
                de.pop()

            de.append(i)

            if i >= k - 1:
                ans.append(nums[de[0]])

        return ans



        

        