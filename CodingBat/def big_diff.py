#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.


def big_diff(nums):
  maxNum = max(nums)
  minNum = min(nums)
  return maxNum - minNum