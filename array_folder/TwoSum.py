#!/usr/bin/env python  
# encoding: utf-8     
""" 
@version: v1.0 
@author: Jerry 
@software: PyCharm 
@file: TwoSum.py 
@time: 2017/3/30 8:22 
"""


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False

        target_dict = {}
        for i in range(len(nums)):
            if nums[i] in target_dict:
                return [target_dict[nums[i]], i]
            else:
                target_dict[target - nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    nums, target = [7, 3, 2, 15], 9
    print(solution.twoSum(nums=nums, target=target))
