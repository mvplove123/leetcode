#!/usr/bin/env python  
# encoding: utf-8     
""" 
@version: v1.0 
@author: Jerry 
@software: PyCharm 
@file: RemoveElement.py 
@time: 2017/3/29 22:35 
"""


class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1

        nums[:] = nums[:start]

        return nums


if __name__ == '__main__':
    nums, val = [3, 2, 2, 3], 3
    solution = Solution()
    print(solution.removeElement(nums=nums, val=val))
