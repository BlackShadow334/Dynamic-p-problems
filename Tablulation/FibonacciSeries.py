# find fibonacci at nth number.


#        0  1  2  3  4  5  6
# fib:   0  1  1  2  3  5  8 .....

# O(n) time
# O(n) space


def fibonacci(n):
    fibs = [0] * (n + 1)
    fibs[1] = 1

    for i in range(n + 1):
        if i + 1 <= n:
            fibs[i + 1] += fibs[i]
        if i + 2 <= n:
            fibs[i + 2] += fibs[i]

    return fibs[n]


if __name__ == "__main__":
    print(fibonacci(6), end=" abcd ")
    print(fibonacci(70))
