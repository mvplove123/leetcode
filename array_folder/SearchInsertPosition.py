#!/usr/bin/env python
# -*- coding: gb18030 -*-
# @Time    : 2017/3/30 14:41
# @Author  : taoyongbo
# @Site    : 
# @File    : SearchInsertPosition.py
# @desc    :


class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) <= 0:
            return False

        start, end = 0, len(nums) - 1

        if nums[start] > target:
            return 0

        if nums[end] < target:
            return end + 1

        while start < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                end = middle

            else:
                start = middle + 1

        return start


if __name__ == '__main__':
    solution = Solution()
    nums, target = [1], 1
    print(solution.searchInsert(nums=nums, target=target))
