def mergeArrays (arr1,arr2,length1,length2,finalLength):
    additionlength = (length1 + length2) - 1

    if additionlength < finalLength:
        finalLength = additionlength
    arr3 = [None] * (finalLength)
    i = 0
    j = 0
    k = 0

    while i < length1 and j < length2 and k < finalLength:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    print(arr3)



arr1 = (-2, 0, 5,6,11)
arr2 = (-1, 1,3,10)
length1 = len(arr1)
length2 = len(arr2)
finalLength = 10

mergeArrays(arr1,arr2,length1, length2, finalLength)


    # List 1 = (-2, 0, 5,6,11)
    # List 2 = (-1, 1,3,10)
    # Length 5
    # (-2, -1,0,1,3)
