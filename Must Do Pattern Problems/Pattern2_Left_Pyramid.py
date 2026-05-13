def pattern2_left_pyramid(num):
    for i in range(num):
        for _ in range(0, i+1):
            print("*", end="")
        print("")

pattern2_left_pyramid(2)
pattern2_left_pyramid(3)