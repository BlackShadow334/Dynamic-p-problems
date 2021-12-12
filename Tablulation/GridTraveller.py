# Q.:
# Say that you are a traveler on a 2D grid.
# You begin in top-left corner and your goal is to travel to the bottom-right corner.
# You can only move down or right.

# In how mny ways can you travel to the goal on a grid with dimension m * n ?

# Write a function "gridTraveler(m, n)" that calculates number of ways.


# Soln:


def gridTraveller(m, n):

    grid = [[0 for i in range(n + 1)] for j in range(m + 1)]
    grid[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):

            # adding for right
            if j + 1 <= n:
                grid[i][j + 1] += grid[i][j]
            # adding for down
            if i + 1 <= m:
                # print(i + 1)
                grid[i + 1][j] += grid[i][j]

    # print(grid)
    return grid[m][n]


if __name__ == "__main__":
    print(gridTraveller(3, 3))
    print(gridTraveller(6, 9))
