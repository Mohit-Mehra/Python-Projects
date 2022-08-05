import random
passlen = int(input("Enter the length of password :- "))
a = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()?"
b = "".join(random.sample(a,passlen))
print(b)