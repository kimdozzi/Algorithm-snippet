class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
            else:
                continue
        words = lst
        for word in range(len(words)//2):
            if words[word] == lst[len(lst) - (word + 1)]:
                continue
            else:
                return False
        return True
