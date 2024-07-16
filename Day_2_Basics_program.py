# Fiboncci series
#
# a, b = 0, 1
# for i in range(0, 10):
#     print(a, end=" ")
#     a, b = b, a+b
#
#
# Factorial of number
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * factorial(number-1)
#
#
# num = int(input("Enter the number: "))
# res = factorial(num)
# print(f"factorial of {num} is {res}")
#
# Armstrong number
# def armstrong(number):
#     sum, temp = 0, number
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     return sum
#
# number = int(input("enter number: "))
# res = armstrong(number)
# if number == res:
#     print(f"entered {number} is armstrong {res}")
# else:
#     print(f"entered {number} is not an armstrong {res}")
#
# Anagram
# def anagram(str1,str2):
#     if (sorted(str1) == sorted(str2)):
#         print(f"entered one is anagram {sorted(str2)} == {sorted(str2)}")
#     else:
#         print("Not an anagram")
#
# str1 =  input("Enter string 1: ")
# str2 =  input("Enter string 2: ")
#
# res = anagram(str1,str2)

# second largest
# def second_largest(list_a):
#     list_a.sort(reverse = True)
#     print(f"sorted list is {list_a}")
#     return list_a[1]
#
#
# list_a = [30,20,40,80,90,99,96,67,78,86]
# res = second_largest(list_a)
# print(f"second largest element in {res}")

# Decimal to binary to hexa

# def decimal_To_binary(number):
#     binary = bin(number)
#     hexa = hex(number)
#     return binary,hexa
#
# number = int(input("Enter number: "))
# binary, hexa = decimal_To_binary(number)
# print(f"binary = {binary} --> {hexa}")

# # program for finding perfect square
# def is_perfect_square(num):
#     if num < 1:
#         return False
#     root = int(num ** 0.5)
#     return root * root == num
#
# # Examples
# print(is_perfect_square(16))  # Output: True
# print(is_perfect_square(9))  # Output: False


# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)
#
# # Example usage
# print(factorial(5))  # Output: 120
