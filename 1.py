# Вычислить число c заданной точностью d

Number = float(input("Введите число: "))
d = input("Введите точность: ")
from decimal import Decimal
import decimal
rounded = Decimal(Number).quantize(Decimal(d), rounding=decimal.ROUND_FLOOR)
print (rounded)