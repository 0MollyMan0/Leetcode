class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = []
        uppercase = []

        for letter in word:
            if letter.islower() and letter not in lowercase:
                lowercase.append(letter)
            elif letter.isupper() and letter not in uppercase:
                uppercase.append(letter)

        count = 0
        for letter in lowercase:
            if letter.upper() in uppercase:
                count += 1

        return count