from pytest import mark
mark = int(input("Enter Your Number:"))

if mark >=80 and mark <=100:
    print("A")
elif mark >=70 and mark <80:
    print("B")
elif mark >=60 and mark <70:
    print("C")
elif mark >=45 and mark <60:
    print("D")
elif mark >=25 and mark <45:
    print("E")
elif mark <25:
    print("F")
else:
    print("Invalid number")

## Write a Program For Checking Three Input That Is Age , gender and martial status for thier job in respectives areas

gender = input("Enter Your Gender M/F:")
age = int(input("Enter Your Age:"))
martial_status = input("Enter Your Martial Status")

if gender == "F":
    print("You can work Only in Urban areas")
elif age >=20 and age <=40:
    print("You can work anyWhere")
elif age > 40 and age <=60 :
    print ("YOu can Work Any Where")
else:
    print("error")


# More on Python

age = int (input("Enter Your age :"))
gender = input("enter Gender M/F:")
martial_status= input("Enter YOur Martial Status Y/ :")

if gender == "Male" and age >=20 and age<=40:
    print("You Can work anyWhere")
elif gender == "Female" and martial_status == "yes":
    print("You can Work In Urban areas Only")
else:
    print("error")


# condition 1 or  condition 2 (any one condition should be true) - freshness
# condition 1 and condition 2 (both condition should be  true) -All Vigitables


# List Topic
#list Of COuntries

countries = [
    "Pakistan",
    "India",
    "Bangladesh",
    "Sri Lanka",
    "Nepal",
    "Bhutam"
]

print(countries)

countries.append("Ausis")


