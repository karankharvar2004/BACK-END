# Fibonacci Series (N Terms)

def fibonacci(n):
    if n <= 0:
        print("Enter a positive number")
        return
    
    a, b = 0, 1
    
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter number of terms: "))
fibonacci(num)
