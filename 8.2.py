try:
    print('Nhap do dai ba canh tam giac: ')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    if (a*b*c<=0):
        raise ValueError('Do dai canh tam giac phai >0')
    if (a>=b+c or b>=a+c or c >= a+ b):
        raise ValueError('a, b, c khong phai la ba canh cua tam giac!')
except ValueError as e:
    print('loi: '+str(e))
else:
    print('la ba canh cua tam giac')

