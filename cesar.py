import string

alphabet = list(2 * (string.ascii_lowercase))


def shift_maker(shift, method):
    shift %= 26
    if method == "d" and shift >= 0:
        shift *= -1
    return shift


def code(word, shift):
    coded_word = ""
    for character in word:
        character = character.lower()
        if character in alphabet:
            shifted_letter = alphabet.index(character) + shift
            character = alphabet[shifted_letter]
        coded_word += character
    return coded_word


shift = shift_maker(6, "d")
print(code("", shift))
