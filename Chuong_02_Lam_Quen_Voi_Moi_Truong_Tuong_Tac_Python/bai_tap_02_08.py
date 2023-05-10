"""
2.8. Đặt tên biến nhớ như sau có được không?
A. a-b-c
B. a_b_c
C. __abc__
D. -a_b_c
"""

"""
Đáp án: 
A. Sai
B. Đúng
C. Đúng
D. Sai
"""
# a-b-c = 'Hello'  # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a_b_c = 'Hello'
__abc__ = 'Hello'
# -a_b_c = 'Hello'  # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

    







