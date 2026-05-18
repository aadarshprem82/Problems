def pattern8_reverse_triangle(num):
    for i in range(num-1, -1, -1):
        spaces = num - i - 1
        stars = i * 2 + 1
        for _ in range(spaces):
            print(" ", end="")
        for _ in range(stars):
            print("*", end="")
        print("")

pattern8_reverse_triangle(5)
pattern8_reverse_triangle(3)