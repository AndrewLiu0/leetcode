# A quick syntax reference



## Math
# Division is decimal by default
print(5/2)

# Double slash rounds down
print(5//2)

# Rounds down, even for negatives
print(-3//2)
# Workaround
print(int(-3/2))

# Max / Min Int
float("inf")
float("-inf")


## Arrays
arr = [1,2,3]
print(arr)

# Can be used as a stack
arr.append(4) # push
arr.pop()

arr.insert(1,7) # O(n)
# Last value
print(arr[-1]) 

n = 5
arr = [1] * 5

# Slicing array, sublists
arr = [1,2,3,4]
print(arr[1:3])

#Unpacking
a, b, c = [1,2,3] # left side must match right side

# Loop through arrays
for i in range(len(arr)):
    print(arr[i])

# Without index
for n in arr:
    print(n)

# With index and value
for i, n in enumerate(arr):
    print(i,n)

# 