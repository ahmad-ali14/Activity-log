cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

if __name__ == '__main__':
  n = int(input())
  print(cache)
  print(fibonacci(n))