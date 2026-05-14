def pattern5_reverse_left_pyramid(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end="")
        print("")

pattern5_reverse_left_pyramid(5)
pattern5_reverse_left_pyramid(3)