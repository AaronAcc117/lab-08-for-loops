 
sum = 0
numberOfInputs = 4

#  loop  4 times like javascript
for i in range(numberOfInputs):
    user__input = input("Number please: ")
    
    try:
        number = int(user__input)
        sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        i -= 1

# the average
average = sum / numberOfInputs

# results
print(f"The average is {average}")