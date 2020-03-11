from typing import List


class Solution:

  # slow solution 46/46
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    ans = []

    if len(nums) == 0:
      return ans

    nums.sort()
    print(nums)

    def addToArr(arr, start, end):
      # print('add [%d/%d]' % (start, end))

      for item in range(start, end):
        # print('item', item)
        ans.append(item)

    if nums[0] > 1:
      addToArr(ans, 1, nums[0])

    for index, val in enumerate(nums[1:]):
      if val - nums[index] > 1:
        print(val)
        addToArr(ans, nums[index] + 1, val)

    if nums[len(nums) - 1] < len(nums):
      addToArr(ans, nums[len(nums) - 1] + 1, len(nums) + 1)

    return ans


my = Solution()

# n0 = [4, 3, 2, 7, 8, 2, 3, 1]
# n0 = [1, 1]
n0 = [2, 2]

ans = my.findDisappearedNumbers(n0)
print('ans')
print(ans)

# Runtime: 408 ms, faster than 45.99% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 20.3 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
