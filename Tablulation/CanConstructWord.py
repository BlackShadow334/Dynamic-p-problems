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
# O(m^2 * n) time
# O(m) space


def canConstructWord(target_word, word_bank):
    # "" a b c d e f
    table = [False] * (len(target_word) + 1)
    table[0] = True

    for i in range(len(target_word) + 1):
        if table[i]:
            for word in word_bank:
                if (
                    i + len(word) <= len(target_word)
                    and target_word.find(word, i, i + len(word)) == i
                ):
                    table[i + len(word)] = True  # table[i] is True

    return table[len(target_word)]


if __name__ == "__main__":
    print(canConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(
        canConstructWord(
            "aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbdddddddddddddddddd",
            ["cccccccccccc", "bbbb", "aaaaaa", "ea", "ffffff", "dfffffff", "a", "b", "c", "d"],
        )
    )
