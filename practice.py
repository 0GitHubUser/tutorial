# Write your code here
def qsort(arr):
	p = len(arr) - 1
	i, l = 0, 0	
	
	while i < len(arr):
		
		if arr[p] > arr[i]:
			arr[i], arr[l] = arr[l], arr[i]
			l = l + 1
		i = i + 1

	
	arr[p], arr[l] = arr[l], arr[p]
	p = l
	partition(arr, p)



def partition(arr, p):
    
    if len(arr) < 2 or p < 1:
        return
    qsort(arr[:p])
    if p < len(arr) - 1:
        qsort(arr[p+1:])
        
# Write your code here
def qsort(arr):
	p = len(arr) - 1
	i, l = 0, 0	
	
	while i < len(arr):
		
		if arr[p] > arr[i]:
			arr[i], arr[l] = arr[l], arr[i]
			l = l + 1
		i = i + 1

	
	arr[p], arr[l] = arr[l], arr[p]
	p = l
	partition(arr, p)

def partition(arr, p):
    
    if len(arr) < 2 or p < 1:
        return
    qsort(arr[:p])
    if p < len(arr) - 1:
        qsort(arr[p+1:])
        


arr = [-1, 1, -2, -3, 3, 4, -4, 0, 2]
qsort(arr)
print(arr)