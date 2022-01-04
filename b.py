import os
def fk():
    print('Tim kiem gia tri k trong day so co N chu so')
    k = float(input('k= '))
    n = int(input('N= '))
    if n == 0: 
        exit()
    i = 0
    a = []
    m = 0
    v = []
    print('Nhap day so:')
    while i <= n-1:
        b = float(input(''))
        a.append(b)
        if k == a[i]:
            m = m+1
            v.append(i+1)
        i = i+1
    print('Co',m,'gia tri trong day bang',k,'tai',v)
    os.system('pause')
    fk()
fk()