from cs50 import get_float


# Prompt user for input
while True:
    dollars = get_float("Change owed: ")
    # Reprompt if input is less than or equal to 0
    if dollars > 0:
        break

# Convert dollars to cents and round up
cents = round(dollars * 100)

while True:
    firstcoins = cents / 25
    firstremainder = cents % 25
    if firstremainder < 25:
        break
# If there is no remainder after dividing by 25, do the following:
if firstremainder == 0:
    firstcoins = int(firstcoins)
    print(firstcoins)

elif firstremainder != 0:
    while True:
        secondremainder = firstremainder % 10
        i = int(firstremainder / 10)
        secondcoins = int(firstcoins) + i
        if secondremainder < 10:
            break
        # If there is no remainder after dividing by 10, do the following:
    if secondremainder == 0:
        print(int(secondcoins))
    elif secondremainder != 0:
        while True:
            thirdremainder = secondremainder % 5
            j = secondremainder / 5
            thirdcoins = secondcoins + j
            if thirdremainder < 5:
                break
        # If there is no remainder after dividing by 5, do the following:
        if thirdremainder == 0:
            print(int(thirdcoins))

        else:
            while True:
                fourthremainder = thirdremainder % 1
                k = thirdremainder / 1
                fourthcoins = thirdcoins + k
                if fourthremainder < 1:
                    break
            print(int(fourthcoins))
