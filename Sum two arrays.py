def sum_arrays(array1,array2):
    if array1 == []:
        return array2
    if array2 == []:
        return array1
    array1 = [str(int) for int in array1]
    array2 = [str(int) for int in array2]
    a = ''.join(array1)
    b = ''.join(array2)
    if int(a) + int(b) == 0:
        return []
    if int(a)+int(b) < 0:
        array3 = []
        array3.append(-1*int(str(int(a)+int(b))[1]))
        for i in range(2,len(str(int(a)+int(b)))):
            array3.append(int(str(int(a)+int(b))[i]))
        return array3
    else:
        array3 = [int(x) for x in str(int(a)+int(b))]
        return array3
    pass
