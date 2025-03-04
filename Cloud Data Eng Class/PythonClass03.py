# ## Tuples 
# tup = [2,3,4,5,6,7,8]
# tup[1] = 20
# tup[2] = 30
# tup[3] =40
# tup[5] = 50
# tup[6] = 60
# print(tup[6])
# print(type(tup),tup)


# fruits = ("Apple")
# for i in fruits:
#     print(i)

# for i in range(5):
#     print(i)

# for i in fruits:
#     print(i)

# fnum = int(input("Enter Your First Number:"))
# snum= int(input("Enter Your Second Number:"))

# sum = fnum +snum
# print("sum of two numbers is :",sum)

## NEsted Loop in Python

n = 10
for i in range(n, 0, -1):
    for j in range(n - i):
        print("*", end=" ")
    print()  # This should be outside the inner loop to print a new line after each row

        
