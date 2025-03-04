# from pytest import mark
# mark = int(input("Enter Your Number:"))

# if mark >=80 and mark <=100:
#     print("A")
# elif mark >=70 and mark <80:
#     print("B")
# elif mark >=60 and mark <70:
#     print("C")
# elif mark >=45 and mark <60:
#     print("D")
# elif mark >=25 and mark <45:
#     print("E")
# elif mark <25:
#     print("F")
# else:
#     print("Invalid number")

# ## Write a Program For Checking Three Input That Is Age , gender and martial status for thier job in respectives areas

# gender = input("Enter Your Gender M/F:")
# age = int(input("Enter Your Age:"))
# martial_status = input("Enter Your Martial Status")

# if gender == "F":
#     print("You can work Only in Urban areas")
# elif age >=20 and age <=40:
#     print("You can work anyWhere")
# elif age > 40 and age <=60 :
#     print ("YOu can Work Any Where")
# else:
#     print("error")


# # More on Python

# age = int (input("Enter Your age :"))
# gender = input("enter Gender M/F:")
# martial_status= input("Enter YOur Martial Status Y/ :")

# if gender == "Male" and age >=20 and age<=40:
#     print("You Can work anyWhere")
# elif gender == "Female" and martial_status == "yes":
#     print("You can Work In Urban areas Only")
# else:
#     print("error")


# condition 1 or  condition 2 (any one condition should be true) - freshness
# condition 1 and condition 2 (both condition should be  true) -All Vigitables


# List Topic

# Print Append and Sllice  (in Slice There are tow Aurgument Pass with positon then Koma Then String) & in append only one aurgument May Pass In String Form
countries = [
    "Pakistan",
    "India",
    "Bangladesh",
    "Sri Lanka",
    "Nepal",
    "Bhutam"
]
countries.append("Assis")

countries.append("New Xealand")
print(countries)


list_of_fruits = [
    "Apple",
    "Banana",
    "MAngo",
    "Pine Apple",
    "Big Aplle",
     "Peach",
]
list_of_fruits.insert(10,"Grapes")

list_of_fruits.insert(11,"watermillion")
print(list_of_fruits)

##  Lists: Taking slices out of them

list_of_cities = ["Karachi", "Hyderabad", "Sakker", "Lahore","Islamabad", "Peshawer"]
print(list_of_cities[0:4]) # it Will Print From Zeroth to LAhorer
print(list_of_cities[:4]) # same as Above
print(list_of_cities[3:4]) # it wil Only Print The LAst before 4 th Element
print(list_of_cities[2:]) # it will print from second Element Till last Element

# Deleting and Removing Elements From The List

list_of_brands = ["apple", "sumsung", "nokia", "hwawei", "oppo", "vivo", "realme"] 
del list_of_brands[0]
del list_of_brands[1]
print(list_of_brands)

## Removing

list  = [1,2,3,4,5]
list.remove(1)





