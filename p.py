
        


# arr = [-1, 1, -2, -3, 3, 4, -4, 0, 2]
# qsort(arr)
# print(arr)

def findValue(numbers, n):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = low + (high - low) // 2
        print(middle)


        if numbers[middle] == n:
            return middle
        elif numbers[middle] < n:
            low = middle + 1
        else:
            high = middle - 1

    return -1
numbers = [1,2,3,4,5,6,7,8,9]
n =4

final = findValue(numbers, n)

if final == -1:
	print("This item was not found in the list.")
else:
	print("The number " + str(n) + " was found at index position " + str(final) + ".")

