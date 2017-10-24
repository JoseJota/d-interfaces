def gcdIter(a, b):
    while (b != 0):
        (a, b) = (b, a % b)
    return a
print (gcdIter(64,12))