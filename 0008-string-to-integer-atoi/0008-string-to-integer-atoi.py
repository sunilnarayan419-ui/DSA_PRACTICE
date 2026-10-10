class Solution:
    def myAtoi(self, s):
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine the sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert digits manually
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1

        result *= sign

        # Step 4: Clamp to the 32-bit integer range
        if result < INT_MIN:
            return INT_MIN

        if result > INT_MAX:
            return INT_MAX

        return result
