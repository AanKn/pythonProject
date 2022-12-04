import numpy
a = numpy.arange(25).reshape(5, 5)
print(a)
for i in range(5):
    k = i
    x = ''
    for j in range(5-i):
        x += str(a[j][k])
        k += 1
    print(x)
for i in range(4):
    k = i + 1
    for j in range(4-i):
        print(a[k][j])
        k += 1
