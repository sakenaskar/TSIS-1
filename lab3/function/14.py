from func11 import is_palindrome
from func9 import sphere_volume

input_word = input()

radius = int(input())

if (is_palindrome(input_word)):
    print("palindrome")
else:
    print("not palindrome")

print(sphere_volume(radius))