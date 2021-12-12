# Q.
# Write a function "howSum(target_sum, numbers)" that takes in a targetSum and
#   an array of numbers as arguments.

# The function should return an array containing any combination of elements that
#   add up to exactly the targetSum.
# If there is no combination that adds up to the targetSun, then return null.

# If there are multiple combinations possible, you may return any single one.


# soln;
# m = target_sum, n = len(numbers)

# O(m^2 * n) time
# O(m^2) space


def howSum(target_sum, numbers):
    how_sums = [None for i in range(target_sum + 1)]
    how_sums[0] = []

    for i in range(target_sum + 1):
        if how_sums[i] != None:
            for num in numbers:
                if i + num <= target_sum:
                    how_sums[i + num] = how_sums[i] + [num]

    return how_sums[target_sum]


if __name__ == "__main__":
    print(howSum(7, [0, 3, 5, 7, 0]))
    print(howSum(7, [2, 4, 6]))
    print(howSum(87, [2, 3, 5, 7]))
    print(howSum(201, [7, 3, 5, 2]))
    print(howSum(1801, [7, 3]))
