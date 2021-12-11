# Q.
# Write a function "bestSum(target_sum, numbers)" that takes in a target_sum and
#   an array of numbers as argument.

# The function should return an array containing the "shortest" combinations of
#   numbers that add up to exactly the target_sum.

# If there is a tie for the shortest combination, you may return any one of the
#   shortest.


# soln:
# m = target_sum, n = len(numbers)

# brute-force version:
# O(n^m * m) time
# O(m^2) space

# memoization version:
# O(n * m^2) time
# O(m^2) space


def bestSum(target_sum, numbers, memo=None):
    if memo == None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    best_result = None
    for num in numbers:
        remainder_result = bestSum(target_sum - num, numbers, memo)

        if remainder_result != None:
            if best_result == None or len(remainder_result) < len(best_result):
                best_result = remainder_result + [num]

    memo[target_sum] = best_result
    return best_result


if __name__ == "__main__":
    print(bestSum(4, [1, 1, 2]))
    print(bestSum(9, [2, 4, 12]))
    print(bestSum(7, [1, 2, 3, 4, 7]))

    print(bestSum(500, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16, 17, 18]))
