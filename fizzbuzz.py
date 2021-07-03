for i in range(1,101):
  fizzbuzz = ""
  if i%3 == 0:
    fizzbuzz +="fizz"
  if i%5 == 0:
    fizzbuzz +="buzz"
  print(i,fizzbuzz)
