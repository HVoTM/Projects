# LeetCode 1137
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:           
            fib_1, fib_2, fib_3 = 0, 1, 1 # initialize the first 3 numbers
            # Iterate over the required nth sequence
            for i in range(2, n):
                # Utilize the formula: f(n) = f(n-1) + f(n-2)
                new_fib = fib_1 + fib_2 + fib_3
                fib_1 = fib_2
                fib_2 = fib_3
                fib_3 = new_fib

            return new_fib
