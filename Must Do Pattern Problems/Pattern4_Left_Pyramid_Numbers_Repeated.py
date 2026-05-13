def pattern4_left_pyramid_numbers_repeated(n):
    for i in range(1, n+1):
        for _ in range(1,i+1):
            print(i, end="")
        print("")

pattern4_left_pyramid_numbers_repeated(5)
pattern4_left_pyramid_numbers_repeated(3)