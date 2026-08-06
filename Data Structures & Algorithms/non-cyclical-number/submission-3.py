class Solution:
    def isHappy(self, n: int) -> bool:

        count = set()
        while n not in count:
            count.add(n)
            sum = 0
            while n > 0:
                digit = n % 10
                digit = digit ** 2
                sum += digit
                n = n // 10
            if sum == 1:
                return True
            n = sum
        return False        


    