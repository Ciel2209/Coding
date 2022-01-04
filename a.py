import os
def fmax():
    a = []
    print('Tim gia tri lon nhat cua day so nguyen co N chu so')
    n = int(input('N= '))
    i = 0
    max = 0
    if n == 0:
        print('ERROR')
        fmax()
    print('Nhap day so: ')
    while i <= n-1:
        b = float(input(''))
        a.append(b)
        if i == 0:
            max = a[0]
        if a[i] > max:
            max = a[i]
        i = i+1
    print('Gia tri lon nhat cua day so la: ',max)
    os.system('pause')
    fmax()
fmax()