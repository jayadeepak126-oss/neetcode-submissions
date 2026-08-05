class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = ""
        for i in s:
            if i.isalnum():
                st += i.lower()
        
        j = len(st) - 1
        for i in range(len(st)):
            if st[i] != st[j]:
                return False
            j-=1
        return True
