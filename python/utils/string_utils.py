

def word_score(word):
    """
    Returns the sum of the ascii values of the letters composing the word.
    Only works on uppercase words.
    """
    # 64 = ord('A')
    total = 0
    for letter in word:
        total += ord(letter) - 64

    return total


def ascii_sum(data):
    total = 0
    for char in data:
        total += ord(char)

    return total
