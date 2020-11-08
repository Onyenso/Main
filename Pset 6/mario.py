from cs50 import get_int
# repeat while input is invalid
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
# draw pyramid
i = height
while i > 0:
    for j in range(i - 1):
        print(" ", end="")
    for k in range(i - (i - 1)):
        for l in range(height - (i - 1)):
            print("#", end="")
        print()
    i = i - 1
