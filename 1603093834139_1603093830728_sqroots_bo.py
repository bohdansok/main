import sys
from datetime import datetime

print("Введіть коефіцієнти квадратного рввняння виду ах^+вх+с=0:")
a = float(input("а="))
b = float(input("b="))
c = float(input("c="))
Now = datetime.now()
time = Now.strftime("%H:%M:%S.%mS")
print("Початок обчислень о ",time)
if a == 0 and b == 0:
	print("Це не рівняння")
	sys.exit("Кінець всім сподіванням!")
if a == 0 and b != 0:
	print("Це не квадратне рівняння, корінь Х=",-1 * c  / b)
	sys.exit("Отаке.")
D = float(b ** 2 - 4 * a * c)
if D < 0:
	print("Рівняння не має дійсних коренів, дескримінант (", D,") менше нуля")
elif D == 0:
	print("Рівняння має два однакових кореня, Х=",-0.5 * b / a)
else:
	print("Рівняння має два кореня:")
	print("X1=",(-1 * b + (D ** 0.5)) / (2 * a))
	print("X2=",(-1 * b - (D ** 0.5)) / (2 * a))
Now = datetime.now()
time = Now.strftime("%H:%M:%S.%mS")
print("Кінець обчислень о ",time)
	