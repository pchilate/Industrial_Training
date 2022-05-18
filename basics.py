def func(value):
  if value % 3 == 0 and value % 7 == 0:
      return "tiktok"
  if value % 3 == 0:
      return "tik"
  if value % 7 == 0:
      return "tok"
  return value



n = int(input("Enter you number: "))
print(func(n))




