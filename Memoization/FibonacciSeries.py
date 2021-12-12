# find fibonacci at nth number.


# concept of memoziation is added here
def getFibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num <= 2:
        return 1
    memo[num] = getFibonacci(num - 1, memo) + getFibonacci(num - 2, memo)
    return memo[num]


if __name__ == "__main__":

    print(getFibonacci(1))
    print(getFibonacci(2))
    print(getFibonacci(3))
    print(getFibonacci(4))
    print(getFibonacci(5))
    print(getFibonacci(6))
    print(getFibonacci(7))
    print(getFibonacci(8))
    print(getFibonacci(9))
    print(getFibonacci(10))

    print(getFibonacci(50))
    print(getFibonacci(500))
    print(getFibonacci(1497))
