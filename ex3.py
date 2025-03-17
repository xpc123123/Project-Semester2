import random

a=random.randint(10,20)

b=0
while b!=a:


   b=int(input("the number you guess is(from 10 to 20):")) 
   if b>a:
       print("too big.")
   elif b<a:
       print("too small")
   else:
       break
print("you gess the right number.")

