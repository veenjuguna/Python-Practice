#basic operations using python

#Arithmetic
a = 100
b = 25

print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b) # Multiplication        
print("Division:", a / b)  # Division
print("Modulus:", a % b)  # Modulus
print("Exponentiation:", a ** b)  # Exponentiation
print("Floor Division:", a // b)  # Floor Division  
#Comparison
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a greater than or equal to b?", a >= b)
print("Is a less than or equal to b?", a <= b)
#Logical
print("Logical AND:", a > 50 and b < 30)    
print("Logical OR:", a > 50 or b < 20)
print("Logical NOT:", not (a > 50))
#Bitwise
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 2)
print("Right Shift:", a >> 2)
#Assignment
a += 10  # a = a + 10
print("After += 10, a:", a)
b -= 5 # b = b - 5
print("After -= 5, b:", b)
a *= 2 # a = a * 2
print("After *= 2, a:", a)
b /= 2
print("After /= 2, b:", b)
a %= 3 # a = a % 3
print("After %= 3, a:", a)
b **= 2 # b = b ** 2
print("After **= 2, b:", b)
a //= 2 # a = a // 2
print("After //= 2, a:", a)
b &= 3 # b = b & 3
print("After &= 3, b:", b)
a |= 1 # a = a | 1
print("After |= 1, a:", a)
b ^= 2 # b = b ^ 2
print("After ^= 2, b:", b)
a <<= 1 # a = a << 1
print("After <<= 1, a:", a)
b >>= 1 # b = b >> 1
print("After >>= 1, b:", b)
#Identity
x = [1, 2, 3]
y = x
z = x[:]
print("Is x identical to y?", x is y)
print("Is x identical to z?", x is z)
print("Is x not identical to y?", x is not y)
print("Is x not identical to z?", x is not z)