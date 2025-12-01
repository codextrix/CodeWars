def spin_words(sentence_):
    words = sentence_.split()
    spined = []
    for word in words:
        if len(word) >= 5:
            new_word = word[::-1]
            spined.append(new_word)

        else:
            spined.append(word)

    return f"{' '.join(spined)}"

sentence = input()
print(spin_words(sentence))
