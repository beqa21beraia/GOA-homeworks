# 1
age = int(input('რამდენი წლის ხარ: '))

print(13 < age < 19)



# 2
mark = int(input('ნუგზარ რა ნიშანი მიიღე: '))

is_A = 9 <= mark
is_B = 8 <= mark < 9
is_C = 7 <= mark < 8
is_D = 6 <= mark < 7
is_F = 6 > mark

print(is_A, is_B, is_C, is_D, is_F)


# 3
a = True
b = False

print(a and b)
print(a and a)
print(b and b)
print(a or b)
print(a or a)
print(b or b)



# 4
num1 = int(input('შეიყვანე ნებისმიერი მთელი რიცხვი: '))
num2 = int(input('შეიყვანე მეორე ნებისმიერი მთელი რიცხვი: '))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)



# 5
a = 21
b = 15
c = 32

is_a_greatest = a > b and a > c
is_b_middle = a < b < c or a > b > c
is_c_least = c < a and c < b

print(is_a_greatest, is_b_middle, is_c_least)


# 6
score = 54

is_pass = 50 < score
is_high_pass = 75 < score < 90
is_perfect = 100 == score
is_failing = 50 > score



# 7
P = True
Q = False

P_and_not_Q = P == True and Q == False
not_P_and_Q = P == False and Q == True
P_xor_Q = P ^ Q 