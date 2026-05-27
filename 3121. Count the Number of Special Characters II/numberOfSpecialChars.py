class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, letter in enumerate(word):
            if letter.islower():
                last_lower[letter] = i
            elif letter.isupper():
                if letter.lower() not in first_upper:
                    first_upper[letter.lower()] = i

        count = 0
        for letter in last_lower:
            if letter in first_upper:
                if last_lower[letter] < first_upper[letter]:
                    count += 1

        return count