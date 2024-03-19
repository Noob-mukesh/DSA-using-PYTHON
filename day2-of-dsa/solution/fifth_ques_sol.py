n=2
def fibonacci_series(n):
  if n < 2:
    return n
  else:
    return fibonacci_series(n-1) + fibonacci_series(n-2)


def fabn(n):
    return [fibonacci_series(i) for i in range(n)]

print(fabn(7))
    