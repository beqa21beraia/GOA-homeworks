#1
age = int(input('enter your age: '))

for i in range(age):
    print(i)
    
#2
temp_in_cel = int(input('enter temperature in celsius: '))

cel_to_fahr = temp_in_cel * 9/5 + 32

print(f'temperature in Fahrenheit is {cel_to_fahr}')
    
    
#3
#and
numbers = [1, 2, -3, 4]
for num in numbers:
    if num > 0 and num < 5:
        print(f"{num} is between 1 and 5.")

#or
numbers = [0, 5, -1, 10]
for num in numbers:
    if num < 0 or num > 5:
        print(f"{num} is out of the 0-5 range.")


# ==
nums = [1, 2, 3, 4]
for n in nums:
    if n == 3:
        print("Found 3!")

# >
nums = [1, 4, 7, 10]
for n in nums:
    if n > 5:
        print(f"{n} is greater than 5.")



#4
for i in range(7):
    print('*' * i)


#5
age = int(input('enter your age: '))

if age == 20:
    print(True)
else:
    print(False)    