# Ask user for width and loop until they
# enter a number more than zero

error = "Please enter a number with a value greater than 0\n"
while True:

    try:
        # ask the user for a number
        widith = float(input("widith: "))

        # check that the number is more than zero
        if widith > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)
