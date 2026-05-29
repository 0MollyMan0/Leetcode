class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for element in nums:
            digit_sum = 0
            for figure in str(element):
                digit_sum += int(figure)
            ans.append(digit_sum)
        return min(ans)