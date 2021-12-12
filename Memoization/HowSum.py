# Q.
# Write a function "howSum(target_sum, numbers)" that takes in a targetSum and
#   an array of numbers as arguments.

# The function should return an array containing any combination of elements that
#   add up to exactly the targetSum.
# If there is no combination that adds up to the targetSun, then return null.

# If there are multiple combinations possible, you may return any single one.


# soln;
# m = target_sum, n = len(numbers)

# brute force version
# O(n^m * m) time
# O(m) space

# memoized version
# O(n * m^2) time
# O(m^2) space


def howSum(target_sum, numbers, memo=None):
    if memo == None: memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder_result = howSum(target_sum - num, numbers, memo)
        if remainder_result != None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]
    memo[target_sum] = None
    return None


if __name__ == "__main__":
    print(howSum(7, [2, 3, 5, 7]))
    print(howSum(7, [2, 4, 6]))
    print(howSum(87, [2, 3, 5, 7]))
    print(howSum(201, [7, 3, 5, 2]))
    print(howSum(1801, [7, 3]))
