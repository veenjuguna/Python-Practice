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
print("Is a equal to b?", a == b) # false, a is not equal to b
print("Is a not equal to b?", a != b)#true, a is not equal to b
print("Is a greater than b?", a > b)# true a is greater than b
print("Is a less than b?", a < b)# false, a is not less than b
print("Is a greater than or equal to b?", a >= b)# true, a is greater than or equal to b
print("Is a less than or equal to b?", a <= b)# false, a is not less than or equal to b

#Logical
print("Logical AND:", a > 50 and b < 30) #a=100, so it is true, a is greater than 50 and 25 is less than 30  
print("Logical OR:", a > 50 or b < 20)#a=100 b=25, true is one side is right, so 100 is greater than 50, statement is true.
print("Logical NOT:", not (a > 50))#reverses the condition, so 50 is not greater than 100, therefore the statement is false.

#Bitwise
print("Bitwise AND:", a & b)#1 if both are 1 (100 & 25 = 24 in decimal)
print("Bitwise OR:", a | b)#1 if either bit is 1 (100 | 25 = 101)
print("Bitwise XOR:", a ^ b)#1 if bits differ (100 ^ 25 = 77)
print("Bitwise NOT:", ~a)#flips all bits (for 100, results in -101 due to two’s complement)
print("Left Shift:", a << 2)#Left shift; shifts bits left by 2, multiplying by 4 (100 << 2 = 400)
print("Right Shift:", a >> 2)#Right shift; shifts bits right by 2, dividing by 4 (100 >> 2 = 25)

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
a |= 1 # a = a | 1
print("After |= 1, a:", a)

a <<= 1 # a = a << 1
print("After <<= 1, a:", a)

#Identity
x = [1, 2, 3]#Creates a list.
y = x #Assigns y to the same list object as x (same memory location).
z = x[:] #Creates a new copy of the list (different memory location).
print("Is x identical to y?", x is y) #Checks if x and y are the same object (True, since y = x).
print("Is x identical to z?", x is z) #Checks if x and z are the same object (False, since z is a copy).
print("Is x not identical to y?", x is not y) #Opposite of is (False, since x and y are identical).
print("Is x not identical to z?", x is not z) #True, since x and z are different objects.
