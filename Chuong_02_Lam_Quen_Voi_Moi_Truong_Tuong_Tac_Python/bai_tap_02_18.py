"""
2.18. Giả sử ss = giá trị tính bằng số giây cho trước. Khi đó muốn đổi giá trị này
ra phút và giờ thì dùng công thức tính nào? Chú ý chỉ cần tính tròn phút và tròn giờ.
"""

"""
Đáp án:
Công thức tính, đổi giây thành phút (làm tròn): ss // 60
Công thức tính, đổi giây thành giờ (làm tròn): ss // 3600
"""

ss = 3700
print('Phút = ', ss // 60)
print('Giờ = ', ss // 3600)











