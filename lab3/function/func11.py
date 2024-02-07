def is_palindrome(word):
    cleaned_word = ""
    for char in word:
        if char.isalnum():
            cleaned_word += char.lower()
    return cleaned_word == cleaned_word[::-1]

input_word = input()
if (is_palindrome(input_word)):
    print("palindrome")
else:
    print("not palindrome")