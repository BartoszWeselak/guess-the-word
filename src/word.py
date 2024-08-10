import random




def pick_word():
    words = [
        "butterfly",
        "mountain",
        "astronomy",
        "puzzle",
        "elephant",
        "umbrella",
        "computer",
        "library",
        "mystery",
        "sunshine",
        "penguin",
        "airplane",
        "bicycle",
        "fireworks",
        "jellyfish",
        "volcano",
        "rainbow",
        "sandcastle",
        "skeleton",
        "spaceship"
    ]

    print(random.randint(0, len(words)-1))
    return words[random.randint(0, len(words)-1)]