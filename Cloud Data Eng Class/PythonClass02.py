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