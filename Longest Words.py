def longest_word(text):
    words = list(text.split())
    longest = sorted(words, key = len)
    return longest[-1]


longest_word("We want a SHRUBBERY")