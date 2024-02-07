def reverse_words(sentence):
    reversed_words = reversed(sentence.split())
    reversed_sentence = ""
    for word in reversed_words:
        reversed_sentence = reversed_sentence + word + " "
    return reversed_sentence

user_input = input()

print(reverse_words(user_input))