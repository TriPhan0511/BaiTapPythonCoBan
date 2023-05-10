"""
2.25. Cho trước các giá trị s tính bằng giây, m tính bằng phút, h tính bằng giờ, d tính bằng ngày.
Viết công thức đổi giá trị "d ngày, h giờ, m phút, s giây" ra:
A. giây
B. phút
C. giờ
"""

"""
s = 10
m = 2
h = 3
d = 1

# A. Công thức đổi ra giây:
ss = d*24*3600 + h*3600 + m*60 + s
print('Số giây: ', ss)

# B. Công thức đổi ra phút:
mm = d*24*60 + h*60 + m + s/60
print('Số phút: ', mm)

# C. Công thức đổi ra giờ:
hh = d*24 + h + m/60 + s/3600
print('Số giờ: ', hh)
"""

s = 10
m = 2
h = 3
d = 1

# Công thức đổi ra giây:
ss = d*24*3600 + h*3600 + m*60 + s
print('Số giây: ', ss)

# Công thức đổi ra phút:
mm = d*24*60 + h*60 + m + s/60
print('Số phút: ', mm)

# Công thức đổi ra giờ:
hh = d*24 + h + m/60 + s/3600
print('Số giờ: ', hh)

# total_of_seconds = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
# total_of_minutes = d * 24 * 60 + h * 60 + m + s // 60
# total_of_hours = d * 24 + h + m // 60 + s // 3600
#
# print('Total of seconds: ', total_of_seconds)
# print('Total of minutes: ', total_of_minutes)
# print('Total of hours: ', total_of_hours)











