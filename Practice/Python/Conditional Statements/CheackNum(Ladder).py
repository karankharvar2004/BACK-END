num = float(input("Enter a number: "))
if num > 0:
   if num % 2 == 0:
       print("Positive even number")
   else:
       print("Positive odd number")
elif num == 0:
   print("Zero")
else:
   if num % 2 == 0:
       print("Negative even number")
   else:
       print("Negative odd number")
