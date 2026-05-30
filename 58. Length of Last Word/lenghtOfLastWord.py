class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		i = -1
		count = 0
		while s[i].isspace() and -i < len(s):
			i -= 1
		while -i <= len(s):
			if s[i].isspace():
				return count
			i -= 1
			count += 1
		return count