

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
