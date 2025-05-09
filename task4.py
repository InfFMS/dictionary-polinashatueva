# Имеется следующий словарь:
from binascii import b2a_qp

numbers = {'dict1': [11, 20, 30, 17, 6, 24, 90, 15, 17],
          	'dict2': [21, 33, 40, 10, 29, 31, 90, 12],
          	'dict3': [52, 34, 20, 21, 44, 22, 10, 87],
          	'dict4': [22, 54, 29, 21, 70, 88, 99, 34],
          	'dict5': [21, 40, 29, 21, 19, 32, 68, 77],
          	'dict6': [14, 60, 70, 10, 55, 61, 84, 99],
          	'dict7': [45, 80, 12, 23, 42, 22, 37, 90],
          	'dict8': [13, 14, 15, 26, 48, 92, 36, 11],
          	'dict9': [12, 70, 18, 28, 18, 28, 53, 91],
          	'dict10': [29, 79, 18, 28, 18, 28, 32, 55]}
# Напишите программу, которая удалит из значений словаря все четные числа.
a1 = numbers['dict1']
a2 = numbers['dict2']
a3 = numbers['dict3']
a4 = numbers['dict4']
a5 = numbers['dict5']
a6 = numbers['dict6']
a7 = numbers['dict7']
a8 = numbers['dict8']
a9 = numbers['dict9']
a10 = numbers['dict10']
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []
b8 = []
b9 = []
b10 = []
for i in a1:
	if i%2!=1:
		b1.append(i)
for i in a2:
	if i%2!=1:
		b2.append(i)
for i in a3:
	if i%2!=1:
		b3.append(i)
for i in a4:
	if i%2!=1:
		b4.append(i)
for i in a5:
	if i%2!=1:
		b5.append(i)
for i in a6:
	if i%2!=1:
		b6.append(i)
for i in a7:
	if i%2!=1:
		b7.append(i)
for i in a8:
	if i%2!=1:
		b8.append(i)
for i in a9:
	if i%2!=1:
		b9.append(i)
for i in a10:
	if i%2!=1:
		b10.append(i)
print(b1)
n = {1:b1,2:b2,3:b3,4:b4,5:b5,6:b6,7:b7,8:b8,9:b9,10:b10}
print(n)
