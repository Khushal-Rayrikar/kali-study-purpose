a = int(input("guess the number from 1-10 :  "))
b = a + 2
c = [9,4,6]
if b > 9 :
    print(b +2)
elif b == c :
    print("Good!!!")
else :
    b += 1
    print(b)