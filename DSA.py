
print("DSA")
# leetcode problem no: 344 (aka reverse string)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP
#88: merge stored arrays
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums2[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]   
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1