def reverse_text(text):
    return text[::-1]

def reverse_sentence(sentence):
    s = sentence.split()
    new_sentence = list()
    for text in s:
        new_sentence.append(reverse_text(text))
    return " ".join(new_sentence)


if __name__ == "__main__":
    print(reverse_text("junyiacademy"))
    print(reverse_sentence("flipped class room is important"))
