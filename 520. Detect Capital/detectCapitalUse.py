class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        if word[0].isupper() and word[1].isupper():
            for letter in word:
                if letter.islower():
                    return False
        else:
            for letter in word[1:]:
                if letter.isupper():
                    return False
        return True