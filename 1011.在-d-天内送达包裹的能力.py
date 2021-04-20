#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (56.75%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 31.9K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
# 
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
# 
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
# 
# 
# 
# 示例 1：
# 
# 输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10
# 
# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9),
# (10) 是不允许的。 
# 
# 
# 示例 2：
# 
# 输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
# 
# 
# 示例 3：
# 
# 输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500
# 
# 
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

      def ableShip(w, weights, days):

      # 正计时写法
      # 返回 天数是否 满足条件（实际天数小于等于D）。
      # 从第一天开始。
      # 循环减；不够减的话，天数加一，再减。
        # w_index = w
        # needDays = 1                   # 易错点！赋初值！
        # for i in range(0, len(weights)):
        #   if needDays > days:
        #     return False
        #   if w >= weights[i]:   # 马虎没有写 等号
        #     w -= weights[i]
        #   else:
        #     needDays += 1
        #     w = w_index
        #     w -= weights[i]     # 这里容易忘记
        # return needDays <= days

      # 倒计时写法
        # w_index = w
        # days -= 1           # 倒计时剩余，开始时应该先减1！
        # for i in range(0, len(weights)):
        #   # 倒计时剩余应该大于 0！不能等于0！
        #   if days < 0:
        #     return False
        #   if w >= weights[i]:   # 马虎没有写 等号
        #     w -= weights[i]
        #   else:
        #     days -= 1
        #     w = w_index
        #     w -= weights[i]     # 这里容易忘记
        # # 倒计时剩余应该大于 0！不能等于0！
        # return days >= 0
      
      # 改进: 倒计时写法 (for循环直接用列表，不用i)
      # 返回 天数是否 满足条件（剩余天数大于等于0）。
      # 开始循环前剩余天数先减一。
      # 循环减；不够减的话，天数加一，再减。
        w_index = w
        days -= 1           # 倒计时剩余，开始时应该先减1！
        for weight in weights:
          if days < 0:
            return False
          if w >= weight:   # 马虎没有写 等号
            w -= weight
          else:
            days -= 1
            w = w_index
            w -= weight     # 这里容易忘记
        return days >= 0
      
      # 二分查找 满足题意的最小值（即，满足条件的值的 左边界）
      # 最小值为：max（数组中最大数，数组平均数_向下取整） 例子：[3,3,3] 2，应为 4
      #          但是取 数组中最大数 差别不大。
      # 最大值为：数组中最大数 * (len/D)_向上取整        例子：[3,3,3] 2，应为 6
      max_weights = max(weights)
      length = len(weights)
      l, r = max_weights, max_weights * [length // D + 1, length // D][length % D == 0]
      while l<=r:
        mid = l + (r-l) // 2
        if ableShip(mid, weights, D):
          r = mid - 1
        else:
          l = mid + 1
      return l
# @lc code=end

