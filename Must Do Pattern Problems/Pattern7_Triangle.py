def pattern7_triangle(num):
    oddIndex = 1
    for i in range(num, 0, -1):
        for _ in range(i):
            print(" ", end="")
        print("*" * oddIndex)
        oddIndex += 2

pattern7_triangle(5)
pattern7_triangle(3)