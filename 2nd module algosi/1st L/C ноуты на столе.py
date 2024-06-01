length_1, width_1, length_2, width_2 = map(int, str(input()).split())

s1 = max(length_1, width_2) * (width_1 + length_2)
s2 = max(length_1, length_2) * (width_1 + width_2)
s3 = max(width_1, width_2) * (length_1 + length_2)
s4 = max(width_1, length_2) * (length_1 + width_2)

if s1 == min(s1, s2, s3, s4):
    print(max(length_1, width_2), (width_1 + length_2))
elif s2 == min(s1, s2, s3, s4):
    print(max(length_1, length_2), (width_1 + width_2))
elif s3 == min(s1, s2, s3, s4):
    print(max(width_1, width_2), (length_1 + length_2))
elif s4 == min(s1, s2, s3, s4):
    print(max(width_1, length_2), (length_1 + width_2))
