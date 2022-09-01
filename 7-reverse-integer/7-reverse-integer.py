class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        reversed_integer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            current_number = x % 10
            if reversed_integer * 10 + current_number > (2 **31) or reversed_integer * 10 + current_number < ((-2 ** 31) - 1):
                return 0
            reversed_integer = reversed_integer * 10 + current_number
            x //= 10
        return reversed_integer * sign