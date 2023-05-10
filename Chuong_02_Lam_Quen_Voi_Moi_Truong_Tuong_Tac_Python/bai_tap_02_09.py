"""
2.9. Các tên định danh sau có hợp lý không trong Python?
A. 1_abc
B. A.B.C
C. ____1_
D. 1.abc
E. a&b&c
"""

"""
Đáp án: 
A. Không
B. Không
C. Có
D. Không
E. Không
"""

# 1_abc = 'Hello'  # SyntaxError: invalid decimal literal
# A.B.C = 'Hello'  # NameError: name 'A' is not defined
____1_ = 'Hello'
# 1.abc = 'Hello'  # SyntaxError: invalid decimal literal
# a&b&c = 'Hello'  # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?








