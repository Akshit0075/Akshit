#write a python program to demonstate any build in function
user_input = input("Enter a list of numbers seperated by spaces")
input_list = user_input.split()
numbers = list(map(int, input_list))
total = sum(numbers)
length = len (numbers)
sorted_numbers = sorted(numbers)
print(f"Orignal list of numbers:{numbers}")
print(f"Sum of numbers:{total}")
print(f"Number of elements:{length}")
print(f"Sorted list of numbers:{sorted_numbers}")
print("THIS PROGRAM IS WRITTEN BY Akshit Trikha ERP :- 0221BCA008")