# Python program to swap two variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')
z = input('Enter value of z: ')

# create a temporary variable and swap the values
temp = x
x = y
y = z
z = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('The value of z after swapping: {}'.format(z))
