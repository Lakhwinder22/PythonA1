a = 10

if a > 10 :
    print("a is greater than 10")
elif a == 10:
    print('a is equal to 10')
else :
    print("a is less than 10")


#  there are students marks out of 50, you have to print the grades accordly  
# 40 to 50 = A
# 30 to 40 = B
# 20 to 30 = C
# 10 to 20 = D
# 0 to 10 = E 
 

marks = int(input("Enter your marks"))

if marks >= 40 and  marks <=50:
    print("A")
elif marks >= 30 and marks <=40:
    print("B")
elif marks >= 20 and marks <=30:
    print("C")
elif marks >= 10 and marks <=20:
    print("D")
elif marks >= 0 and marks <=10:
    print("E")
else: print("invaild marks")