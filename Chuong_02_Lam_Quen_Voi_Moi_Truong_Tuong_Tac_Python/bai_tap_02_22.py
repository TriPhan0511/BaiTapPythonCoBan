"""
2.22. Trên thế giới có hai cách thể hiện nhiệt độ: Nhiệt độ C theo Celsius và nhiệt độ K theo Kelvin.
Công thức tính nhiệt độ T theo Kelvin tính theo nhiệt độ t theo Celsius như sau:
T = t + 273.
Viết công thức trong Python tính nhiệt độ Kelvin theo Celsius và ngược lại
"""

"""
Lời giải:
Công thức tính nhiệt độ Kelvin (K) theo Celsius (C):
k = c + 273
Công thức tính nhiệt độ Celsius (C) theo Kelvin (K):
c = k - 273
"""

c = 25
k = c + 273
print('Nhiệt độ C: ', c)  # 25
print('Nhiệt độ K: ', k)  # 298

k = 300
c = k - 273
print('Nhiệt độ K: ', k)  # 300
print('Nhiệt độ C: ', c)  # 27











