a = 0b1101
b = 0b1001

# AND
print(bin(a & b))   # 0b1001

# OR
print(bin(a | b))   # 0b1101

# XOR
print(bin(a ^ b))   # 0b100

# SHIFT
# 왼쪽으로 2칸
print(bin(0b0010 << 2))     # 0b1000
print(bin(0b1100 << 2))     # ob110000

# 오른쪽으로 2칸
print(bin(0b1010 >> 2))    # 0b11
print(bin(0b1111 >> 2))

print(bin(1<<5))    # 0b100000
print(1<<5)         # 32
print(range(1<<5))  # range(32)
print([i for i in range(1<<5)]) # [0, 1, 2 ... 31]

print(bin(0b1111 & 1<<3)) # 0b1111 AND 0b1000 -> 0b1000
print(bin(0b1111 ^ 1<<3)) # 0b1111 XOR 0b1000 -> 0b111
