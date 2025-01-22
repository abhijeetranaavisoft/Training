try:
    x = int(input('Input an integer : '))  # Attempt to convert user input to an integer
    print(x)  # Print the integer if conversion is successful
except:
    print('Something went wrong')  # Handle any errors that occur during the try block
else:
    print('nothing went wrong')  # Execute if no exception was raised in the try block
