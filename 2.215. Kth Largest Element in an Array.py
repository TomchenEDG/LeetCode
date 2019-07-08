#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# nums = [-1, 2, 0]
# k = 2
# def findKthLargest(nums, k):
#     two_max = []
#     list = []
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return max(nums[0],nums[1])
#     else:
#         for i in range(len(nums)-1):
#             two_max.append(max(nums[i], nums[i+1]))
#         for i in two_max:
#             if not i in list:
#                 list.append(i)
#         return list[-k]
#
# a = findKthLargest(nums, k)
# print(a)



class Solution():
    def findKthLargest(self, nums: 'List[int]', k: 'int')-> 'int':
        return self.quick_sort(nums, k)

    def quick_sort(self, nums, k):
        # 这个位置的元素是我们想要的结果元素
        k = len(nums) - k
        left = 0
        right = len(nums) - 1
        while left < right:
            j = self.partition(nums, left, right)
            if j == k:
                break
            elif j < k:
                left = j + 1
            else:
                right = j - 1
        return nums[k]

    def partition(self, nums, left, right):
        while True:
            while nums [left] < nums[right]:
                right -= 1
            else:
                nums [left], nums[right] = nums [right], nums [left]
                if left >=right:
                    break
                left += 1

                while nums [left] < nums [right]:
                    left += 1
                else:
                    nums [left], nums [right]= nums [right], nums [left]
                    if left >= right:
                        break
                    right -=1
        return left


def main():
    nums = [2,4,5]
    k = 2

    obj = Solution()
    result = obj.findKthLargest(nums, k)
    print(result)

if __name__=="__main__": main()



# def partition(nums, left, right):
#     while True:
#         while nums[left] < nums[right]:
#             right -= 1
#         else:
#             nums [left], nums[right] = nums[right], nums[left]
#             if left >= right:
#                 break
#             left += 1
#
#             while nums[left] < nums[right]:
#                 left += 1
#             else:
#                 nums[left], nums[right]= nums[right], nums[left]
#                 if left >= right:
#                     break
#                 right -=1
#     return nums

# nums = [3,2,1,5,6,4]
# left = 0
# right = 5
# a = partition(nums, left, right)
# print(a)