for i in range(-1000,10000):
    s = i
    n = 2
    while s < 85:
      s = s + 15
      n = n * 2
    if n == 64:
        print(i)