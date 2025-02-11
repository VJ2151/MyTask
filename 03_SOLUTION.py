# The 3rd smallest number in an array:


arr = list(map(int, input("Enter numbers separated by space: ").split()))  
arr = sorted(set(arr))  

if len(arr) < 3:  
    print("Not enough unique numbers")  
else:  
    print("3rd smallest number:", arr[2])  
