#1
birth_year = int(input('enter your birth year: '))

age = 2024 - birth_year

print(f'your age is {age}')


#2
length = int(input('შეიყვანე ოთხკუთხედის სიგრძე: '))
width = int(input('შეიყვანე ოთხკუთხედის სიგანე: '))

S = length * width
P = 2*(length + width)

print(f'ოთხკუთხედის ფართობია {S}, ხოლო პერიმეტრი {P}')


#3
distance = int(input('შეიყვანე მანძილი შენი სახლიდან სკოლამდე კილომეტრებში: '))

in_meters = distance * 1000
in_centimeters = distance * 100000
in_millimeters = distance * 1000000

print(f'შენი მანძილი მეტრებში: {in_meters} | სანტიმეტრებში: {in_centimeters} | მილიმეტრებში: {in_millimeters}')



# 4
name = input('enter your name: ')
surname = input('enter your surname: ')
parent_name = input('enter your parents name: ')
parent_surname = input('enter your parents surname: ')
fav_color = input('enter your favourite color: ')
fav_car = input('enter your favourite car brand: ')
fav_hobby = input('what is your favourite hobby: ')

info = f'შენი სახელი და გვარია {name} {surname}, მშობლის სახელი და გვარია {parent_name} {parent_surname}, შენი საყვარელი ფერია {fav_color}, ხოლო მანქნებიდან მოგწონს {fav_car}, ასევე გიყვარს {fav_hobby}'

print(info)



#5
number = int(input('შეიყვანე ორნიშნა რიცხვი: '))

ateuli = number // 10
erteuli = number % 10
sum_num = ateuli + erteuli

print(sum_num)