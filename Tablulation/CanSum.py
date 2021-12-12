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

# O(m * n) time
# O(m) space


def canSum(target_sum, numbers):
    can_sums = [False] * (target_sum + 1)
    can_sums[0] = True

    for i in range(target_sum + 1):
        if can_sums[i]:
            for num in numbers:
                if i + num <= target_sum:
                    can_sums[
                        i + num
                    ] = True  # can_sums[i] is true, because we already checked.

    return can_sums[target_sum]


if __name__ == "__main__":
    print(canSum(7, [1, 2, 5, 3, 7]))
    print(canSum(7, [2, 4, 9, 6]))
