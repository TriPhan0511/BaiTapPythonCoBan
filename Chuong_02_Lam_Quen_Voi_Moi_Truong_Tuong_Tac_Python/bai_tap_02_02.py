"""
2.2. Các lệnh sau đây có hợp lệ không?
A. x = y = z = 1
B. x = 1, y = 2, z = 3
C. x, y = 1
D. x, y, z = 1, 2, 3
"""

"""
Đáp án:
A. Hợp lệ
B. Không hợp lệ
C. Không hợp lệ
D. Hợp lệ
"""

x = y = z = 1
# x = 1, y = 2, z = 3  # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# x, y = 1  # TypeError: cannot unpack non-iterable int object
x, y, z = 1, 2, 3




