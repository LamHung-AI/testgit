try:
    a = int(input('a = '))
    b = int(input('b = '))
    k = a/b
except ValueError as ex:
    print('So vua nhap khong phai la so nguyen: '+str(ex))
except ZeroDivisionError as ex:
    print('b = 0: Loi khong chia duoc so 0: '+str(ex))
else:
    print(k)
