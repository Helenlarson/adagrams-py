from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    pool_list = []

    for letter, qty in LETTER_POOL.items():
        for _ in range(qty):
            pool_list.append(letter)  

    hand = []
    for _ in range(10):
        idx = randint(0, len(pool_list) -1)
        hand.append(pool_list.pop(idx))

    return hand


def uses_available_letters(word, letter_bank):
    counts = {}
    for ch in letter_bank:
        ch = ch.upper()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    for ch in word.upper():
        if ch not in counts or counts[ch] == 0:
            return False
        counts[ch] -= 1
    return True

def score_word(word):
    if word == "":
        return 0
    
    one = "AEIOULNRSTT"
    two = "DG"
    three = "BCMP"
    four = "FHVWY"
    five = "K"
    eight = "JX"
    ten = "QZ"

    total = 0
    for ch in word.upper():
        if ch in one:
            total += 1
        elif ch in two:
            total += 2
        elif ch in three:
            total += 3
        elif ch in four:
            total += 4
        elif ch in five:
            total += 5
        elif ch in eight:
            total += 8
        elif ch in ten:
            total += 10
        else:
            total += 0

    length = 0 
    for _ in word:
        length+= 1
    if length >= 7 and length <= 10:
        total += 8

    return total

def get_highest_word_score(word_list):
    if not word_list:
        return ("", 0)
    
    best_word = None
    best_score = -1
    best_len = 0
    best_index = -1

    i = 0
    while i < len(word_list):
        word = word_list[i]
        score = score_word(word)
        wlen = len(word)

        if score > best_score:
            best_word = word
            best_score = score
            best_len = wlen
            best_index = i

        elif score == best_score:
            if wlen == 10 and best_len != 10:
                best_word = word 
                best_len = wlen
                best_index = i
            elif best_len == 10 and wlen != 10:
                pass
            else:
                if wlen < best_len:
                    best_word = word 
                    best_len = wlen
                    best_index = i
                elif wlen == best_len:
                    pass

        i += 1

    return (best_word, best_score)