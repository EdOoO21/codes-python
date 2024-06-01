f = [0] * 2250

for x in range(2250):
    if x < 2025:
        f[x] = x ** 2
    if 2025 <= x < 2050:
        f[x] = 2 * f[x - 1] - f[x - 2] + x
    if 2050 <= x <= 2100:
        f[x] = f[x - 1] + 2 * f[x - 2] + 3 * f[x - 3]
    if x > 2100:
        f[x] = 2 * f[x - 1] + f[x - 2] + x

print(f[2020] + f[2200])
