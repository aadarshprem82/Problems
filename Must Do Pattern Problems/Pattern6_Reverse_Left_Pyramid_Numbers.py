def pattern6_reverse_left_pyramid_numbers(num):
    for i in range(num, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print("")

pattern6_reverse_left_pyramid_numbers(5)
pattern6_reverse_left_pyramid_numbers(3)