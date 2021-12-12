# Q.
# Write a function "bestSum(target_sum, numbers)" that takes in a target_sum and
#   an array of numbers as argument.

# The function should return an array containing the "shortest" combinations of
#   numbers that add up to exactly the target_sum.

# If there is a tie for the shortest combination, you may return any one of the
#   shortest.


# soln:
# m = target_sum, n = len(numbers)

# O(m^2 * n) time
# O(m^2)


def bestSum(target_sum, numbers):
    best_sums = [None] * (target_sum + 1)
    best_sums[0] = []

    for i in range(target_sum + 1):
        if best_sums[i] != None:
            for num in numbers:
                if i + num <= target_sum:
                    next_sum = best_sums[i] + [num]
                    if best_sums[i + num] == None or len(next_sum) < len(
                        best_sums[i + num]
                    ):
                        best_sums[i + num] = next_sum

    return best_sums[target_sum]


if __name__ == "__main__":
    print(bestSum(4, [1, 1, 2]))
    print(bestSum(9, [2, 4, 12]))
    print(bestSum(7, [1, 2, 3, 4, 7]))

    print(bestSum(500, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
