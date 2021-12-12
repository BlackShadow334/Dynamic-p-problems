# Q.:
# Write a function "allConstructWays (target_word, word_bank)" that accepts a target string
#   and an array of strings.

# The function should return a 2D array containing 'all the ways' that the the `target_word` can
#   be constructed by concanating elements of the `word_bank` array. Each element of the the
#   2D array should represent one combination the `target`.

# You may reuse elements of `word_bank` as many times as needed.

# Eg:
# allConstructWays (purple, [purp, p, ur, le, purpl])
#   [
#       [purp, le],
#       [p, ur, p, le]
#   ]


# Soln:
# m = len(target_word), n = len(word_bank)

# ~O(n^m) time
# ~O(n^m) space


from typing import NoReturn


def allConstructWays(target_word, word_bank):
    table = [[] for i in range(len(target_word) + 1)]
    table[0] = [[]]

    for i in range(len(target_word) + 1):
        if table[i] != []:
            for word in word_bank:
                if (
                    i + len(word) <= len(target_word)
                    and target_word.find(word, i, i + len(word)) == i
                ):
                    current_ways = table[i].copy()
                    for j in range(len(current_ways)):
                        current_ways[j] = current_ways[j] + [word]
                    table[i + len(word)] = table[i + len(word)] + current_ways

    return table[len(target_word)]


if __name__ == "__main__":
    print(allConstructWays("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstructWays("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
