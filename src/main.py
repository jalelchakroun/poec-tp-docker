import sys
from calc import apply_vat

price = float(sys.argv[1])
percent = float(sys.argv[2])
res = apply_vat(price, percent)
print(f'Price : {price} $/ percent : {percent}%')
print(f',res:{res}$')
