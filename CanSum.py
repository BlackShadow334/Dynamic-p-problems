# Q.:
# Write a function "canSum(target_sum, numbers)" that takes in a target_sum
#   and a array of numbers as arguments.
# The Function should return a boolean indicating whether or not it is possible
#   to generate the target_sum using numbers from the array.

# You may use an element of the array as many tiems as needed.
# You may assume that all numbers are non-negative.

# Eg: canSum(7, [1, 2, 5, 3, 7]) --> true
# Eg: canSum(7, [2, 4, 9, 6]) --> false


# Soln:
# let m = target_sum, n = array length
# O(n^m) time ---> O(m*n) time because of memoization


def canSum(target_sum, numbers):
    memo = {}
    return memo_canSum(target_sum, numbers, memo)


def memo_canSum(target_sum, numbers, memo):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if memo_canSum(target_sum - num, numbers, memo) == True:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


if __name__ == "__main__":
    print(canSum(7, [2, 5, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(9, [2, 4]))
