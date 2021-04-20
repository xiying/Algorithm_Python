#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (50.92%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    114.9K
# Total Submissions: 225.8K
# Testcase Example:  '"axc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 进阶：
# 
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢：
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# 两个字符串都只由小写字符组成。
# 
# 
#

# @lc code=start
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) > len(t):       # BUG！注意！先看范围长度！母序列为空的坑！
      return False
    # if len(s) == 0:         # 注意！子序列为空的坑！？？是吗？
    #   return True
    # t的索引，最坏情况从 [0, len(t)) 走一遍
    t_flag = 0
    for s_letter in s:
      if t_flag == len(t):    # BUG！注意！情况："acb" "ahbgdc"
        return False
      # i 为 t实时的对比索引
      for i in range(t_flag, len(t)):
        if s_letter == t[i]:
          t_flag = i + 1
          break
        # 执行此行代码有两种情况：
        #   1-没有进入循环的if，i=len(t)-1，t_flag没变，即 t_flag != i + 1。返回 False
        #   2-进入循环的if，i=[0, len(t))，t_flag=i+1，即 t_flag == i + 1。不返回，继续运行。
      if t_flag != i + 1:
        return False
    # 所有 False 情况被排除，到这里一定 True
    return True
# @lc code=end

