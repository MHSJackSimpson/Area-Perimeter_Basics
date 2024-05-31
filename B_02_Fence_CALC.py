# Ask user for width and loop until they
# enter a number more than zero
def num_checker(question):

    error = "Please enter a number with a value greater than 0\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# main routine goes here

keep_going = ""
while keep_going == "":
    # calculate the area / perimeter
    width = num_checker("width: ")
    length = num_checker("length: ")
    print("NOTE: Do not use a dollar sign")
    cost = num_checker("cost/m:  ")

    perimeter = 2 * (width + length)
    Total_cost = cost * perimeter

    # output the area and perimeter
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Total_Cost: {Total_cost} dollar/s")
    print()

    keep_going = input("Press ENTER to keep going or type no then press enter to quit")
    print()
print("Thank you for using this program :)")
