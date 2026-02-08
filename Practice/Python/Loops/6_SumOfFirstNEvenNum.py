# Sum of even numbers till N

num = int(input("Enter Your Number: "))

sum = 0

# for i in range(1,num+1):
#     if i % 2 == 0:
#         sum += i

# print(sum)

i = 1
while i<=num:
    if i % 2 ==0:
        sum +=i
    i += 1
print(sum)

