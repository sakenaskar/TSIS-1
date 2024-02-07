def solve(numheads, numlegs):
    if numheads == 0 or numlegs % 2 != 0:
        print("No solution")
        return

    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits

    if num_rabbits >= 0 and num_chickens >= 0 and num_rabbits.is_integer() and num_chickens.is_integer():
        print(f"Number of rabbits: {int(num_rabbits)}")
        print(f"Number of chickens: {int(num_chickens)}")
    else:
        print("No solution")

solve(35, 94)