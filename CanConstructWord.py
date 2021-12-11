# Q.
# Write a function "canConstructWord (target_word, word_bank)" that accepts a
#   target_word and an array of strings.

# The function should return a boolean indicating whether or the "target_word"
#   can be constructed by concatenating elements of the "word_bank" array.

# You may reuse elements of "word_bank" as many times as needed.

# Eg:
# canConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]) --> True
# canConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) --> False
# canConstructWord("", ["cat", "dog", "eagle"]) --> True


# Soln:
# m = len(target_word), n = len(word_bank) = number of words in word_bank

# Brute-force verion:
# O(n^m * m) time
# O(m^2) space

# Memoized version:
# O(m^2 * n) time
# O(m^2) space


def canConstructWord(target_word, word_bank, memo=None):
    if memo == None:
        memo = {}
    if target_word in memo:
        return memo[target_word]

    if target_word == "":
        return True

    for word in word_bank:
        if target_word.find(word) == 0:
            remaining_word = target_word[len(word) :]

            if canConstructWord(remaining_word, word_bank, memo):
                memo[target_word] = True
                return True

    memo[target_word] = False
    return False


if __name__ == "__main__":
    print(canConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

    print(
        canConstructWord(
            "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbdddddddddddddddddd",
            ["cccccccccccc", "bbbb", "aaaaaa", "ea", "ffffff", "dfffffff", "a", "b", "c", "d"],
        )
    )
