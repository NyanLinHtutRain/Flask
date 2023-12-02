numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
# Ans: 3
print(numbers[-1])
# Ans: 2
print(numbers[3])
# Ans: 1
print(numbers[:-1])
# Ans: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])
# Ans: [1]
print(5 in numbers)
# Ans: True
print(7 in numbers)
# Ans: False
print("3" in numbers)
# Ans: False
print(numbers + [6, 5, 3] )
# Ans: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# Print whether 9 is an element of numbers
print(9 in numbers)
