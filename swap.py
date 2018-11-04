
a = 5
b = 6
print("initial a=", a)
print("initial b=", b)

# 1. using third variable
temp = a
a = b
b = temp
print("after swap a=", a)
print("after swap b=", b)

# 2. without using third variable
a = a + b
b = a - b
a = a - b
print("after swap a=", a)
print("after swap b=", b)

# 3. using xor (^) operator
a = a ^ b
b = a ^ b
a = a ^ b
print("after swap a=", a)
print("after swap b=", b)

# 4. unique in python only
a, b = b, a
print("after swap a=", a)
print("after swap b=", b)
