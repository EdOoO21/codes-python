y = 64**115 + 8**305 - 512
count = 0
while y > 0:
   if y % 8 == 7:
       count+=1
   y //= 8
print(count)