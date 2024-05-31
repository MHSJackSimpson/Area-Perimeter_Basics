# Ask user for width and loop until they
# enter a number more than zero
def num_checker (question):

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
for item in range(0, 2):
    widith = num_checker("widith: ")
    print(widith)

print()

for item in range(0, 2):
    height = num_checker("height: ")
    print(height)
