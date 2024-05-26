noi_dung = []
with open('E:/code_python/qua_trinh_train.txt',  'r') as file:
    noi_dung = file.readlines()

for i in range(len(noi_dung)):
    noi_dung[i] = noi_dung[:-1]
print(noi_dung)
print('hoan thanh')