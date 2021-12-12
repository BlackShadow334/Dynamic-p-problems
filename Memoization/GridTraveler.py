# Q.:
# Say that you are a traveler on a 2D grid.
# You begin in top-left corner and your goal is to travel to the bottom-right corner.
# You can only move down or right.

# In how mny ways can you travel to the goal on a grid with dimension m * n ?

# Write a function "gridTraveler(m, n)" that calculates number of ways.


# Soln:
# let m = row, n = column
# so, (m - 1) is down & (n - 1) is right
# using memo changes time complexity O(2^(n+m)) to O(n * m)
# space complexity 0(m + n)


def gridTraveler(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[(m, n)] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

    # ways to travel from (1, 2) and (2, 1) are same. ie order doesn't matter.
    memo[(n, m)] = memo[(m, n)]
    return memo[(m, n)]


if __name__ == "__main__":
    print(gridTraveler(1, 0))
    print(gridTraveler(1, 1))
    print(gridTraveler(2, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(4, 2))
    print(gridTraveler(3, 4))
    print(gridTraveler(30, 40))
