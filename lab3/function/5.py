def print_permutations(input_string, prefix=""):
    if not input_string:
        print(prefix)
    else:
        for i in range(len(input_string)):
            new_prefix = prefix + input_string[i]
            new_remaining = input_string[:i] + input_string[i+1:]
            print_permutations(new_remaining, new_prefix)

user_input = input()

print_permutations(user_input)