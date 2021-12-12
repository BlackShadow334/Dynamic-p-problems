# Write a function "allConstructWays (target_word, word_bank)" that accepts a target string
#   and an array of strings.

# The function should return a 2D array containing 'all the ways' that the the `target_word` can
#   be constructed by concanating elements of the `word_bank` array. Each element of the the
#   2D array should represent one combination the `target`.

# You may reuse elements of `word_bank` as many times as needed.

# Eg:
# allConstructWays (purple, [purp, p, ur, le, purp])
#   [
#       [purp, le],
#       [p, ur, p, le]
#   ]


# Soln:
# m = len(target_word), n = len(word_bank)

# Brute-force verion:
# O(n^m * m^2) time      ???
# O(m) space

# memoized version:
# O(n^m) time
# O(m) space


def allConstructWays(target_word, word_bank, memo=None):
    if memo == None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    if target_word == "":
        return [[]]

    ways = []

    for word in word_bank:
        if target_word.find(word) == 0:
            remaining_word = target_word[len(word) :]
            remaining_ways = allConstructWays(remaining_word, word_bank, memo)

            for i in range(len(remaining_ways)):
                remaining_ways[i] = [word] + remaining_ways[i]

            ways += remaining_ways

    memo[target_word] = ways
    return ways


if __name__ == "__main__":
    print(allConstructWays("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstructWays("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(allConstructWays("", ["cat", "dog", "eagle"]))
    print(allConstructWays("apple", ["ap", "p", "le", "a", "app"]))
    print(allConstructWays("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

    print(
        allConstructWays(
            "aaaaaaaaaaaaaaaaaaaaaa",
            ["a", "aa", "aaa", "aaaa", "aaaaa"],
        )
    ) 
    # wow, this has so many combinations.....it goes way beyond my shell's max limit.
    # It keeps printing combination for more than five minutes....!