n = int(input())

def Factorial(n):
  if n == 0:
    return 1
  else:
    return Factorial(n - 1) * n

Factorial(n)
