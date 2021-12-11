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

# Brute-force verion:
# O(n^m * m) time
# O(m^2)

# memoized verion:
# O(n * m^2) time
# O(m ^2) spacer


def countConstructWord(target_word, word_bank, memo=None):
    if memo == None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    if target_word == "":
        return 1

    count = 0
    for word in word_bank:
        if target_word.find(word) == 0:
            remaining_word = target_word[len(word) :]
            ways_for_rest = countConstructWord(remaining_word, word_bank, memo)
            count += ways_for_rest

    memo[target_word] = count
    return count


if __name__ == "__main__":
    print(countConstructWord("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstructWord("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstructWord("", ["cat", "dog", "eagle"]))
    print(countConstructWord("apple", ["ap", "p", "le", "a", "app"]))
    print(
        countConstructWord("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    )
    print(
        countConstructWord(
            "dog-cat", ["cat", "dog", "-", "ca", "do", "t", "g", "c", "a", "d", "g"]
        )
    )

    print(
        countConstructWord(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ["a", "aa", "aaa", "aaaa", "aaaaa"],
        )
    )
