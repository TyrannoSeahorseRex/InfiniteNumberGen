specialNumber = float(input("Please input your special number: "))
xnum = 1
znum = specialNumber * xnum

while True:
  print(f"{specialNumber} * {xnum} is {znum}")
  xnum = xnum + 1
  znum = specialNumber * xnum 