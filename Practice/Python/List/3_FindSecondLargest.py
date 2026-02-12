# Find second largest element

arr = [50, 40, 70, 60, 20]

if len(arr) < 2:
    print("Not enough elements")
else:
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for i in arr:
        
        # For Largest & Second Largest
        if i > largest:
            second_largest = largest
            largest = i
        elif largest > i > second_largest:
            second_largest = i

        # For Smallest & Second Smallest
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif smallest < i < second_smallest:
            second_smallest = i

    print("Second Largest:", second_largest)
    print("Second Smallest:", second_smallest)
