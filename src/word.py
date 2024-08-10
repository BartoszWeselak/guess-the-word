import random



def pick_word(words):
    print(random.randint(0, len(words)-1))
    return words[random.randint(0, len(words)-1)]