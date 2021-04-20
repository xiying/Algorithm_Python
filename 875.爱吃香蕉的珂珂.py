# @lc app=leetcode.cn id=875 lang=python3

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:

    # 该速度能否吃完.吃完返回True；吃不完返回False
    # def ableEatingSpeed(speed, piles, hours):
    #   for i in range(0, len(piles)):
    #     # 如果 hours<0 直接退出循环
    #     if hours < 0:
    #       return False
    #     if (piles[i] % speed) != 0:
    #       hours -= (piles[i]//speed + 1)
    #     else:
    #       hours -= (piles[i] // speed)
    #   if hours < 0:
    #     return False
    #   else:
    #     return True

    # 改进：该速度能否吃完.吃完返回True；吃不完返回False (for循环直接用列表，不用i；直接return，不用if-else)
    def ableEatingSpeed(speed, piles, hours):
      for pile in piles:
        # 如果 hours<0 直接退出循环
        if hours < 0:
          return False
        if (pile % speed) != 0:
          hours -= (pile//speed + 1)
        else:
          hours -= (pile // speed)
      return hours >= 0

    # 二分查找 满足题意的最小值（即，满足条件的值的 左边界）
    l, r = 1, max(piles)
    while l <= r:
      mid = l + (r-l)//2
      if ableEatingSpeed(mid, piles, h):
        r = mid - 1
      else:
        l = mid + 1
    return l
# @lc code=end

