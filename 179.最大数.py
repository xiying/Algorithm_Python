#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (38.22%)
# Likes:    614
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 197.2K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,2]
# 输出："210"
# 
# 示例 2：
# 
# 
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出："1"
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [10]
# 输出："10"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        nums.sort(key=cmp_to_key(lambda x, y: x+y>y+x))
        res= str(int("".join(nums)))
        return res


# @lc code=end

