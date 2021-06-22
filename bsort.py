def bsort(arr, l):
    #print(' '*12, '0  ', '1  ', '2  ', '3  ', '4  ', '5  ')
    for j in range(len(arr) - 1):
        l = j
        for i in range(l+1, len(arr)):
            #print('l', l, 'i', i, end=' ')
            if arr[l] > arr[i]:
                arr[l], arr[i] = arr[i], arr[l]
            #print('arr', arr, 'l', l, 'i', i)
    print(arr)
bsort([1, 9, 4, 6, 3 ,8 ,8 ,4, 6, 5], 0)
bsort([82, 75, 93, 42, 71, 68, 34, 99, 7], 0)
bsort([-1, 5, 98, 4, 7, 4, -46, 88, 0, -5, -46, 0], 0)
bsort([200, 99, 5, 2, 99, 33, 7,  99, 400], 0)



#
