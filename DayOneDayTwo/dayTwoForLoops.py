import datetime

x = datetime.datetime(2023, 9, 1)

for i in x.strftime("%B"):
  if i == 'e':
    continue
  print(i)
    