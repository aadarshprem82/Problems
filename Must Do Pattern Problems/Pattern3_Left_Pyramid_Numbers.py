def pattern3_left_pyramid_numbers(num):
    for i in range(1,num+1):
        for j in range(1, i+1):
            print(j, end="")
        print("")

pattern3_left_pyramid_numbers(3)
pattern3_left_pyramid_numbers(5)