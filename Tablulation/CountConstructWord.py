# Q.
# Write a function "countConsturctWord (target_word, word_bank)" that accepts a
#   target string and an array of strings.

# The function should return the number of ways that the "target_word" can be
#   constructed by concatenating elements of the "word_bank" array.

# You must reuse elements of "word_bank" as many times as needed.

# Eg:
# countConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]) --> 1
# countConstructWord("purple", ["purp", "p", "ur", "le", "purpl"]) --> 2
# countConstructWord("", ["cat", "dog", "eagle"]) --> 1
# countConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) --> 0

# Soln:
# m = len(target_word), n = len(word_bank) = number of words in word_bank

# O(m^2 * n) time
# O(m) space


def countConstructWord(target_word, word_bank):
    table = [0] * (len(target_word) + 1)
    table[0] = 1

    for i in range(len(target_word) + 1):
        if table[i] != 0:
            for word in word_bank:
                if (
                    i + len(word) <= len(target_word)
                    and target_word.find(word, i, i + len(word)) == i
                ):
                    table[i + len(word)] += table[i]

    return table[len(target_word)]


if __name__ == "__main__":
    print(countConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstructWord("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstructWord("", ["cat", "dog", "eagle"]))
    print(
        countConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    )
    print(
        countConstructWord(
            "dog-cat", ["cat", "dog", "-", "ca", "do", "t", "g", "c", "a", "d", "g"]
        )
    )
