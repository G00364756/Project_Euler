#Each new term in the Fibonacci sequence is generated,
#by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence,
#whose values do not exceed four million, find the sum of the even-valued terms.
#Code adapted from code created by Dr. Ian McGloughlin

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  b = 0

  while i <= 4000000:
    i, j = j, i + j
    if i % 2 == 0:
        b = b + i

  return (b)

n = 1
ans = fib(n)
print(ans)
