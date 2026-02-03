list = [56 , 27 , 65 , 13 , 90]

# n=len(list)

# for i in range(0,n-1):
#     for j in range(0,n-1):
#         if list[j]>list[j+1]:
#             temp=list[j]
#             list[j]=list[j+1]
#             list[j+1]=temp

# print(list)

# print(list[0])
# print(list[n-1])

min_val=list[0]
max_val=list[0]

for i in list:
    if i<min_val:
        min_val=i
    if i>max_val:
        max_val=i
        
print(min_val)
print(max_val)




    


