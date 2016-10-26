'''
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.
'''

'''
Referred articles:
    http://www.geeksforgeeks.org/array-rotation/
'''

def GCD(a, b):
    if(b == 0):
        return a
    else:
        return GCD(b, a%b)



def array_left_rotation(array, numElements, numRotations):
    gcd = GCD(numElements, numRotations)
    for i in range(gcd):
        j = i
        temp = array[i]
        while 1:
            k = j + numRotations
            if(k >= numElements):
                k = k - numElements
            if(k == i):
                break
            array[j] = array[k]
            j = k
        array[j] = temp
    return array



n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
